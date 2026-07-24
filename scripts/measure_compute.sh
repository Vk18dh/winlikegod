#!/bin/bash
# Stage 4: Measure Computational Profiling
# Usage: ./scripts/measure_compute.sh <model_name> <config_path>

MODEL_NAME=$1
CONFIG=$2
mkdir -p /workspace/results/metrics

echo "Measuring Computational Metrics for: $MODEL_NAME"

echo "Running PyTorch Compute Profiler on real GPU..."
PYTHONPATH=/workspace/external/qfdet-baseline python /workspace/scripts/proper_compute.py $CONFIG $MODEL_NAME

echo "Compute profiling complete."
cat /workspace/results/metrics/${MODEL_NAME}_compute.json
