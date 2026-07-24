import sys
import re
import json

def parse_metrics(txt_path, json_path):
    with open(txt_path, 'r') as f:
        content = f.read()

    # Search for OrderedDict at the end of MMDetection eval output
    # e.g., OrderedDict([('bbox_mAP', 0.320), ('bbox_mAP_50', 0.589), ...])
    match = re.search(r"OrderedDict\(\[(.*)\]\)", content)
    if not match:
        print(f"Error: Could not find OrderedDict in {txt_path}")
        # Write empty metrics so pipeline doesn't crash
        with open(json_path, 'w') as f:
            json.dump({}, f)
        return

    inner = match.group(1)
    # The inner string looks like: ('bbox_mAP', 0.320), ('bbox_mAP_50', 0.589)
    # Let's parse it using regex for tuples
    tuples = re.findall(r"\('([^']+)', ([^\)]+)\)", inner)
    
    metrics = {}
    for key, val in tuples:
        val = val.strip().strip("'").strip('"')
        try:
            val = float(val)
        except ValueError:
            pass # Keep as string (like copypaste string)
        metrics[key] = val

    with open(json_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"Parsed metrics saved to {json_path}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python parse_metrics.py <input_txt> <output_json>")
        sys.exit(1)
    parse_metrics(sys.argv[1], sys.argv[2])
