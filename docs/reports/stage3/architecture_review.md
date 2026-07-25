# Stage 3 Architecture Review

## Baseline Analysis
The baseline model (QFDet) utilizes a simple concatenation and 1x1 convolution strategy to fuse RGB and Thermal features (`base_fusion='cat'`). While computationally lightweight, this strategy fundamentally lacks the ability to selectively weight modalities based on content quality. For example, in low-light conditions, Thermal features should heavily dominate RGB features, but a standard concatenation assigns equal inductive importance to both feature maps until deeper layers adapt, which is suboptimal.

Furthermore, analyzing the failure modes from Stage 2 revealed that **small and tiny pedestrians** were frequently missed or resulted in false positives. The initial attempt at a `cmaf.py` module in the repository attempted to solve the modality weighting problem via Cross-Modal Attention using `AdaptiveAvgPool2d` (Channel Attention). However, global average pooling destroys spatial information, meaning the model loses the precise pixel locations of tiny objects, severely hurting small object AP (`mAPS`).

## Weaknesses Identified
1. **Loss of Spatial Resolution**: Using only Channel Attention suppresses spatial context critical for tiny pedestrian bounding box localization.
2. **Modality Imbalance**: Concatenation is inefficient at handling dynamically changing environments (e.g., day vs. night) where one modality is corrupted.
3. **Catastrophic Forgetting Risk**: Fine-tuning the entire detector on the small subset could degrade the FPN and detection heads.

## Solution Proposed
To address this, we designed the **Dual Spatial-Channel Attention Gate (DSCAG)**.

- **Spatial Attention**: Applied first. It uses Max and Average Pooling across the channel dimension to identify the most salient spatial regions in the image, followed by a 7x7 convolution to generate a spatial mask. This ensures the model knows *where* small pedestrians are located in the high-resolution feature maps (like P2).
- **Channel Attention**: Applied next, utilizing the existing squeeze-and-excitation block to determine *which modality* (RGB or Thermal) provides better features for the attended regions.

This architecture directly solves the spatial resolution loss while preserving the dynamic modality weighting required for robust RGB-Thermal fusion.
