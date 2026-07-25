# Failure Analysis

## False Positives (Ghost Detections)
The model occasionally predicts bounding boxes on objects that emit thermal signatures similar to pedestrians, such as heating vents, bright reflections, or animals. While the RGB stream helps suppress some of these, heavily occluded or low-light scenarios sometimes cause the thermal signature to dominate the CMAF attention gate, leading to a False Positive.

## False Negatives (Missed Detections)
Small or heavily occluded pedestrians at long ranges occasionally go undetected. If the ambient temperature is close to the human body temperature and the RGB stream is poorly lit, the dual-stream feature maps lack sufficient contrast for the ATSS heads to generate a high-confidence anchor.

## Edge Cases
- **Tiny Pedestrians**: The network performs moderately well on small targets (mAPS = 0.192), but extreme scale variances still pose challenges.
- **Occlusion**: The model is robust to partial occlusion due to thermal penetration, but full physical occlusion behind solid walls naturally fails.
