# Experiment Registry

**Project:** FusionGuard AI

**Hackathon:** Yugma TechFest 2.0 – MedhaDrishti AI Hackathon

**Purpose:** Central Experiment Dashboard

**Document Version:** 1.0

---

# Overview

The Experiment Registry is the central control document for every experiment performed during the FusionGuard AI project.

Unlike `EXPERIMENT_LOG.md`, which contains detailed observations, this registry provides a high-level overview of every experiment, its current status, artifacts, metrics, and final decision.

This document should always reflect the current state of the project.

---

# Project Progress

| Stage | Status | Progress |
|---------|---------|-----------|
| Planning | ✅ Complete | 100% |
| Stage 1 | ✅ Complete | 100% |
| Stage 2 | 🟡 In Progress | 0% |
| Stage 3 | ⚪ Pending | 0% |
| Stage 4 | ⚪ Pending | 0% |

---

# Experiment Status Legend

| Icon | Meaning |
|-------|----------|
| 🔵 | Planned |
| 🟡 | Running |
| 🟢 | Completed |
| 🔴 | Failed |
| ⚪ | Not Started |
| ⭐ | Selected for Final Model |

---

# Master Experiment Registry

| ID | Experiment | Stage | Owner | Priority | Status |
|----|------------|--------|---------|----------|--------|
| EXP-001 | Dataset Validation | 1 | Team | Critical | 🟢 |
| EXP-002 | RGB Benchmark | 2 | Team | Critical | 🔵 |
| EXP-003 | Thermal Benchmark | 2 | Team | Critical | 🔵 |
| EXP-004 | Baseline QFDet Benchmark | 2 | Team | Critical | 🔵 |
| EXP-005 | Baseline Comparative Analysis | 2 | Team | High | 🔵 |
| EXP-006 | Fusion Strategy Review | 3 | Team | Critical | ⚪ |
| EXP-007 | Adaptive Fusion V1 | 3 | Team | High | ⚪ |
| EXP-008 | Cross-Modal Attention | 3 | Team | High | ⚪ |
| EXP-009 | Multi-Scale Fusion | 3 | Team | High | ⚪ |
| EXP-010 | Tiny Pedestrian Enhancement | 3 | Team | Critical | ⚪ |
| EXP-011 | Lightweight Fusion Optimization | 3 | Team | Medium | ⚪ |
| EXP-012 | Final Model Evaluation | 4 | Team | Critical | ⚪ |

---

# Experiment Dependencies

```text
EXP-001
      │
      ▼
EXP-002
      │
      ▼
EXP-003
      │
      ▼
EXP-004
      │
      ▼
EXP-005
      │
      ▼
EXP-006
      │
      ▼
EXP-007
      │
      ▼
EXP-008
      │
      ▼
EXP-009
      │
      ▼
EXP-010
      │
      ▼
EXP-011
      │
      ▼
EXP-012
```

No experiment may bypass dependency order unless explicitly approved.

---

# Experiment Tracker

---

## EXP-001

### Objective

Validate the dataset.

Status

🟢 Completed

Artifacts

- Dataset Statistics
- Alignment Report
- Visualization
- Validation Report

Decision

Accepted

---

## EXP-002

### Objective

Benchmark RGB-only performance.

Current Status

🔵 Planned

Expected Deliverables

- RGB Predictions
- COCO Metrics
- Benchmark Report

Blocking Issues

None

---

## EXP-003

### Objective

Benchmark Thermal-only performance.

Status

🔵 Planned

Expected Deliverables

- Thermal Predictions
- Metrics
- Report

---

## EXP-004

### Objective

Reproduce organizer baseline.

Status

🔵 Planned

Expected Deliverables

- Baseline Metrics
- FLOPs
- FPS
- Comparison Tables

---

## EXP-005

### Objective

Compare RGB vs Thermal vs Fusion.

Status

🔵 Planned

Expected Deliverables

- Comparison Charts
- Failure Analysis
- Observations

---

## EXP-006

### Objective

Review fusion strategy candidates.

Possible Candidates

- Adaptive Fusion
- Cross-Modal Attention
- Dynamic Feature Weighting
- Multi-Scale Fusion
- Lightweight Fusion

Decision

Pending

---

## EXP-007

Adaptive Fusion

Status

⚪

---

## EXP-008

Cross-Modal Attention

Status

⚪

---

## EXP-009

Multi-Scale Fusion

Status

⚪

---

## EXP-010

Tiny Pedestrian Enhancement

Status

⚪

Reason

This experiment directly targets the hackathon's emphasis on improving small and tiny pedestrian detection.

---

## EXP-011

Lightweight Optimization

Status

⚪

Goal

Reduce computational overhead while preserving accuracy.

---

## EXP-012

Final Evaluation

Status

⚪

Goal

Generate final benchmark and submission metrics.

---

# Selected Improvements

This section is updated throughout Stage 3.

| Improvement | Selected |
|--------------|-----------|
| Adaptive Fusion | ☐ |
| Cross-Modal Attention | ☐ |
| Dynamic Weighting | ☐ |
| Multi-Scale Fusion | ☐ |
| Tiny Object Enhancement | ☐ |
| Lightweight Fusion | ☐ |

---

# Benchmark Dashboard

| Model | mAP | mAPS | FPS | FLOPs | Status |
|--------|-----|------|------|--------|---------|
| RGB | — | — | — | — | Pending |
| Thermal | — | — | — | — | Pending |
| QFDet | — | — | — | — | Pending |
| Final Model | — | — | — | — | Pending |

---

# Submission Checklist

| Item | Status |
|------|---------|
| Stage 1 | ✅ |
| Stage 2 | ☐ |
| Stage 3 | ☐ |
| Stage 4 | ☐ |
| Source Code | ☐ |
| Model Weights | ☐ |
| Technical Report | ☐ |
| Presentation | ☐ |
| GitHub Repository | ☐ |

---

# Risks

| Risk | Severity | Status |
|------|----------|--------|
| Baseline cannot be reproduced | High | Open |
| No measurable improvement | High | Open |
| GPU memory limitation | Medium | Open |
| Overfitting | Medium | Open |
| Increased latency | Medium | Open |

---

# Winning Criteria

To maximize competitiveness, the project should aim to:

- Reproduce the baseline reliably before making changes.
- Demonstrate measurable improvements over the baseline.
- Improve performance on small and tiny pedestrians.
- Keep computational overhead reasonable.
- Maintain clean documentation and reproducible experiments.
- Present clear evidence that each architectural change is justified by experimental results.

These goals align closely with the hackathon evaluation criteria.

---

# Next Milestone

Complete Stage 2 benchmarking and establish a trustworthy baseline before beginning any architectural modifications.

---

# Document Status

Version: 1.0

Status: Active

Updated After Every Experiment