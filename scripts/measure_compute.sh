#!/bin/bash
# Stage 4: Measure Computational Profiling
# Usage: ./scripts/measure_compute.sh <model_name> <config_path>

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <model_name> <config_path>"
    exit 1
fi

MODEL_NAME=$1
CONFIG=$2

echo "======================================"
echo "Measuring Compute for: $MODEL_NAME"
echo "======================================"

mkdir -p /workspace/results/metrics

# 1. Get FLOPs and Params
echo "Calculating FLOPs and Parameters..."
PYTHONPATH=/workspace/external/qfdet-baseline python /workspace/external/qfdet-baseline/tools/analysis_tools/get_flops.py $CONFIG > /workspace/results/metrics/${MODEL_NAME}_flops.txt

# Extract FLOPs and Params using grep and awk
FLOPS=$(grep "FLOPs:" /workspace/results/metrics/${MODEL_NAME}_flops.txt | awk -F ': ' '{print $2}')
PARAMS=$(grep "Params:" /workspace/results/metrics/${MODEL_NAME}_flops.txt | awk -F ': ' '{print $2}')

# Note: The benchmark script requires an actual checkpoint to run FPS correctly without random init overhead.
# For simplicity, we just use the architecture definition to get FLOPs and skip actual FPS benchmark if we don't pass a checkpoint.
# We will just save FLOPs and Params to JSON.

echo "{" > /workspace/results/metrics/${MODEL_NAME}_compute.json
echo "  \"FLOPs\": \"$FLOPS\"," >> /workspace/results/metrics/${MODEL_NAME}_compute.json
echo "  \"Params\": \"$PARAMS\"" >> /workspace/results/metrics/${MODEL_NAME}_compute.json
echo "}" >> /workspace/results/metrics/${MODEL_NAME}_compute.json

echo "Compute profiling complete."
cat /workspace/results/metrics/${MODEL_NAME}_compute.json
