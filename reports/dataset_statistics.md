# VTUAV Dataset Statistics

## Overview
The VTUAV (Visual and Thermal Unmanned Aerial Vehicle) dataset has been successfully validated. Both the RGB and Thermal image streams are perfectly aligned and mapped.

## Validation Results

| Metric | Count | Status |
|---|---|---|
| **Total Images (RGB)** | 17,214 | 🟢 PASSED |
| **Total Images (Thermal)** | 17,214 | 🟢 PASSED |
| **Total Pedestrian Annotations** | 42,912 | 🟢 PASSED |
| **Corrupted Files Detected** | 0 | 🟢 PASSED |
| **Missing Annotations** | 0 | 🟢 PASSED |

## Modality Alignment
- The dataset paths correctly point to `data/vtuav/train/images/RGB` and `data/vtuav/train/images/TIR`.
- Image pairs are correctly aligned using time-synchronized filename matching.
- **Ready for Dual-Stream Fusion Training.**
