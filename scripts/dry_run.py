import sys
import torch
from mmcv.utils import Config
from mmdet.datasets import build_dataset, build_dataloader
from mmdet.models import build_detector
from mmcv.runner import load_checkpoint

def main():
    print("Loading config...")
    cfg = Config.fromfile('external/qfdet-baseline/qfdet_configs/qfdet_cmaf_finetune.py')
    
    print("Building model...")
    model = build_detector(
        cfg.model,
        train_cfg=cfg.get('train_cfg'),
        test_cfg=cfg.get('test_cfg'))
    
    print("Loading baseline checkpoint...")
    load_checkpoint(model, cfg.load_from, map_location='cpu')
    
    print("Building dataset...")
    dataset = build_dataset(cfg.data.train)
    
    print("Building dataloader...")
    data_loader = build_dataloader(
        dataset,
        samples_per_gpu=1,
        workers_per_gpu=0,
        dist=False,
        seed=42)
    
    print("Fetching one batch...")
    batch = next(iter(data_loader))
    
    print("Pushing to GPU...")
    model = model.cuda()
    
    if isinstance(batch['img'], list):
        img = tuple(i.data[0].cuda() for i in batch['img'])
    else:
        img = batch['img'].data[0].cuda()
        
    img_metas = batch['img_metas'].data[0]
    gt_bboxes = [b.cuda() for b in batch['gt_bboxes'].data[0]]
    gt_labels = [l.cuda() for l in batch['gt_labels'].data[0]]
    
    print("Performing forward pass...")
    losses = model.forward_train(img, img_metas, gt_bboxes, gt_labels)
    
    print("Validating loss computation...")
    loss, log_vars = model._parse_losses(losses)
    print(f"Total Loss computed successfully: {loss.item():.4f}")
    
    print("Dry run completely successful! Memory and architecture are intact.")

if __name__ == '__main__':
    main()
