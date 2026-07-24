import os
import glob
from PIL import Image
import json

def analyze_dataset(dataset_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Dataset Analysis: VTUAV_subset\n\n")

        # 1. Dataset Tree (up to 3 levels deep to avoid massive output)
        f.write("## Dataset Tree\n```text\n")
        
        def tree(dir_path, prefix="", depth=0, max_depth=3):
            if depth > max_depth:
                return
            try:
                contents = os.listdir(dir_path)
            except PermissionError:
                return
            pointers = [('├── ' if i < len(contents) - 1 else '└── ') for i in range(len(contents))]
            for pointer, path in zip(pointers, contents):
                full_path = os.path.join(dir_path, path)
                f.write(prefix + pointer + path + "\n")
                if os.path.isdir(full_path):
                    extension = '│   ' if pointer == '├── ' else '    '
                    tree(full_path, prefix=prefix + extension, depth=depth + 1, max_depth=max_depth)
        
        tree(dataset_path)
        f.write("```\n\n")

        # Metrics
        total_images = 0
        total_annotations = 0
        rgb_images = []
        thermal_images = []
        annotation_files = []
        resolutions = set()

        for root, dirs, files in os.walk(dataset_path):
            for file in files:
                ext = file.lower().split('.')[-1]
                full_path = os.path.join(root, file)
                if ext in ['jpg', 'png', 'jpeg']:
                    total_images += 1
                    try:
                        with Image.open(full_path) as img:
                            resolutions.add(f"{img.width}x{img.height}")
                    except Exception as e:
                        pass
                    
                    if 'rgb' in full_path.lower():
                        rgb_images.append(full_path)
                    elif 't' in full_path.lower() or 'ir' in full_path.lower() or 'thermal' in full_path.lower():
                        thermal_images.append(full_path)
                    else:
                        # try guessing based on filename
                        if 'rgb' in file.lower() or 'v' in file.lower(): # v for visible
                            rgb_images.append(full_path)
                        elif 't' in file.lower() or 'i' in file.lower(): # i for infrared
                            thermal_images.append(full_path)

                elif ext in ['txt', 'json', 'xml']:
                    total_annotations += 1
                    annotation_files.append(full_path)

        # 2. Image Counts
        f.write("## Image Counts\n")
        f.write(f"- Total Images: {total_images}\n")
        f.write(f"- RGB Images (approx): {len(rgb_images)}\n")
        f.write(f"- Thermal Images (approx): {len(thermal_images)}\n")
        f.write(f"- Total Annotations: {total_annotations}\n\n")

        # 3. Annotation Format & 4. Sample Annotations
        f.write("## Annotation Format & Samples\n")
        if annotation_files:
            sample_anno = annotation_files[0]
            ext = sample_anno.split('.')[-1].lower()
            f.write(f"Format appears to be: **{ext.upper()}**\n\n")
            f.write("Sample Annotation:\n")
            f.write(f"File: `{sample_anno}`\n")
            f.write("```\n")
            try:
                with open(sample_anno, 'r', encoding='utf-8') as af:
                    content = af.read()
                    if len(content) > 500:
                        content = content[:500] + "\n...[truncated]"
                    f.write(content)
            except Exception as e:
                f.write(f"Error reading file: {e}")
            f.write("\n```\n\n")
        else:
            f.write("No annotation files found.\n\n")

        # 5. Image Resolutions
        f.write("## Image Resolutions\n")
        for res in resolutions:
            f.write(f"- {res}\n")
        f.write("\n")

        # 6. RGB-Thermal pairing verification & 7. Missing files report
        f.write("## RGB-Thermal Pairing Verification\n")
        # Assuming typical VTUAV structure: sequences contain rgb and ir folders.
        rgb_basenames = {os.path.splitext(os.path.basename(p))[0] for p in rgb_images}
        thermal_basenames = {os.path.splitext(os.path.basename(p))[0] for p in thermal_images}
        
        common = rgb_basenames.intersection(thermal_basenames)
        rgb_only = rgb_basenames - thermal_basenames
        thermal_only = thermal_basenames - rgb_basenames
        
        f.write(f"- Perfectly paired basenames: {len(common)}\n")
        f.write(f"- Unpaired RGB images: {len(rgb_only)}\n")
        f.write(f"- Unpaired Thermal images: {len(thermal_only)}\n\n")
        
        if rgb_only or thermal_only:
            f.write("### Missing Files Report\n")
            if rgb_only:
                f.write(f"Sample missing thermal counterparts for: {list(rgb_only)[:5]}\n")
            if thermal_only:
                f.write(f"Sample missing RGB counterparts for: {list(thermal_only)[:5]}\n")
        f.write("\n")

        # 8. Dataset Summary
        f.write("## Dataset Summary\n")
        f.write("The VTUAV subset contains ")
        if total_images == 0:
            f.write("no images. Please check the provided path.\n")
        else:
            f.write(f"{total_images} images with {total_annotations} annotation files. ")
            f.write(f"Images have {len(resolutions)} distinct resolutions. ")
            if len(rgb_only) == 0 and len(thermal_only) == 0:
                f.write("RGB and Thermal images are perfectly paired.\n")
            else:
                f.write("There are some unpaired images which may require data cleaning.\n")

if __name__ == '__main__':
    dataset_path = r'C:\Users\dhyan\Desktop\hackathon-2\FusionGuard-AI\datasets\VTUAV_subset'
    output_file = r'C:\Users\dhyan\Desktop\hackathon-2\FusionGuard-AI\docs\dataset_analysis.md'
    analyze_dataset(dataset_path, output_file)
    print(f"Analysis saved to {output_file}")
