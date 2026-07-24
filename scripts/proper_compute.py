import sys
import torch
import time
import json
import os
from mmcv import Config
from mmdet.models import build_detector
from mmcv.runner import load_checkpoint
from mmcv.cnn.utils.flops_counter import get_model_complexity_info
import torch.nn as nn

class DualImageWrapper(nn.Module):
    """
    Wrapper to fix mmcv's flops_counter which crashes on tuple inputs.
    We pass a 6-channel dummy tensor and split it into RGB and Thermal.
    """
    def __init__(self, model):
        super().__init__()
        self.model = model

    def forward(self, x):
        v_img = x[:, :3, :, :]
        t_img = x[:, 3:, :, :]
        return self.model.forward_dummy([v_img, t_img])

def measure(config_path, model_name):
    print(f"Loading config {config_path}...")
    cfg = Config.fromfile(config_path)
    
    # Build the model
    model = build_detector(cfg.model, train_cfg=cfg.get('train_cfg'), test_cfg=cfg.get('test_cfg'))
    if torch.cuda.is_available():
        model.cuda()
    model.eval()

    print("Measuring FLOPs and Params...")
    try:
        # Wrap the model and pass a 6-channel input (RGB + Thermal)
        wrapped_model = DualImageWrapper(model)
        
        # VTUAV images are 640x512. Input shape for mmcv is (C, H, W)
        flops, params = get_model_complexity_info(wrapped_model, (6, 512, 640), as_strings=True, print_per_layer_stat=False)
        print(f"FLOPs: {flops}, Params: {params}")
    except Exception as e:
        print(f"FLOPs calculation failed: {e}")
        flops, params = "N/A", "N/A"

    print("Measuring FPS (Inference Time) on real GPU...")
    # Warmup
    dummy_v = torch.randn(1, 3, 512, 640).cuda()
    dummy_t = torch.randn(1, 3, 512, 640).cuda()
    
    with torch.no_grad():
        for _ in range(20):
            model.forward_dummy([dummy_v, dummy_t])
            
        # Benchmark
        torch.cuda.synchronize()
        start_time = time.time()
        num_runs = 100
        for _ in range(num_runs):
            model.forward_dummy([dummy_v, dummy_t])
        torch.cuda.synchronize()
        end_time = time.time()

    total_time = end_time - start_time
    time_per_img_ms = (total_time / num_runs) * 1000
    fps = 1000 / time_per_img_ms
    print(f"Inference Time: {time_per_img_ms:.2f} ms")
    print(f"FPS: {fps:.2f}")

    # Model Size (approximate from params)
    # 1 param = 4 bytes (float32)
    # Convert to MB
    total_params = sum(p.numel() for p in model.parameters())
    model_size_mb = (total_params * 4) / (1024 * 1024)
    print(f"Model Size: {model_size_mb:.2f} MB")

    out_path = f"/workspace/results/metrics/{model_name}_compute.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, 'w') as f:
        json.dump({
            "FLOPs": flops,
            "Params": params,
            "FPS": round(fps, 2),
            "Inference Time": round(time_per_img_ms, 2),
            "Model Size": round(model_size_mb, 2)
        }, f, indent=4)
    
    print(f"Metrics saved to {out_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python proper_compute.py <config_path> <model_name>")
        sys.exit(1)
    measure(sys.argv[1], sys.argv[2])
