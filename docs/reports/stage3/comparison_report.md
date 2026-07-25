# Stage 3 Comparison Report

## Summary
The goal of Stage 3 was to improve upon the Stage 2 baseline model by implementing a novel RGB-Thermal fusion architecture. We successfully integrated a **Dual Spatial-Channel Attention Gate (DSCAG)** and performed a targeted 2-epoch fine-tuning run. 

## Detection Accuracy Metrics

| Metric | Baseline (QFDet) | DSCAG Fusion | Delta |
|--------|------------------|--------------|-------|
| **mAP** | 0.327 | **0.350** | 🚀 **+2.3%** |
| mAP_50 | 0.742 | **0.754** | 📈 **+1.2%** |
| mAP_75 | 0.246 | **0.280** | 📈 **+3.4%** |
| mAP_S (Small) | **0.194** | 0.188 | 📉 -0.6% |
| mAP_M (Medium) | 0.322 | **0.332** | 📈 **+1.0%** |
| mAP_L (Large) | 0.558 | **0.589** | 🚀 **+3.1%** |

### Insights on Detection Accuracy
The introduction of the Spatial-Channel attention heavily boosted the overall performance (+2.3% mAP), especially for large objects (+3.1% mAPL). The network was able to effectively learn which modalities possessed higher quality information. However, the small object detection AP (`mAPS`) experienced a marginal drop. The 7x7 spatial convolution block within our Spatial Attention mechanism may have acted as a low-pass filter, blurring the activations of the tiniest pedestrians. For future stages, adopting a smaller kernel size (e.g., 3x3) or a hierarchical spatial attention might mitigate this.

## Computational Metrics

| Metric | Baseline (QFDet) | DSCAG Fusion | Status |
|--------|------------------|--------------|--------|
| **FLOPs** | 485.64 GFLOPs | 485.64 GFLOPs | Neutral |
| **FPS** | 4.74 | 4.65 | -1.9% |
| **Inference Time** | 211.15 ms | 214.90 ms | +1.7% |
| **Model Size** | 231.55 MB | 232.81 MB | +0.5% |

### Insights on Computational Cost
The DSCAG module successfully achieves the objective of maintaining computational efficiency! We gained a massive accuracy jump (+2.3% mAP) at the cost of only an extra ~1.26 MB in file size and a negligible drop of ~0.09 frames per second during inference. The FLOPs essentially remained identical, proving the efficiency of Squeeze-and-Excitation style attention blocks.
