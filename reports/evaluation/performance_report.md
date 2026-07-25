# Performance Report (Edge Viability)

## Hardware Constraints
- **Target Device Requirements**: The system is designed to run on Edge GPUs (e.g. NVIDIA Jetson Nano / Orin, RTX 3050 Mobile).
- **VRAM Limitations**: To avoid Out-Of-Memory (OOM) and Bus Errors on 4GB VRAM devices, we utilize `workers_per_gpu=0` and gradient checkpointing.

## Optimization Techniques
1. **Automatic Mixed Precision (FP16)**: Reduces tensor precision during the forward and backward passes from 32-bit floating point to 16-bit, halving memory bandwidth constraints.
2. **Batch Normalization Fusion (`--fuse-conv-bn`)**: Mathematically fuses Batch Normalization layers into their preceding Convolutional layers. This completely eliminates BN computational overhead during inference.

## Final Metrics
- **Model Size**: 15.65 Million Parameters (74% reduction from Baseline)
- **Inference Speed**: 4.75 FPS on RTX 3050 Mobile (Drone-deployable)
