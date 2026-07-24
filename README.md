# FusionGuard AI

This project evaluates the **QFDet*** (Fusion) model on the VTUAV dataset. The workflow is divided into two main stages: Stage 1 (Dataset Analysis) and Stage 2 (Model Inference).

---

## 📊 Stage 1: Dataset Exploration & Analysis

This stage analyzes the VTUAV dataset, verifying image pairs, generating scale distribution statistics, and confirming annotation integrity.

**How to run Stage 1:**
Open a terminal in the `FusionGuard-AI` folder and run the Python analysis script:
```bash
python scripts/analyze_dataset.py
```

**Where to find the outputs:**
Once finished, the script generates statistical reports about your dataset:
- `reports/dataset_statistics.md` (Summary report)
- `reports/stats.json` (Raw statistics data)

---

## 🤖 Stage 2: Model Inference & Evaluation

This stage runs the actual AI model inference on the dataset using a PyTorch Docker container to evaluate pedestrian detection accuracy (mAP).

### Step 1: Start Docker Desktop
Make sure the **Docker Desktop** application is open and running on your computer.

### Step 2: Download the AI Model Weights
In your terminal, run this script to download the pre-trained model weights:
```bash
python scripts/download_weights.py
```

### Step 3: Run the Model (Evaluation)
There are two ways to run the evaluation depending on your preference:

**Option A: Build a Permanent Image (Recommended)**
Build a custom Docker image that permanently caches the AI libraries so you never have to wait for downloads again.
First, build the image (this takes ~15 minutes but you only do it once!):
```bash
docker build -t fusionguard .
```
Then, run it instantly:
```bash
docker run --rm --gpus all --ipc=host -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace -w /workspace fusionguard bash scripts/run_benchmark.sh
```

**Option B: Quick Run (Downloads libraries every time)**
If you just want to run it once without saving the environment, run this directly:
```bash
docker run --rm --gpus all --ipc=host -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace -w /workspace pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel bash scripts/run_benchmark.sh
```

### Step 4: View Your Results
Once the command finishes running, you can find the final accuracy metrics compared side-by-side in this file:
- `reports/comparison_report.md` 
(Note: The raw numerical output from the model script itself is saved to `reports/raw_metrics/fusion_eval.txt`).
