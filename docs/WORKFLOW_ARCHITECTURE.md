# Structural & Architectural Workflow

This document outlines the technical architecture and end-to-end workflow of the **FusionGuard AI** project. The system is designed to handle multimodal data ingestion, isolated MLOps infrastructure, and heavy neural network inference.

---

## 1. System Architecture Overview

Our architecture is strictly decoupled into three main pipelines to ensure stability and reproducibility:
1. **Data Engineering Pipeline (Local):** Lightweight mathematical analysis and validation of the raw dataset.
2. **MLOps Infrastructure Pipeline (Containerized):** Heavy C++ and CUDA dependency management isolated via Docker.
3. **Inference Pipeline (GPU Execution):** The execution of the dual-stream neural network on the drone footage.

---

## 2. The Three-Pipeline Workflow

### Pipeline 1: Data Engineering & Validation (Stage 1)
**Execution:** Local Python (`scripts/analyze_dataset.py`)
**Purpose:** Ensure data integrity and generate mathematical priors before training or inference.
* **Input:** Raw VTUAV Dataset (RGB `VTUAV_co`, Thermal `VTUAV_ir`, and COCO JSON annotations).
* **Process 1 (Hardware Calibration Check):** Extracts a random sample of 20 image pairs to visually verify the drone's physical camera alignment (`alignment_grid.png`).
* **Process 2 (K-Means Clustering):** Parses all bounding boxes and runs a K-Means algorithm (K=9) to calculate the optimal anchor box templates for tiny drone-captured pedestrians.
* **Output:** `dataset_statistics.md` and `anchor_analysis.json`.

### Pipeline 2: MLOps & Infrastructure Setup (Stage 2 Prep)
**Execution:** Docker (`Dockerfile`, `scripts/download_weights.py`)
**Purpose:** Create a crash-proof, reproducible environment for the AI.
* **Weights Ingestion:** Securely downloads the 131MB PyTorch `.pth` checkpoint from the cloud into the `/weights` directory.
* **Containerization:** Builds a custom Docker image based on `pytorch:1.13.1-cuda11.6`. It installs system binaries (`libgl1`), updates pip, and compiles fragile computer vision libraries (`mmcv-full`) safely on the hard drive.
* **Output:** The `fusionguard` permanent Docker Image.

### Pipeline 3: Dual-Stream AI Inference (Stage 2 Execution)
**Execution:** Docker Container GPU (`scripts/run_benchmark.sh`)
**Purpose:** Feed the data through the neural network to output detection metrics.
* **Orchestration:** The bash script mounts the local `/workspace` into the container, passes GPU access (`--gpus all`), and mitigates memory crashes (`--ipc=host`).
* **Execution:** Triggers the MMDetection framework (`tools/test.py`) using the `qfdet_star_r50_fpn_1x_vtuav.py` configuration.
* **Output:** `raw_metrics/fusion_eval.txt` (yielding `0.320 mAP`).

---

## 3. Core AI Architecture: QFDet* (Quality-Aware Fusion)

When the Inference Pipeline runs, the data passes through the **QFDet*** Neural Network architecture:

1. **Dual-Stream Input:** The network takes two simultaneous inputs (1 RGB image, 1 Thermal IR image).
2. **Feature Extraction (Backbone):** Both images pass through parallel **ResNet-50** networks to extract basic features (edges, shapes, thermal signatures).
3. **Multi-Scale Feature Pyramid (Neck):** The features are passed into an **FPN (Feature Pyramid Network)** to detect objects at varying scales (crucial for tiny pedestrians).
4. **Quality-Aware Feature Fusion (The Core Innovation):** 
   - Instead of blindly combining the RGB and Thermal data, the network calculates an "Illumination Quality Score." 
   - If the image is pitch black (night), it heavily weights the Thermal stream. If the thermal contrast is washed out (hot summer day), it heavily weights the RGB stream.
5. **Detection Head:** The dynamically fused features are fed into the final detection head, which outputs the bounding box coordinates and confidence scores for the pedestrians.

---

## 4. Tech Stack
* **Languages:** Python (Data/AI), Bash (Automation)
* **AI Frameworks:** PyTorch, MMDetection, MMCV
* **Infrastructure:** Docker, NVIDIA CUDA
* **Data Processing:** OpenCV (`cv2`), Numpy, Scikit-Learn (K-Means)
