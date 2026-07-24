#!/bin/bash
# Generate Visualizations for Stage 3 Deliverables
echo "Generating Detection Results visualizations..."
mkdir -p /workspace/reports/stage3/visualizations/detections

cd /workspace/external/qfdet-baseline
PYTHONPATH=/workspace/external/qfdet-baseline python tools/test.py \
    qfdet_configs/qfdet_star_r50_fpn_1x_vtuav.py \
    /workspace/weights/epoch_11_qfdet_star_vtuav.pth \
    --show-dir /workspace/reports/stage3/visualizations/detections \
    --show-score-thr 0.3

echo "Visualizations generated in reports/stage3/visualizations/detections"
