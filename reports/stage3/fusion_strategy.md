# Stage 3 — Fusion Strategy Report

**Project:** FusionGuard AI
**Stage:** 3
**Date:** 2026-07-25

---

## Baseline Analysis

From Stage 2 benchmark (`comparison_report.md`), the critical weakness identified is:

| Metric | Baseline QFDet* | Interpretation |
|--------|-----------------|----------------|
| mAP    | 0.320           | Good overall |
| mAP50  | 0.735           | Strong overlap threshold |
| **mAPS** | **0.185**   | **Critical gap — tiny pedestrians** |
| mAPM   | 0.317           | Moderate |
| mAPL   | 0.552           | Strong for large objects |

**Root Cause:** The baseline `qce_fusion()` applies quality-aware feature scaling, but the RGB and Thermal streams have **no direct cross-modal interaction**. Each modality's channels are scaled independently. The model cannot learn, for example, that "channel 47 of Thermal is highly correlated with channel 12 of RGB when illumination is low."

---

## Selected Strategy: CMAF (Cross-Modal Attention Fusion)

### Motivation
Channel-wise cross-modal attention allows each modality to act as a "filter" for the other. This produces attended features that are inherently more complementary, improving information density per channel — especially useful for tiny pedestrians that occupy very few feature map pixels.

### Why NOT other approaches?
| Strategy | Rejected Reason |
|----------|-----------------|
| Multi-scale aggregation | High FLOP cost, marginal gain |
| Transformer attention | Too memory-heavy for our GPU constraints |
| Separate FPN necks | Doubled parameters, complex training |
| Spatial attention only | Doesn't capture inter-modality dependencies |

### Module Design

**1. ChannelAttentionGate**
- Squeeze-and-Excitation style gate
- Query modality → Global Avg Pool → 2-layer MLP → Sigmoid weights
- Weights applied multiplicatively to the key modality
- Parameters per gate: `2 × (C × C/reduction)` = 2 × (256 × 64) = 32,768

**2. SmallObjectContextBlock (P2 only)**
- 3 parallel dilated convolutions (dilation 1, 3, 5)
- Aggregated via 1x1 conv + BN + ReLU
- Residual connection to preserve original features
- Applied ONLY at P2 (stride=4, highest resolution) to target tiny objects
- Does NOT increase FLOPs at other FPN levels

### Parameter Budget
| Component | Parameters |
|-----------|------------|
| rgb_gates (5 levels) | ~163K |
| tir_gates (5 levels) | ~163K |
| conv1x1s (5 levels) | ~328K |
| SmallObjectContextBlock | ~99K |
| **Total CMAF overhead** | **~753K** |
| Baseline params | 33.4M |
| **New total** | **~34.2M** |

This represents a **+2.3% parameter increase** — negligible.

---

## Expected Improvement

Based on cross-modal attention literature and our dataset analysis:
- **mAPS:** Expected +2–5% (targeted by SmallObjectContextBlock)
- **mAP overall:** Expected +1–3%
- **FPS:** Expected drop of 1–2 FPS (negligible)
