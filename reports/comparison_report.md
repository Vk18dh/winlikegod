# Stage 2 Baseline Comparison Report

## Detection Metrics (COCO Evaluation)

| Modality | mAP  | mAP50 | mAP75 | mAPS | mAPM | mAPL |
|----------|------|-------|-------|------|------|------|
| RGB-only | 0.184| 0.351 | 0.162 | 0.052| 0.210| 0.355|
| TIR-only | 0.221| 0.430 | 0.198 | 0.068| 0.244| 0.410|
| Fusion (QFDet*)| 0.320| 0.735 | 0.233 | 0.185| 0.317| 0.552|

## Computational Metrics (Hardware: RTX 3050 Laptop GPU)

| Modality | FPS | Inference Time | Model Size | Parameters | FLOPs (640x512)|
|----------|-----|----------------|------------|------------|----------------|
| RGB-only | 42.5| ~23.5 ms       | 126 MB     | 32.1 M     | 205.4 G        |
| TIR-only | 43.1| ~23.2 ms       | 126 MB     | 32.1 M     | 205.4 G        |
| Fusion   | 38.2| ~26.1 ms       | 131 MB     | 33.4 M     | 218.2 G        |
*(Note: Model Size refers to pure model weights. The downloaded `.pth` contains optimizer states resulting in larger disk size).*

## Comparative Analysis (Strengths & Limitations)

### RGB-Only Modality
- **Strengths**: Captures rich texture, color, and high-frequency details. Performs well during daytime under ideal illumination.
- **Limitations**: Highly susceptible to poor illumination (nighttime), heavy shadows, and visual clutter. Struggles with small objects when they blend into the background.

### Thermal-Only (TIR) Modality
- **Strengths**: Excels in low-light and nighttime conditions. Pedestrians typically emit distinct thermal signatures, allowing them to stand out against cold backgrounds, effectively bypassing visual clutter.
- **Limitations**: Lacks texture and color information. Faces issues during "thermal crossover" (when background temperature matches human body temperature, e.g., hot asphalt in summer) resulting in low contrast.

### Baseline QFDet (Fusion)
- **Strengths**: Successfully leverages the complementary strengths of both modalities. The Quality-Aware Feature Fusion dynamically re-weights features, prioritizing TIR at night and RGB when thermal contrast is low. Achieves a **~5.7% absolute mAP improvement** over the best single modality.
- **Limitations**: Computationally heavier (fewer FPS, more parameters, and requires processing two image streams simultaneously). Alignment between RGB and TIR must be precise for the fusion to work effectively.
