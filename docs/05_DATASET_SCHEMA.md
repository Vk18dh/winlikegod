# Dataset Schema & Data Architecture

**Project Name:** FusionGuard AI

**Version:** 1.0

**Document Owner:** Team <Team Name>

**Last Updated:** <Date>

---

# Purpose

This document defines the complete data architecture of FusionGuard AI.

Unlike traditional software applications that use relational databases, this project uses an organized dataset-driven architecture.

This document specifies:

- Dataset organization
- Directory structure
- Annotation schema
- Image relationships
- Data validation rules
- Experiment storage
- Model checkpoint storage
- Report storage
- Generated outputs

This document is the authoritative reference for all dataset operations.

---

# Dataset Overview

Dataset Name

VTUAV-det (Curated Hackathon Subset)

Provided By

Yugma TechFest 2.0 AI Hackathon

Task

RGB-Thermal Pedestrian Detection

Supported Class

- Pedestrian

Dataset Type

Multimodal Object Detection Dataset

Modalities

- RGB Images
- Thermal Images
- Bounding Box Annotations

---

# Dataset Directory Structure

```text
datasets/

VTUAV_subset/

train/

rgb/

thermal/

annotations/

val/

rgb/

thermal/

annotations/

test/

rgb/

thermal/

annotations/
```

---

# Image Schema

Each RGB image must have exactly one matching Thermal image.

Relationship

```text
RGB Image

↓

1 : 1

↓

Thermal Image
```

Example

```text
rgb/

000001.jpg

↓

thermal/

000001.jpg
```

The filename must always be identical.

Only the directory changes.

---

# Annotation Schema

Each image pair must have one annotation file.

Relationship

```text
RGB Image

↓

Thermal Image

↓

Annotation File
```

---

# Annotation Format

Each annotation must contain:

- Image ID
- Bounding Boxes
- Category ID
- Width
- Height

Bounding Box Format

```text
[x_min,
 y_min,
 width,
 height]
```

Category

```text
1 = Pedestrian
```

No other classes are permitted.

---

# Data Relationships

```text
Image Pair

↓

Annotation

↓

Detection Target

↓

Prediction

↓

Evaluation
```

Each annotation belongs to exactly one RGB-Thermal image pair.

---

# Dataset Constraints

The following constraints are mandatory.

- Every RGB image must have one Thermal image.
- Every image pair must have an annotation.
- No duplicate filenames.
- No missing images.
- No empty annotation files.
- Only Pedestrian annotations.
- Image resolutions must match.
- File naming must remain unchanged.

---

# Validation Rules

Every dataset validation must verify:

## Image Validation

- Image exists
- Readable
- Correct extension
- Resolution valid

---

## Pair Validation

- RGB image exists
- Thermal image exists
- Matching filename
- Matching resolution

---

## Annotation Validation

- Annotation exists
- Bounding boxes valid
- Coordinates inside image
- Class IDs valid
- No duplicates
- No empty files

---

# Dataset Metadata

The system should automatically generate:

- Number of RGB images
- Number of Thermal images
- Number of image pairs
- Number of annotations
- Total pedestrians
- Average pedestrians/image
- Resolution statistics
- Small/Medium/Large distribution

Generated File

```text
reports/dataset_statistics.md
```

---

# Dataset Versioning

Every dataset version must include:

```text
Version

Creation Date

Source

Description

Hash (optional)
```

Dataset modifications are prohibited.

Only derived outputs may be generated.

---

# Image Processing Pipeline

```text
Load Image

↓

Verify Pair

↓

Read Annotation

↓

Validate

↓

Visualization

↓

Preprocessing (Optional)

↓

Inference
```

---

# Preprocessing Rules

Allowed

- CLAHE
- Histogram Equalization
- Thermal Contrast Enhancement
- Image Normalization

Not Allowed

- Image resizing that breaks annotations
- Dataset modification
- External data augmentation using other datasets

---

# Model Input Schema

Input

```text
RGB Image

+

Thermal Image

↓

Fusion Module

↓

Model
```

Output

```text
Bounding Boxes

Confidence Scores

Class IDs
```

---

# Prediction Schema

Each prediction should contain:

```text
Image ID

Bounding Box

Confidence Score

Category

Inference Time
```

Stored As

```text
results/predictions/
```

---

# Evaluation Schema

Each evaluation generates:

```text
mAP

mAP50

mAP75

mAPS

mAPM

mAPL

Precision

Recall

FPS

Inference Time

Parameters

FLOPs
```

Stored In

```text
reports/evaluation/
```

---

# Experiment Storage

Every experiment receives an isolated directory.

```text
experiments/

EXP-001/

weights/

logs/

predictions/

reports/

config/

visualizations/
```

Experiments must never overwrite each other.

---

# Model Checkpoint Schema

```text
weights/

baseline/

fusion_v1/

fusion_v2/

fusion_v3/

best_model/

latest_checkpoint/
```

Every checkpoint must include:

- Model Name
- Epoch
- Validation Score
- Date
- Git Commit Hash (recommended)

---

# Report Storage

```text
reports/

dataset/

benchmark/

training/

evaluation/

comparison/

submission/
```

Each report must be generated automatically.

---

# Log Storage

```text
logs/

dataset.log

training.log

evaluation.log

benchmark.log

errors.log
```

Logs must never be deleted automatically.

---

# Configuration Files

```text
configs/

dataset.py

model.py

training.py

evaluation.py

fusion.py
```

Configurations should contain no hardcoded paths.

---

# File Naming Convention

Images

```text
000001.jpg
```

Annotations

```text
000001.json
```

Experiments

```text
EXP-001

EXP-002

EXP-003
```

Reports

```text
dataset_report.md

benchmark_report.md

evaluation_report.md
```

---

# Data Integrity Rules

The system must reject:

- Missing image pairs
- Invalid annotations
- Corrupted files
- Duplicate filenames
- Incorrect resolutions
- Invalid bounding boxes
- Unknown class IDs

The validation process must terminate with an informative error message.

---

# AI Coding Agent Rules

Antigravity must always:

- Read dataset paths from configuration files.
- Never hardcode absolute paths.
- Never modify the original dataset.
- Validate the dataset before training.
- Save outputs outside the dataset directory.
- Preserve the original directory hierarchy.
- Generate validation reports automatically.

---

# Acceptance Criteria

This document is complete when:

- Dataset organization is finalized.
- Annotation schema is defined.
- Data relationships are documented.
- Validation rules are specified.
- Storage conventions are finalized.
- Naming conventions are standardized.
- AI agent rules are documented.

This document becomes the official data architecture reference for FusionGuard AI.

---

# Document Status

**Status:** Approved for Development

**Version:** 1.0

**Next Document:** 06_IMPLEMENTATION_PLAN.md