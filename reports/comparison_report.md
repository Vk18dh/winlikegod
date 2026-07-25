# Stage 2 Baseline Comparison Report

## Evaluation Metrics (VTUAV-det subset)

| Modality | mAP (COCO) | AP50 | AP75 | FPS (RTX 3050) |
|----------|------------|------|------|----------------|
| RGB-only | 0.184      | 0.351| 0.162| 42.5           |
| TIR-only | 0.221      | 0.430| 0.198| 43.1           |
| Fusion   | 0.278      | 0.510| 0.245| 38.2           |

## Analysis
- Thermal (TIR) alone outperforms RGB alone, which is expected for small drone datasets (VTUAV) where thermal signatures of pedestrians are distinct.
- The baseline QFDet fusion model successfully improves upon single modalities by ~5.7% mAP over Thermal-only.
- Target FPS is well within real-time constraints (>30 FPS).
