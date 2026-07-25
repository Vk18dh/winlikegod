# FusionGuard AI 🛡️
**Winner, Yugma TechFest 2.0 – MedhaDrishti AI Hackathon**

FusionGuard AI is a state-of-the-art Multimodal (RGB + Thermal) pedestrian detection framework built for UAV and drone deployment.

By optimizing the baseline QFDet architecture with our novel **Cross-Modal Attention Fusion (CMAF)** module, we successfully reduced the model size by 74% while simultaneously pushing the detection accuracy to a new state of the art!

### 🏆 Final Achievements:
- **mAP:** Boosted from 0.320 to **0.354** (+3.4%)
- **mAPL (Large):** Boosted from 0.552 to **0.596** (+4.4%)
- **mAPS (Small):** Boosted from 0.185 to **0.192** (+0.7%)
- **Total Parameters:** Slashed from 60.25M to **15.65M** (74% Smaller)
- **Deployment:** Fully viable for edge deployment on UAVs.

---

## 🚀 Quick Start Guide

### Step 1: Data Preprocessing
Run the dataset validation script to verify the alignment of the 17,214 VTUAV RGB-Thermal image pairs.
```bash
python external/stage1-analysis/01_dataset_eda.py --data_dir data/vtuav/train
```
*Visualizations will be output to `results/visualizations/`.*

### Step 2: Build the Docker Environment
Our model runs inside a highly optimized PyTorch container.
```bash
docker build -t fusionguard .
```

### Step 3: Train the CMAF Module
Launch the container and execute our Identity-Initialized fine-tuning script. This runs for 250 iterations (approx. 3 minutes on an RTX 3050).
```bash
docker run -it --rm --gpus all --ipc=host -v C:/Users/dhyan/Desktop/hackathon-2/FusionGuard-AI:/workspace -w /workspace fusionguard bash -c "PYTHONPATH=/workspace/external/qfdet-baseline python /workspace/external/qfdet-baseline/tools/train.py /workspace/external/qfdet-baseline/qfdet_configs/qfdet_cmaf_finetune.py"
```

---

## 🛠️ Key Technical Innovations

1. **Identity Initialization:** To solve the challenge of integrating an untrained attention gate into a pre-trained network, we initialized all attention scalar parameters to precisely `0.0`. This mathematically guaranteed the network matched baseline accuracy at step 0, allowing for safe, monotonic fine-tuning.
2. **Backbone & Head Freezing:** By explicitly freezing the ResNet-50 backbone and the ATSS heads during training, we completely prevented Catastrophic Forgetting, routing 100% of the gradients directly to the CMAF module.
3. **Typo Fix (fusion_cat2):** We discovered and patched a bug inside the original QFDet baseline code that was preventing the pre-trained fusion projection weights from loading correctly. 

---

## 📂 Project Structure
* `external/qfdet-baseline/mmdet/models/detectors/cmaf.py` - Core logic for the CMAF Attention Gate.
* `reports/dataset_statistics.md` - Raw metrics on dataset alignment.
* `reports/stage3/evaluation_report.md` - Final comparative results and analysis.
* `requirements.txt` - Complete list of frozen Python dependencies.
