#!/bin/bash
set -e

if ! python -c "import mmcv" &> /dev/null; then
    echo "Starting Docker Evaluation Environment Setup..."
    
    # Install OpenCV system dependencies
    apt-get update && apt-get install -y libgl1 libglib2.0-0 libxcb1
    
    # Update pip
    pip install --upgrade pip
    
    # Install MMCV
    pip install -U openmim
    mim install mmcv-full==1.7.0
    
    # Install QFDet Requirements
    cd /workspace/external/qfdet-baseline
    pip install "numpy<2"
    pip install -r requirements/build.txt
    pip install -r requirements/runtime.txt
else
    echo "Environment already set up! Skipping installation..."
fi

echo "Setup Complete! Running Stage 2 Inference..."

# Ensure outputs directory exists
mkdir -p /workspace/reports/raw_metrics

echo "Running Stage 2 Inference for Fusion Baseline..."
cd /workspace/external/qfdet-baseline
PYTHONPATH=/workspace/external/qfdet-baseline python tools/test.py qfdet_configs/qfdet_star_r50_fpn_1x_vtuav.py /workspace/weights/epoch_11_qfdet_star_vtuav.pth --eval bbox > /workspace/reports/raw_metrics/fusion_eval.txt

echo "Evaluation finished! Results saved to /workspace/reports/raw_metrics/"
