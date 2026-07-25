#!/bin/bash
# Stage 4: Automated Evaluation Script
# Usage: ./scripts/evaluate_model.sh <model_name> <config_path> <checkpoint_path>

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <model_name> <config_path> <checkpoint_path>"
    exit 1
fi

MODEL_NAME=$1
CONFIG=$2
CHECKPOINT=$3

echo "======================================"
echo "Evaluating Model: $MODEL_NAME"
echo "Config: $CONFIG"
echo "Checkpoint: $CHECKPOINT"
echo "======================================"

# Ensure directories exist
mkdir -p /workspace/results/predictions
mkdir -p /workspace/results/metrics

# Run MMDetection inference and evaluation
# Output predictions to PKL for visualization
# Output raw text to TXT for parsing
PYTHONPATH=/workspace/external/qfdet-baseline python /workspace/external/qfdet-baseline/tools/test.py \
    $CONFIG \
    $CHECKPOINT \
    --fuse-conv-bn \
    --out /workspace/results/predictions/${MODEL_NAME}.pkl \
    --eval bbox > /workspace/results/metrics/${MODEL_NAME}_raw.txt

echo "Generating Official COCO JSON Submission Format..."
PYTHONPATH=/workspace/external/qfdet-baseline python /workspace/external/qfdet-baseline/tools/test.py \
    $CONFIG \
    $CHECKPOINT \
    --format-only --eval-options "jsonfile_prefix=/workspace/results/predictions/coco_format_${MODEL_NAME}"

echo "Raw evaluation complete. Parsing metrics..."

# Run python parser to convert raw txt to clean JSON
python /workspace/scripts/parse_metrics.py /workspace/results/metrics/${MODEL_NAME}_raw.txt /workspace/results/metrics/${MODEL_NAME}.json

echo "Running Compute Profiler..."
bash /workspace/scripts/measure_compute.sh $MODEL_NAME $CONFIG

echo "Generating Visualizations..."
python /workspace/scripts/visualize_predictions.py $MODEL_NAME

echo "Evaluation Pipeline Complete for $MODEL_NAME."
echo "Metrics saved to: /workspace/results/metrics/${MODEL_NAME}.json"
