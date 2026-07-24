import os
import sys
import platform

def check_env():
    md = []
    md.append("# Environment Check Report")
    md.append("")
    
    md.append("## System")
    md.append(f"- **OS**: {platform.system()} {platform.release()}")
    md.append(f"- **Python**: {sys.version.split()[0]}")
    
    md.append("\n## PyTorch & CUDA")
    try:
        import torch
        md.append(f"- **PyTorch**: {torch.__version__}")
        md.append(f"- **CUDA Available**: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            md.append(f"- **CUDA Device**: {torch.cuda.get_device_name(0)}")
            md.append(f"- **CUDA Version**: {torch.version.cuda}")
    except ImportError:
        md.append("- **PyTorch**: Not Installed or Failed to Import")
    
    md.append("\n## MMLab Dependencies")
    try:
        import mmdet
        md.append(f"- **MMDetection**: {mmdet.__version__}")
    except ImportError:
        md.append("- **MMDetection**: Not Installed")
        
    try:
        import mmcv
        md.append(f"- **MMCV**: {mmcv.__version__}")
    except ImportError:
        md.append("- **MMCV**: Not Installed")
        
    try:
        import mmengine
        md.append(f"- **MMEngine**: {mmengine.__version__}")
    except ImportError:
        md.append("- **MMEngine**: Not Installed")
        
    md.append("\n## OpenCV")
    try:
        import cv2
        md.append(f"- **OpenCV**: {cv2.__version__}")
    except ImportError:
        md.append("- **OpenCV**: Not Installed")
        
    report_path = "reports/environment_check.md"
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    
    print("Environment check report generated at", report_path)

if __name__ == "__main__":
    check_env()
