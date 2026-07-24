# Stage 2 — Baseline Performance Benchmarking

**Project:** FusionGuard AI

**Hackathon:** Yugma TechFest 2.0 – MedhaDrishti AI Hackathon

**Stage:** 2

**Status:** 🔄 Ready to Start

**Priority:** Highest

**Estimated Duration:** 3–5 Hours

---

# Objective

The primary objective of Stage 2 is to establish a reliable and reproducible benchmark using the organizer-provided pretrained QFDet model.

No architectural modifications or custom fusion modules shall be implemented during this stage.

This stage establishes the reference performance that every future experiment must surpass.

---

# Purpose

Stage 2 answers three fundamental questions:

1. How well does RGB perform independently?
2. How well does Thermal perform independently?
3. How much improvement does the baseline RGB-Thermal fusion provide?

Only after answering these questions should Stage 3 begin.

---

# Inputs

## Dataset

datasets/VTUAV_subset/

Status

✅ Verified during Stage 1

---

## Baseline Repository

third_party/qfdet-baseline/

Status

Pending Integration

---

## Stage 1 Repository

third_party/stage1-analysis/

Status

Completed

---

## Pretrained Model

weights/

Status

Organizer Provided

---

# Expected Outputs

```text
reports/

stage2/

baseline_report.md

rgb_report.md

thermal_report.md

comparison_report.md

metrics_summary.md
```

---

Generated Predictions

```text
results/

predictions/

rgb/

thermal/

fusion/
```

---

Evaluation Logs

```text
logs/

stage2/

rgb.log

thermal.log

fusion.log
```

---

# Stage Workflow

```text
Load Dataset

↓

Load Pretrained QFDet

↓

Verify Model

↓

RGB-only Evaluation

↓

Thermal-only Evaluation

↓

Baseline Fusion Evaluation

↓

Metric Collection

↓

Performance Analysis

↓

Comparison Report

↓

Stage 2 Complete
```

---

# Quality Gates Before Execution

Before running any benchmark, verify:

- Dataset accessible
- Stage 1 completed
- QFDet repository available
- Pretrained weights available
- CUDA detected
- MMDetection installed
- Evaluation scripts working

If any check fails, benchmarking must stop.

---

# Task 1 — Environment Verification

Validate:

- Python environment
- CUDA
- GPU
- MMDetection
- MMCV
- MMEngine
- PyTorch
- OpenCV

Generate

```text
reports/environment_check.md
```

---

# Task 2 — Repository Validation

Verify

- Baseline repository cloned
- Dependencies installed
- Configurations available
- Evaluation scripts executable

Generate

```text
reports/repository_validation.md
```

---

# Task 3 — Model Validation

Verify

- Checkpoint loads successfully
- Architecture initializes
- No missing layers
- No missing weights

Run one inference on a sample image.

Generate

```text
reports/model_validation.md
```

---

# Task 4 — RGB-only Benchmark

Disable Thermal input.

Evaluate only RGB modality.

Generate:

- mAP
- mAP50
- mAP75
- mAPS
- mAPM
- mAPL
- Precision
- Recall
- FPS
- Inference Time

Store predictions in:

```text
results/predictions/rgb/
```

---

# Task 5 — Thermal-only Benchmark

Disable RGB input.

Evaluate only Thermal modality.

Generate identical metrics.

Store predictions in:

```text
results/predictions/thermal/
```

---

# Task 6 — Baseline Fusion Benchmark

Evaluate the organizer-provided QFDet model without modifications.

Generate:

- COCO metrics
- FPS
- Latency
- FLOPs
- Parameters
- Model Size

Store predictions in:

```text
results/predictions/fusion/
```

---

# Task 7 — Computational Analysis

Measure

- FPS
- GPU Memory
- CPU Usage
- Inference Time
- Model Size
- FLOPs
- Parameters

Generate

```text
reports/computation_report.md
```

---

# Task 8 — Comparative Analysis

Compare

RGB

vs

Thermal

vs

Baseline Fusion

Comparison Criteria

- Detection Accuracy
- Small Pedestrian Detection
- Night Performance
- Day Performance
- Recall
- Precision
- Speed
- Resource Usage

Generate:

```text
reports/comparison_report.md
```

---

# Task 9 — Failure Case Analysis

Document

- False Positives
- False Negatives
- Missed Small Pedestrians
- Occluded Pedestrians
- Low Illumination Failures
- Thermal Failure Cases

Generate visual examples.

---

# Deliverables

The following files must exist before Stage 2 is considered complete.

```text
reports/

baseline_report.md

rgb_report.md

thermal_report.md

comparison_report.md

metrics_summary.md

environment_check.md

model_validation.md

repository_validation.md

computation_report.md
```

---

# Evaluation Metrics

## Detection Metrics

- mAP
- mAP50
- mAP75
- mAPS
- mAPM
- mAPL
- Precision
- Recall

---

## Computational Metrics

- FPS
- Latency
- FLOPs
- Parameters
- GPU Memory
- Model Size

---

# Quality Gates

Stage 2 passes only if:

- Baseline model loads successfully.
- RGB benchmark completed.
- Thermal benchmark completed.
- Fusion benchmark completed.
- Reports generated.
- Metrics reproducible.
- Prediction files saved.
- Logs generated.

---

# Team Responsibilities

## Member 1

Environment Setup

Dependency Validation

GPU Verification

---

## Member 2

RGB Benchmark

Thermal Benchmark

---

## Member 3

Fusion Benchmark

Performance Measurement

---

## Member 4

Report Generation

Comparison

Documentation

---

# AI Coding Agent Instructions

Antigravity must:

- Never modify the baseline architecture during Stage 2.
- Never retrain the model.
- Never overwrite organizer weights.
- Run RGB, Thermal, and Fusion benchmarks independently.
- Store predictions separately.
- Save all logs.
- Generate markdown reports automatically.
- Read all paths from configuration files.
- Continue execution only if all quality gates pass.

---

# Definition of Done

Stage 2 is complete when:

- RGB benchmark completed.
- Thermal benchmark completed.
- Fusion benchmark completed.
- Metrics verified.
- Comparison report generated.
- Failure cases documented.
- Git commit created.

---

# Git Commit

```bash
git add .
git commit -m "Complete Stage 2 - Baseline Performance Benchmarking"
```

---

# Exit Criteria

Proceed to **Stage 3 — RGB-Thermal Fusion Strategy Development** only if:

- Stage 1 is validated.
- Stage 2 metrics are reproducible.
- Baseline repository is fully understood.
- QFDet architecture has been reviewed.
- Benchmark reports have been approved.

No architectural modifications are permitted before these conditions are satisfied.

---

# Document Status

**Status:** Approved for Execution

**Version:** 1.0

**Next Stage:** Stage 3 – RGB-Thermal Fusion Strategy Development