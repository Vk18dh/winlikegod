import json
import cv2
import os
import sys
import pickle

def draw_boxes(image_path, img_preds, out_path, color=(0, 0, 255)):
    # img_preds is a list of length num_classes. Each element is a numpy array of shape (N, 5) [x1, y1, x2, y2, score]
    img = cv2.imread(image_path)
    if img is None:
        print(f"Warning: Could not read {image_path}")
        return
        
    for class_idx, class_preds in enumerate(img_preds):
        for box in class_preds:
            x1, y1, x2, y2, score = box
            if score < 0.3: # Threshold
                continue
                
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(img, f"{score:.2f}", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    cv2.imwrite(out_path, img)

def visualize(model_name):
    print(f"Generating custom visualizations for {model_name}...")
    anno_path = '/workspace/datasets/VTUAV_subset/VTUAV_subset/annotations/test.json'
    pred_path = f'/workspace/results/predictions/{model_name}.pkl'
    out_dir = f'/workspace/results/visualizations/{model_name}'

    if not os.path.exists(pred_path):
        print(f"Error: Prediction file {pred_path} not found.")
        return

    with open(anno_path, 'r') as f:
        coco = json.load(f)
    
    with open(pred_path, 'rb') as f:
        preds = pickle.load(f)

    # Just visualize the first 10 images to save time and space
    img_list = coco['images'][:10]
    
    for i, img_info in enumerate(img_list):
        if i >= len(preds):
            break
            
        file_name = img_info['file_name']
        rgb_path = os.path.join('/workspace/datasets/VTUAV_subset/VTUAV_subset/VTUAV_co/test/images', img_info['file_name'])
        ir_path = os.path.join('/workspace/datasets/VTUAV_subset/VTUAV_subset/VTUAV_ir/test/images', img_info['file_name'])
        
        img_preds = preds[i] # This corresponds to the i-th image in the test set
        
        if os.path.exists(rgb_path):
            draw_boxes(rgb_path, img_preds, os.path.join(out_dir, "rgb", os.path.basename(file_name)))
        if os.path.exists(ir_path):
            draw_boxes(ir_path, img_preds, os.path.join(out_dir, "thermal", os.path.basename(file_name)))

    print(f"Visualizations saved to {out_dir}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python visualize_predictions.py <model_name>")
        sys.exit(1)
    visualize(sys.argv[1])
