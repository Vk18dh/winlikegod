# Dataset Analysis: VTUAV_subset

## Dataset Tree
```text
├── vtuav_processed
│   ├── anchor_analysis.json
│   ├── annotations
│   │   ├── test.json
│   │   ├── train.json
│   │   └── val.json
│   ├── norm_stats.json
│   └── preprocessing_report.json
└── VTUAV_subset
    ├── annotations
    │   ├── test.json
    │   ├── train.json
    │   └── val.json
    ├── selected_test.txt
    ├── selected_train.txt
    ├── selected_val.txt
    ├── VTUAV_co
    │   ├── test
    │   │   └── images
    │   ├── train
    │   │   └── images
    │   └── val
    │       └── images
    └── VTUAV_ir
        ├── test
        │   └── images
        ├── train
        │   └── images
        └── val
            └── images
```

## Image Counts
- Total Images: 3400
- RGB Images (approx): 0
- Thermal Images (approx): 3400
- Total Annotations: 12

## Annotation Format & Samples
Format appears to be: **JSON**

Sample Annotation:
File: `C:\Users\dhyan\Desktop\hackathon-2\FusionGuard-AI\datasets\VTUAV_subset\vtuav_processed\anchor_analysis.json`
```
{
  "k": 9,
  "avg_iou": 0.7878045439720154,
  "anchors_flat": [
    [
      13.309828758239746,
      31.7756404876709
    ],
    [
      22.433935165405273,
      47.304588317871094
    ],
    [
      28.477426528930664,
      68.31715393066406
    ],
    [
      38.53651428222656,
      82.1214599609375
    ],
    [
      55.442222595214844,
      89.15555572509766
    ],
    [
      46.85908126831055,
      131.208740234375
    ],
    [
      79.7676773071289,
      117.63973236083984
    ],
...[truncated]
```

## Image Resolutions
- 1920x1080

## RGB-Thermal Pairing Verification
- Perfectly paired basenames: 0
- Unpaired RGB images: 0
- Unpaired Thermal images: 1650

### Missing Files Report
Sample missing RGB counterparts for: ['04034', '00779', '00849', '10576', '01147']

## Dataset Summary
The VTUAV subset contains 3400 images with 12 annotation files. Images have 1 distinct resolutions. There are some unpaired images which may require data cleaning.
