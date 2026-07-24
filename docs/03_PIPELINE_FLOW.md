# Pipeline Flow Document

**Project Name:** FusionGuard AI

**Version:** 1.0

**Document Owner:** Team <Team Name>

**Last Updated:** <Date>

---

# Purpose

This document defines the complete execution pipeline of FusionGuard AI.

It describes how data flows through the system, how each module interacts, the execution order, dependencies, expected inputs and outputs, failure handling, and completion criteria.

This document serves as the architectural reference for all developers and AI coding agents.

Every implementation must follow the pipeline described below.

---

# High-Level Pipeline

```text
                 ┌────────────────────┐
                 │  VTUAV-det Dataset │
                 └─────────┬──────────┘
                           │
                           ▼
              Dataset Verification Module
                           │
                           ▼
              Annotation Validation Module
                           │
                           ▼
            RGB-Thermal Pair Verification
                           │
                           ▼
                Dataset Analysis Module
                           │
                           ▼
                Dataset Visualization
                           │
                 (Stage 1 Completed)
                           │
                           ▼
               Load Pretrained QFDet
                           │
             ┌─────────────┼──────────────┐
             ▼             ▼              ▼
        RGB Model     Thermal Model   Fusion Model
             │             │              │
             └─────────────┼──────────────┘
                           ▼
                    Model Evaluation
                           │
                           ▼
               Performance Benchmarking
                           │
                           ▼
                 Comparative Analysis
                           │
                           ▼
              Improved Fusion Development
                           │
                           ▼
                    Final Evaluation
                           │
                           ▼
                 Report Generation
                           │
                           ▼
                  Hackathon Submission
```

---

# Pipeline Overview

The project is divided into four independent execution stages.

Each stage produces outputs required by the following stage.

No stage should begin until the previous stage has been validated.

---

# Stage 1

## Dataset Exploration & Preparation

### Goal

Understand the dataset completely before model evaluation.

---

## Inputs

- RGB Images
- Thermal Images
- Annotation Files
- Dataset Metadata

---

## Processing Steps

### Step 1

Load Dataset

↓

Verify folder structure

↓

Verify image count

↓

Verify annotation count

↓

Generate dataset summary

---

### Step 2

Annotation Validation

Checks

- Missing annotations

- Invalid coordinates

- Duplicate annotations

- Invalid class IDs

- Empty annotation files

Output

Validated dataset

---

### Step 3

RGB-Thermal Pair Verification

Checks

- Missing RGB images

- Missing Thermal images

- Incorrect filenames

- Resolution mismatch

- Alignment mismatch

Output

Verified image pairs

---

### Step 4

Dataset Statistics

Generate

- Number of images

- Number of pedestrians

- Average pedestrians/image

- Image resolution

- Class distribution

- Train/Validation/Test statistics

---

### Step 5

Pedestrian Scale Analysis

Calculate

Small

Medium

Large

Distribution

Generate graphs.

---

### Step 6

Visualization

Generate

- RGB Images

- Thermal Images

- Side-by-side comparison

- Bounding boxes

- Overlay visualization

Minimum

20 image pairs

---

### Step 7

Optional Preprocessing

Evaluate

- Histogram Equalization

- CLAHE

- Thermal Contrast Enhancement

Apply only if justified.

---

### Outputs

Dataset Report

Statistics

Visualizations

Verification Report

Analysis Report

---

### Done Criteria

Dataset fully validated.

No missing files.

Statistics generated.

Visualizations generated.

Reports generated.

---

# Stage 2

## Baseline Benchmarking

### Goal

Establish baseline performance before proposing improvements.

---

## Inputs

Validated dataset

Pretrained QFDet

Configuration files

---

## Step 1

Load pretrained checkpoint.

Validate checkpoint integrity.

---

## Step 2

Run RGB-only inference.

Collect metrics.

---

## Step 3

Run Thermal-only inference.

Collect metrics.

---

## Step 4

Run Baseline Fusion Model.

Collect metrics.

---

## Step 5

Generate Evaluation Metrics

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

Model Size

---

## Step 6

Generate Benchmark Report

Include

Comparison tables

Performance graphs

Observations

Failure cases

---

### Outputs

Benchmark Report

Evaluation Metrics

Prediction Results

Comparison Charts

---

### Done Criteria

RGB benchmark completed.

Thermal benchmark completed.

Fusion benchmark completed.

Reports generated.

---

# Stage 3

## Fusion Strategy Development

### Goal

Improve baseline performance using an innovative RGB-Thermal fusion strategy.

---

## Inputs

Baseline model

Evaluation report

Dataset

---

## Pipeline

Baseline

↓

Feature Extraction

↓

Feature Fusion

↓

Attention Module

↓

Small Object Enhancement

↓

Detection Head

↓

Prediction

↓

Evaluation

---

## Experiment Loop

```text
Fusion Strategy

↓

Training

↓

Validation

↓

Evaluation

↓

Performance Improvement?

      │

   Yes ─────────► Save Model

      │

      No

      │

Modify Fusion Strategy

      │

      ▼

Repeat
```

---

## Outputs

Improved model

Trained weights

Experiment logs

Evaluation reports

---

### Done Criteria

Performance exceeds baseline.

Training stable.

Experiments documented.

---

# Stage 4

## Final Evaluation

### Goal

Compare the improved model against the baseline.

---

## Inputs

Baseline

Improved Model

Validation Dataset

Test Dataset

---

## Evaluation

Quantitative

- COCO Metrics

- FPS

- FLOPs

- Model Size

Qualitative

- Detection Visualization

- Failure Cases

- False Positives

- False Negatives

---

## Outputs

Final Report

Performance Charts

Comparison Tables

Submission Files

---

### Done Criteria

All required deliverables generated.

---

# Module Dependencies

```text
Dataset

↓

Validation

↓

Visualization

↓

Benchmark

↓

Fusion

↓

Evaluation

↓

Report
```

Each module depends only on outputs from the previous stage.

Circular dependencies are prohibited.

---

# Failure Handling

The pipeline must stop immediately if:

- Dataset missing

- Annotation corruption

- Missing checkpoints

- CUDA unavailable

- Invalid configuration

- Model loading failure

- Evaluation failure

Every failure must generate a detailed error log.

---

# Logging Pipeline

Every stage must generate logs.

```text
logs/

dataset.log

validation.log

benchmark.log

training.log

evaluation.log

errors.log
```

---

# Generated Reports

The following reports must be automatically created.

```text
reports/

dataset_report.md

benchmark_report.md

evaluation_report.md

experiment_log.md

submission_summary.md
```

---

# Expected Folder Outputs

```text
results/

statistics/

graphs/

predictions/

weights/

visualizations/

reports/
```

---

# Pipeline Constraints

The execution order must never change.

Dataset Verification

↓

Annotation Validation

↓

Visualization

↓

Benchmark

↓

Fusion

↓

Evaluation

↓

Submission

Skipping stages is prohibited.

---

# Acceptance Criteria

The Pipeline Flow Document is complete when:

- Every execution stage is defined.

- Every module has clear inputs and outputs.

- Dependencies are documented.

- Failure conditions are documented.

- Logging requirements are defined.

- Report generation is specified.

- Pipeline execution order is fixed.

This document becomes the architectural reference for all future development.

---

# Document Status

**Status:** Approved for Development

**Version:** 1.0

**Next Document:** 04_EXPERIMENT_DESIGN.md