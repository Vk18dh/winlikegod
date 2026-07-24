# Technical Requirements Document (TRD)

**Project Name:** FusionGuard AI

**Version:** 1.0

**Document Owner:** Team <Team Name>

**Last Updated:** <Date>

---

# Purpose

This document defines the complete technical architecture, development stack, coding standards, dependencies, infrastructure, and engineering constraints for the FusionGuard AI project.

This document serves as the **single technical source of truth** for all AI coding agents, developers, and contributors.

No implementation should violate the specifications defined in this document.

---

# Project Overview

FusionGuard AI is an advanced RGB-Thermal pedestrian detection system developed for the **Yugma TechFest 2.0 - MedhaDrishti National-Level AI Hackathon**.

The project extends the baseline **Quality-aware RGB-Thermal Fusion Detector (QFDet)** by introducing novel multimodal fusion techniques specifically optimized for detecting small and tiny pedestrians while maintaining computational efficiency.

---

# Technology Stack

## Programming Language

- Python 3.10+

Reason

- Native support for PyTorch
- MMDetection compatibility
- Extensive Computer Vision ecosystem

---

# Deep Learning Framework

**Primary**

- PyTorch

Reason

- Native compatibility with MMDetection
- GPU acceleration
- Dynamic computation graph
- Industry standard for Computer Vision research

---

# Detection Framework

- MMDetection
- MMEngine
- MMCV

Purpose

- Model training
- Evaluation
- Configuration management
- Dataset pipeline
- Checkpoint handling

---

# Baseline Model

Model Name

Quality-aware RGB-Thermal Fusion Detector (QFDet)

Repository

Baseline implementation provided by the hackathon organizers.

Restrictions

- Training from scratch is prohibited.
- Pretrained weights must be used.
- Architecture modifications are allowed.
- External datasets are prohibited.

---

# Dataset

Dataset Name

VTUAV-det (Curated Subset)

Contains

- RGB Images
- Thermal Images
- Bounding Box Annotations
- Train Split
- Validation Split
- Test Split

Supported Image Formats

- JPG
- PNG

Annotation Format

- COCO-compatible annotations (or organizer-provided format)

Supported Classes

- Pedestrian (Only)

---

# Computer Vision Libraries

Required

- OpenCV
- Pillow
- NumPy
- TorchVision

Purpose

- Image loading
- Image preprocessing
- Visualization
- Data augmentation
- Utility operations

---

# Scientific Computing Libraries

Required

- NumPy
- SciPy
- Pandas

Purpose

- Numerical computation
- Statistical analysis
- Dataset reporting
- Experiment analysis

---

# Visualization Libraries

Required

- Matplotlib
- OpenCV

Purpose

- Bounding box visualization
- RGB-Thermal comparison
- Dataset statistics
- Performance graphs

---

# Evaluation Framework

Evaluation Standard

COCO Object Detection Metrics

Metrics

- mAP
- mAP50
- mAP75
- mAPS
- mAPM
- mAPL

Additional Metrics

- Precision
- Recall
- FPS
- Inference Time
- FLOPs
- Number of Parameters
- Model Size

---

# Development Environment

Operating System

Preferred

- Ubuntu 22.04 LTS

Supported

- Windows 11
- WSL2
- Linux

Python Environment

Recommended

Conda

Alternative

Python Virtual Environment

IDE

Preferred

- VS Code

AI Coding Agent

Primary

- Antigravity

Version Control

- Git
- GitHub

---

# GPU Requirements

Minimum

- NVIDIA RTX 3050
- 8GB VRAM

Recommended

- RTX 4060
- RTX 4070
- RTX 4080
- RTX 4090

CUDA

- CUDA 12+

Acceleration

- cuDNN

Fallback

- CPU Execution (Debugging Only)

---

# Project Folder Structure

```text
FusionGuard-AI/

configs/
docs/
datasets/
models/
weights/
scripts/
analysis/
fusion/
evaluation/
visualization/
results/
experiments/
logs/
tests/
notebooks/
utils/

README.md
requirements.txt
environment.yml
.gitignore
LICENSE
```

---

# Configuration Management

All configurable values must be stored outside source code.

Examples

- Dataset paths
- Weight paths
- Hyperparameters
- GPU selection
- Batch size
- Learning rate

Configuration Files

```text
configs/

dataset.py
model.py
training.py
evaluation.py
fusion.py
```

---

# Coding Standards

All source code must follow:

- PEP 8
- Type hints
- Modular architecture
- SOLID principles where applicable
- Clear documentation
- Descriptive variable names
- No hardcoded paths
- No duplicate code

---

# Logging Standards

Every major module must generate logs.

Required Logging

- Dataset loading
- Annotation validation
- Training
- Evaluation
- Inference
- Errors
- Warnings
- GPU utilization

Log Directory

```text
logs/
```

---

# Error Handling

The project must gracefully handle:

- Missing images
- Corrupted annotations
- Invalid checkpoints
- CUDA memory overflow
- Missing dependencies
- Invalid configuration
- Empty datasets

The system should never terminate without producing a meaningful error message.

---

# Testing Strategy

Every major module must have automated tests.

Required Tests

- Dataset Loader
- Annotation Parser
- Image Pair Verification
- RGB Loader
- Thermal Loader
- Model Loader
- Inference Pipeline
- Evaluation Pipeline
- Visualization Pipeline

Testing Framework

- pytest

---

# Documentation Standards

Every module must include:

- Purpose
- Inputs
- Outputs
- Dependencies
- Usage Example

Documentation Format

Markdown

Docstrings

Google Style

---

# Environment Variables

Example

```text
DATASET_ROOT=

TRAIN_PATH=

VAL_PATH=

TEST_PATH=

CHECKPOINT_PATH=

OUTPUT_DIR=

LOG_DIR=

CUDA_VISIBLE_DEVICES=

PYTHONPATH=
```

No sensitive information shall be stored inside source code.

---

# Performance Constraints

The final solution should:

- Improve baseline detection accuracy.
- Maintain reasonable inference speed.
- Minimize additional computational overhead.
- Prioritize small pedestrian detection.
- Support reproducible experiments.

---

# Security Considerations

The project must:

- Never modify original datasets.
- Preserve pretrained weights.
- Keep experiment outputs isolated.
- Validate external inputs.
- Prevent accidental file overwrites.

---

# Engineering Constraints

The implementation must comply with hackathon rules.

Mandatory Constraints

- Use only the provided VTUAV-det subset.
- Use pretrained QFDet weights.
- Do not train from scratch.
- External datasets are prohibited.
- Only the Pedestrian class is permitted.
- Evaluation must use organizer-provided protocols.

---

# Third-Party Dependencies

Core

- PyTorch
- MMDetection
- MMCV
- MMEngine
- OpenCV
- NumPy
- Pandas
- TorchVision
- Pillow
- Matplotlib
- SciPy
- pycocotools
- tqdm
- rich
- pytest

Optional

- TensorBoard
- Weights & Biases
- ONNX
- TensorRT

---

# Deployment Strategy

Development

Local GPU

Training

Local GPU / Cloud GPU

Evaluation

Local GPU

Submission

GitHub Repository

Final Deliverables

- Source Code
- Trained Weights
- Evaluation Results
- Technical Report
- Presentation

---

# Technical Risks

- GPU memory limitations
- Dataset imbalance
- Thermal image quality
- Small object detection
- Longer inference time
- Overfitting during fine-tuning

Mitigation strategies shall be documented during development.

---

# Acceptance Criteria

This document is considered complete when:

- Technology stack is finalized.
- Development environment is fixed.
- Folder structure is finalized.
- Coding standards are defined.
- Dependencies are finalized.
- Performance constraints are documented.
- Engineering constraints are documented.
- The document becomes the technical reference for all future development.

---

# Document Status

**Status:** Approved for Development

**Version:** 1.0

**Next Document:** 03_PIPELINE_FLOW.md