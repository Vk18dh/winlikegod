# Stage 3 Evaluation Report

## Setup
The fine-tuned QFDet model utilizing the Dual Spatial-Channel Attention Gate (DSCAG) was evaluated on the VTUAV subset dataset (val split).

## Quantitative Results (AP Metrics)
- **mAP**: 0.350
- **mAP_50**: 0.754
- **mAP_75**: 0.280
- **mAP_S**: 0.188
- **mAP_M**: 0.332
- **mAP_L**: 0.589

## Computational Results
*(To be populated after evaluation finishes)*

## Qualitative Observations
The model converged very rapidly due to freezing the backbones and prediction heads. The addition of the DSCAG parameters allowed the FPN layers to selectively weight Thermal and RGB streams based on spatial and channel responses.
Interestingly, while overall mAP improved substantially from 0.327 to 0.350 (+2.3%), the small object AP (mAP_S) slightly degraded (0.194 to 0.188). The network heavily optimized for medium and large pedestrians, likely because the 7x7 spatial convolution kernel in the DSCAG over-smoothed the tiny feature activations at higher resolutions, acting as a low-pass filter on the tiniest objects.
