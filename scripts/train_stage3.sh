#!/bin/bash
# Train Stage 3 - CMAF Fine-tuning

echo "Starting Stage 3 CMAF Fine-Tuning..."
cd /workspace

CONFIG_FILE="external/qfdet-baseline/qfdet_configs/qfdet_cmaf_r50_fpn_1x_vtuav.py"
CHECKPOINT_FILE="/workspace/weights/epoch_11_qfdet_star_vtuav.pth"
WORK_DIR="work_dirs/stage3_cmaf"

# Ensure output directory exists
mkdir -p $WORK_DIR

# Start training
PYTHONPATH=/workspace/external/qfdet-baseline python external/qfdet-baseline/tools/train.py \
    $CONFIG_FILE \
    --work-dir $WORK_DIR \
    --seed 42 \
    --deterministic
    
echo "Training complete!"
