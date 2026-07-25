# Stage 3 Fusion Strategy: Dual Spatial-Channel Attention Gate (DSCAG)

## Objective
To develop an RGB-Thermal fusion architecture that outperforms the baseline model's naive concatenation, with a specific focus on improving small and tiny pedestrian detection.

## Design Concept
The baseline QFDet fuses modalities late in the network (in the neck/FPN) using element-wise concatenation and a 1x1 convolution reduction layer. This gives both modalities equal inductive bias, which performs poorly if one modality is heavily degraded (e.g., RGB during nighttime). 

Our novel strategy replaces the concatenation layer with a **Dual Spatial-Channel Attention Gate (DSCAG)**.

### Step 1: Spatial Attention
Small object localization requires fine-grained spatial information. If a tiny pedestrian is visible in the Thermal camera but hidden by a bush in RGB, the model must spatially isolate those pixels.
We implemented a Spatial Attention module that computes both the Max Pool and Average Pool along the channel dimensions of the feature maps, concatenates them, and passes them through a 7x7 spatial convolution. This creates a spatial mask highlighting regions of interest.

### Step 2: Channel Attention
Once the regions of interest are spatially weighted, a standard Squeeze-and-Excitation (SE) channel attention module evaluates the global context of the feature map to determine the inter-channel weighting (effectively choosing whether the RGB or Thermal feature maps are more reliable for the current frame).

## Implementation Details
- **Residual Integration**: To ensure the model doesn't suffer catastrophic degradation at the beginning of fine-tuning, the DSCAG module implements a residual identity initialization `key + 0.0 * (attn_key - key)`. This allows the pre-trained FPN weights to act exactly as they did in the baseline at Step 0, and the attention parameters smoothly ramp up their influence via gradient descent.
- **Layer Freezing**: During fine-tuning, the QFDet backbones (RGB and Thermal), FPN neck, and regression/classification heads were explicitly frozen. Only the new DSCAG attention weights were allowed to update. This prevents catastrophic forgetting on the tiny VTUAV dataset subset while drastically speeding up the fine-tuning convergence.
