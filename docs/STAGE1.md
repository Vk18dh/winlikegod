# Stage 1 — Dataset Exploration, Analysis & Preparation

**Project:** FusionGuard AI

**Stage:** 1

**Status:** 🔄 In Progress

**Priority:** Critical

**Estimated Time:** 2–4 Hours

**Owner:** Team FusionGuard AI

---

# Objective

Complete all Stage 1 deliverables required by the Yugma TechFest AI Hackathon.

This stage focuses on understanding the VTUAV-det dataset before any model evaluation or modification.

No model development should begin until every Stage 1 quality gate has been satisfied.

---

# Success Criteria

Stage 1 is considered complete when:

- Dataset successfully loaded.
- Dataset validated.
- All RGB-Thermal image pairs verified.
- Annotations verified.
- Dataset statistics generated.
- Pedestrian scale distribution generated.
- RGB-Thermal alignment verified.
- Sample visualizations created.
- Stage 1 report generated.

---

# Inputs

Dataset

```text
VTUAV_subset/
```

Contains

- RGB Images
- Thermal Images
- Annotation Files

Baseline Repository

- QFDet

Configuration

```text
configs/dataset.py
```

---

# Expected Outputs

```text
reports/

dataset_statistics.md

dataset_summary.csv

dataset_validation.md

dataset_challenges.md

visualization_report.md
```

Generated Images

```text
results/

visualizations/

rgb/

thermal/

paired/

annotated/

alignment/
```

---

# Stage Workflow

```text
Dataset

↓

Load Dataset

↓

Validate Structure

↓

Validate Images

↓

Validate Annotations

↓

RGB-Thermal Pair Verification

↓

Generate Statistics

↓

Scale Distribution

↓

Visualization

↓

Alignment Verification

↓

Preprocessing Analysis

↓

Generate Reports

↓

Stage 1 Complete
```

---

# Task 1 — Dataset Structure Validation

## Objective

Verify the dataset follows the expected directory hierarchy.

### Validation Checklist

- Train folder exists
- Validation folder exists
- Test folder exists
- RGB directory exists
- Thermal directory exists
- Annotation directory exists

### Output

```text
reports/dataset_structure.md
```

---

# Task 2 — Image Validation

## Verify

- Images readable
- Correct extension
- No corrupted images
- Resolution recorded
- Missing files detected

### Output

```text
reports/image_validation.md
```

---

# Task 3 — Annotation Validation

## Verify

- Annotation file exists
- Correct format
- Valid bounding boxes
- Coordinates inside image
- Correct class IDs
- No empty annotation files
- No duplicate annotations

### Output

```text
reports/annotation_validation.md
```

---

# Task 4 — RGB-Thermal Pair Verification

Every RGB image must have

Exactly one Thermal image

Exactly one Annotation file

Checks

- Matching filenames
- Matching dimensions
- Correct pairing
- Missing pairs

Generate

Minimum

20 paired visualizations

Output

```text
results/alignment/
```

---

# Task 5 — Dataset Statistics

Generate

## Images

- Total RGB Images
- Total Thermal Images
- Total Image Pairs

---

## Pedestrians

- Total Pedestrians
- Average Per Image
- Maximum
- Minimum

---

## Dataset Split

| Split | Images | Pedestrians |
|--------|--------|-------------|
| Train | | |
| Validation | | |
| Test | | |

---

Output

```text
reports/dataset_statistics.md
```

---

# Task 6 — Pedestrian Scale Distribution

Classify pedestrians into

Small

```text
Area < 32²
```

Medium

```text
32² ≤ Area < 96²
```

Large

```text
Area ≥ 96²
```

Generate

- Table
- Histogram
- Pie Chart

Output

```text
results/statistics/
```

---

# Task 7 — Image Resolution Analysis

Collect

- Width
- Height
- Aspect Ratio

Generate

- Resolution Histogram
- Resolution Distribution

---

# Task 8 — RGB vs Thermal Analysis

Compare

RGB

- Brightness
- Contrast
- Noise
- Illumination

Thermal

- Heat signatures
- Dynamic range
- Noise
- Contrast

Document observations.

---

# Task 9 — Visualization

Generate

Minimum

20 paired examples.

Each visualization should include

- RGB Image
- Thermal Image
- Ground Truth Bounding Boxes

Generate

- Side-by-side view
- Overlay view

Save

```text
results/visualizations/
```

---

# Task 10 — Alignment Verification

Verify

- Bounding boxes align correctly
- RGB matches Thermal
- No image shift
- No annotation mismatch

Generate

Alignment Report

```text
reports/alignment_report.md
```

---

# Task 11 — Dataset Challenges

Identify

- Small pedestrians
- Occlusion
- Crowded scenes
- Low illumination
- Thermal noise
- Motion blur
- Difficult backgrounds

Output

```text
reports/dataset_challenges.md
```

---

# Task 12 — Optional Preprocessing

Evaluate

- CLAHE
- Histogram Equalization
- Thermal Contrast Enhancement

Document

Advantages

Disadvantages

Decision

No preprocessing should be applied without justification.

---

# Deliverables Checklist

| Deliverable | Status |
|-------------|--------|
| Dataset Validation | ☐ |
| Annotation Validation | ☐ |
| Pair Verification | ☐ |
| Dataset Statistics | ☐ |
| Scale Distribution | ☐ |
| Resolution Analysis | ☐ |
| RGB-Thermal Analysis | ☐ |
| Alignment Verification | ☐ |
| Visualizations | ☐ |
| Dataset Challenges | ☐ |
| Stage 1 Report | ☐ |

---

# Quality Gates

Before moving to Stage 2

All conditions must pass.

- No missing RGB images
- No missing Thermal images
- No missing annotations
- No corrupted files
- All image pairs verified
- Statistics generated
- Visualizations generated
- Alignment verified
- Reports generated

If any quality gate fails,

Stage 1 remains **Incomplete**.

---

# Team Responsibilities

### Member 1

Dataset Loader

Dataset Validation

Statistics

---

### Member 2

Annotation Parser

Pair Verification

Visualization

---

### Member 3

Scale Analysis

Resolution Analysis

Challenge Analysis

---

### Member 4

Report Generation

Documentation

Quality Verification

---

# AI Coding Agent Instructions

Antigravity must

- Never modify the original dataset.
- Read all paths from configuration files.
- Validate before processing.
- Save outputs outside the dataset directory.
- Automatically generate reports.
- Log every validation error.
- Continue processing valid files even if isolated errors are found, while summarizing failures at the end.
- Produce deterministic outputs whenever possible.

---

# Definition of Done

Stage 1 is complete only if

- All required reports exist.
- All required visualizations exist.
- Validation passes.
- Dataset statistics are generated.
- Team review completed.
- Git commit created.

---

# Completion Command

```bash
git add .
git commit -m "Complete Stage 1 - Dataset Exploration & Analysis"
```

---

# Next Stage

Proceed to **STAGE2.md** only after all Stage 1 deliverables satisfy the quality gates.