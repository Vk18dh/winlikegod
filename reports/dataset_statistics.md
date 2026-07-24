# Dataset Statistics

## Overview
- **Total Images**: 1700
- **Total Valid Annotations**: 12541
- **Image Resolution**: 1920x1080 (uniform across all splits)
- **Annotation Format**: COCO JSON (category_id=0, 'person')

## Split Breakdown
| Split | Images | Valid Anns | Avg Ped/Img | Max Ped/Img | Paired |
|-------|--------|------------|-------------|-------------|--------|
| train | 1200   | 8138       | 6.78        | 99          | 1200   |
| val   | 300    | 2336       | 7.79        | 61          | 300    |
| test  | 200    | 2067       | 10.34       | 61          | 200    |
| **TOTAL** | **1700** | **12541** | - | - | **1700** |

## Bounding Box Statistics
- **Area**: min=114, mean=6127, median=3690, max=394210 (px^2)
- **Scale Distribution**:
  - Small (< 1024 px^2): 1759 (14.0%)
  - Medium (1024-9216 px^2): 8311 (66.3%)
  - Large (>= 9216 px^2): 2471 (19.7%)

## Key Findings
- Small pedestrians dominate: 14.0% of all instances.
- RGB-TIR pairing: PERFECT (0 mismatches in all splits).
- TIR format: 3-channel BGR JPG with identical channels (pseudo-grayscale).
- 2 zero-area annotations were removed (val=1, test=1).
- Alignment Mean Edge NCC: 0.0129.
