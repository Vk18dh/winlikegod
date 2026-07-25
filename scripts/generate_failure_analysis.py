import json
import pickle
import os
import cv2
import numpy as np

def compute_iou(box1, box2):
    # box: [x1, y1, x2, y2]
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    inter_area = max(0, x2 - x1) * max(0, y2 - y1)
    if inter_area == 0:
        return 0
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    return inter_area / float(box1_area + box2_area - inter_area)

def analyze_failures():
    anno_path = '/workspace/datasets/VTUAV_subset/VTUAV_subset/annotations/test.json'
    pred_path = '/workspace/results/predictions/cmaf.pkl'
    out_dir = '/workspace/results/visualizations/failures'
    os.makedirs(out_dir, exist_ok=True)
    
    with open(anno_path, 'r') as f:
        coco = json.load(f)
    with open(pred_path, 'rb') as f:
        preds = pickle.load(f)
        
    img_list = coco['images']
    annos = coco['annotations']
    
    # Map image id to annotations
    img_to_anns = {img['id']: [] for img in img_list}
    for ann in annos:
        img_to_anns[ann['image_id']].append(ann)
        
    fn_count = 0
    fp_count = 0
    
    for i, img_info in enumerate(img_list):
        if i >= len(preds): break
        if fn_count >= 5 and fp_count >= 5: break
            
        img_preds = preds[i][0] # class 0 (pedestrian)
        gt_anns = img_to_anns[img_info['id']]
        
        # Format gt boxes
        gt_boxes = []
        for ann in gt_anns:
            x, y, w, h = ann['bbox']
            gt_boxes.append([x, y, x+w, y+h])
            
        # Format pred boxes (score > 0.3)
        pred_boxes = [p[:4] for p in img_preds if p[4] > 0.3]
        
        # Match
        matched_gt = set()
        matched_pred = set()
        
        for p_idx, p in enumerate(pred_boxes):
            best_iou = 0
            best_gt = -1
            for g_idx, g in enumerate(gt_boxes):
                iou = compute_iou(p, g)
                if iou > best_iou:
                    best_iou = iou
                    best_gt = g_idx
            if best_iou > 0.5:
                matched_gt.add(best_gt)
                matched_pred.add(p_idx)
                
        # Find FN (GT not matched)
        fns = [g for i, g in enumerate(gt_boxes) if i not in matched_gt]
        # Find FP (Pred not matched)
        fps = [p for i, p in enumerate(pred_boxes) if i not in matched_pred]
        
        if len(fns) > 0 or len(fps) > 0:
            rgb_path = os.path.join('/workspace/datasets/VTUAV_subset/VTUAV_subset/VTUAV_co/test/images', img_info['file_name'])
            if not os.path.exists(rgb_path): continue
            
            img = cv2.imread(rgb_path)
            if img is None: continue
            
            is_saved = False
            
            if len(fns) > 0 and fn_count < 5:
                for fn in fns:
                    x1, y1, x2, y2 = map(int, fn)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2) # Red for FN
                    cv2.putText(img, "FN (Missed)", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                fn_count += 1
                is_saved = True
                
            if len(fps) > 0 and fp_count < 5:
                for fp in fps:
                    x1, y1, x2, y2 = map(int, fp)
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 2) # Yellow for FP
                    cv2.putText(img, "FP (Ghost)", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
                fp_count += 1
                is_saved = True
                
            if is_saved:
                out_path = os.path.join(out_dir, f"failure_{img_info['file_name']}")
                cv2.imwrite(out_path, img)
                
    print(f"Generated {fn_count} False Negative images and {fp_count} False Positive images in {out_dir}")

if __name__ == '__main__':
    analyze_failures()
