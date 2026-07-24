# 🚀 FusionGuard AI: Complete Execution & Output Guide

This document serves as the master guide for the hackathon judges (or anyone else) to run the FusionGuard AI pipeline end-to-end, from data exploration all the way to final automated evaluation.

---

## 🛠️ Prerequisites
Ensure that Docker is installed and running with GPU access. The entire project is containerized to avoid dependency conflicts.
- **Workspace Dir:** `C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI`
- **Docker Image:** `fusionguard` (must be built locally)

---

## 📊 Stage 1: Dataset Exploration & Validation

**Goal:** Verify the VTUAV subset integrity, check RGB-Thermal pairings, and validate JSON annotations.

### How to Run
Run the dataset analysis script locally:
```bash
python scripts/analyze_dataset.py
```

### Outputs Generated
- 📄 **Dataset Statistics Report:** [reports/dataset_statistics.md](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/reports/dataset_statistics.md)

---

## 🏗️ Stage 2: Unimodal Analysis & Baseline Setup

**Goal:** Set up the MMDetection environment and download the pre-trained weights to establish the baseline `0.320 mAP`.

### How to Run
```bash
# 1. Check local environment and requirements
python scripts/check_env.py

# 2. Download Baseline Weights
python scripts/download_weights.py

# 3. Build the Docker Container
docker build -t fusionguard -f Dockerfile .

# 4. Benchmark the Baseline Model using Docker (0.320 mAP)
docker run --rm --gpus all --ipc=host \
  -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace \
  -w /workspace fusionguard \
  bash -c "PYTHONPATH=/workspace/external/qfdet-baseline python external/qfdet-baseline/tools/test.py external/qfdet-baseline/qfdet_configs/qfdet_star_r50_fpn_1x_vtuav.py weights/epoch_11_qfdet_star_vtuav.pth --eval bbox"
```

### Outputs Generated
- 📦 **Baseline Weights:** `weights/epoch_11_qfdet_star_vtuav.pth`
- 📄 **Baseline Env Check:** [docs/STAGE2_COMPLETION_REPORT.md](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/docs/STAGE2_COMPLETION_REPORT.md)

---

## 🧠 Stage 3: Novel Fusion Strategy (CMAF)

**Goal:** Implement the Cross-Modal Attention Fusion (CMAF) architecture and fine-tune it to surpass the baseline without overfitting.

### How to Run
Because CMAF is built directly into the codebase, you run it by launching a fine-tuning job inside the Docker container:
```bash
docker run --rm --gpus all --ipc=host \
  -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace \
  -w /workspace fusionguard \
  bash -c "pip install yapf==0.40.1 && PYTHONPATH=/workspace/external/qfdet-baseline python external/qfdet-baseline/tools/train.py external/qfdet-baseline/qfdet_configs/qfdet_cmaf_finetune.py"
```

### Outputs Generated
- 💻 **Custom Source Code:** [external/qfdet-baseline/mmdet/models/detectors/cmaf.py](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/external/qfdet-baseline/mmdet/models/detectors/cmaf.py)
- ⚙️ **Experiment Config:** [external/qfdet-baseline/qfdet_configs/qfdet_cmaf_finetune.py](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/external/qfdet-baseline/qfdet_configs/qfdet_cmaf_finetune.py)
- 📦 **Fine-Tuned Weights:** `weights/fusion_cmaf_finetune/` *(Generated after training completes)*

---

## 📈 Stage 4: Performance Evaluation Framework

**Goal:** Automatically calculate all COCO metrics (mAP), extract dynamic hardware limits (FLOPs/FPS), and draw visualization boxes.

### How to Run
Run the master bash script to perform inference, followed by the report generator:

```bash
# 1. Run inference, dynamic PyTorch profiling, and OpenCV visualizer
docker run --rm --gpus all --ipc=host \
  -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace \
  -w /workspace fusionguard \
  bash scripts/evaluate_model.sh baseline external/qfdet-baseline/qfdet_configs/qfdet_star_r50_fpn_1x_vtuav.py weights/epoch_11_qfdet_star_vtuav.pth

# 2. Generate the final Markdown Comparison Report
docker run --rm --gpus all --ipc=host \
  -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace \
  -w /workspace fusionguard \
  python scripts/generate_reports.py
```

### Outputs Generated
- 🏆 **Unified Comparison Report:** [reports/evaluation/comparison_report.md](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/reports/evaluation/comparison_report.md)
- 📊 **Official COCO Deliverable:** [results/predictions/coco_format_baseline.bbox.json](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/results/predictions/coco_format_baseline.bbox.json)
- 🖼️ **RGB Bounding Box Images:** `results/visualizations/baseline/rgb/`
- 🖼️ **Thermal Bounding Box Images:** `results/visualizations/baseline/thermal/`
- 📈 **Dynamic Compute Profiling:** [results/metrics/baseline_compute.json](file:///c:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI/results/metrics/baseline_compute.json)
