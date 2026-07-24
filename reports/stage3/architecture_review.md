# Stage 3 — Architecture Review

**Project:** FusionGuard AI
**Stage:** 3

---

## Full System Architecture

```text
┌───────────────────────────────────────────────────────────────────┐
│                    FusionGuard AI — Stage 3                       │
│                  RGB–Thermal Pedestrian Detector                   │
└───────────────────────────────────────────────────────────────────┘

Input: Paired RGB Image + Thermal IR Image (640×512)
        │                    │
        ▼                    ▼
┌─────────────┐      ┌─────────────┐
│  ResNet-50  │      │  ResNet-50  │
│  (RGB)      │      │  (Thermal)  │
│  backbone   │      │  backbone   │
└──────┬──────┘      └──────┬──────┘
       │                    │
   (P2–P5 features)     (P2–P5 features)
       │                    │
       ▼                    ▼
┌─────────────┐      ┌─────────────┐
│    FPN      │      │    FPN      │
│  (RGB neck) │      │ (TIR neck)  │
└──────┬──────┘      └──────┬──────┘
       │                    │
       └────────┬───────────┘
                │
                ▼
┌───────────────────────────────┐
│  QFDetPreHead (Quality Pred.) │
│  Computes quality score per   │
│  modality per FPN level       │
└──────────────┬────────────────┘
               │ quality_t, quality_v
               ▼
┌───────────────────────────────┐
│    Quality-Aware Scaling       │
│  x_t = (1 + quality_t) * x_t  │
│  x_v = (1 + quality_v) * x_v  │
└──────────────┬────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────┐
│         CMAF: Cross-Modal Attention Fusion (NEW)         │
│                                                          │
│   x_v ──→ TIR gates RGB ──→ x_v_attended ──┐           │
│                                              ├─ Concat   │
│   x_t ──→ RGB gates TIR ──→ x_t_attended ──┘   +Conv1x1│
│                                              │           │
│                    [At P2 only]              ▼           │
│              SmallObjectContextBlock  (fused features)  │
│          (dilated conv 1,3,5 + residual)               │
└──────────────────────────────┬───────────────────────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │     ATSSQHead           │
                 │  (Detection Head)       │
                 │  FocalLoss + GIoU       │
                 └─────────────┬───────────┘
                               │
                               ▼
                    Pedestrian Detections
                  (Bounding boxes + scores)
```

---

## CMAF Module Internal Architecture

```text
For each FPN level i ∈ {0,1,2,3,4}:

rgb_feat[i]                          tir_feat[i]
    │                                    │
    ├──→ GlobalAvgPool ──→ MLP ──────────┤
    │    (queries TIR to weight RGB)     │
    │                                    │
    │    ┌──────────────────────────┐    │
    └────┤   ChannelAttentionGate   ├────┘
         │  (TIR gates RGB)         │
         └──────────┬───────────────┘
                    │
             rgb_attended[i]

    │                                    │
    ├──────────────────────────────┐     │
    │  ChannelAttentionGate        │     │
    │  (RGB gates TIR)             │     │
    └──→ GlobalAvgPool ──→ MLP ───┘     │
                    │                    │
             tir_attended[i]             │

    rgb_attended[i] + tir_attended[i]
               │
               ▼
          Concat(C + C = 2C)
               │
            Conv1x1 (2C → C)
               │
        [If i == 0 (P2):]
               │
    SmallObjectContextBlock
    ┌────────────────────────────────┐
    │  dilated_conv(d=1) ─┐         │
    │  dilated_conv(d=3) ─┼─ Concat │
    │  dilated_conv(d=5) ─┘   +Conv │
    │                        + Res. │
    └────────────────────────────────┘
               │
           fused[i]
```

---

## Files Modified

| File | Type | Change |
|------|------|--------|
| `mmdet/models/detectors/cmaf.py` | NEW | CMAF module implementation |
| `mmdet/models/detectors/qfdet.py` | MODIFIED | Added `fusion_type` parameter |
| `qfdet_configs/qfdet_cmaf_r50_fpn_1x_vtuav.py` | NEW | CMAF experiment config |
| `scripts/run_benchmark.sh` | MODIFIED | Added CMAF evaluation block |
| `reports/stage3/*.md` | NEW | All Stage 3 reports |

---

## Backward Compatibility

The baseline config `qfdet_star_r50_fpn_1x_vtuav.py` is **not modified**.
Running the original Docker command will still produce identical baseline results.
CMAF is activated only when `fusion_type='cmaf'` is set in the model config.
