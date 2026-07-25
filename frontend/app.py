import os
import json
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

# Base directory for the project, one level up from the frontend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    stats = {
        'dataset': 'Analyzed - 62,575 val frames',
        'baseline_fps': '4.66',
        'baseline_ap': '0.320',
        'cmaf_fps': '4.73',
        'cmaf_ap': '0.354'
    }
    
    # User requested pulling directly from the markdown report
    report_path = os.path.join(BASE_DIR, 'reports', 'stage3', 'evaluation_report.md')
    if os.path.exists(report_path):
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Very basic parsing for this specific markdown structure
                for line in content.split('\n'):
                    if '| **mAP** |' in line:
                        parts = [p.strip() for p in line.split('|')]
                        stats['baseline_ap'] = parts[2]
                        stats['cmaf_ap'] = parts[3].replace('**', '')
                    elif '| **Inference FPS** |' in line:
                        parts = [p.strip() for p in line.split('|')]
                        stats['baseline_fps'] = parts[2]
                        stats['cmaf_fps'] = parts[3]
        except Exception as e:
            print("Error parsing MD:", e)
            
    return jsonify(stats)

@app.route('/api/files/<path:folder>')
def list_files(folder):
    """List images or files in a given directory relative to BASE_DIR"""
    target_dir = os.path.abspath(os.path.join(BASE_DIR, folder))
    # Basic path traversal protection
    if not target_dir.startswith(BASE_DIR):
        return jsonify([])
        
    if not os.path.exists(target_dir) or not os.path.isdir(target_dir):
        return jsonify([])
    
    files = []
    for f in os.listdir(target_dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            files.append(f)
    return jsonify(files)

@app.route('/media/<path:folder>/<filename>')
def get_media(folder, filename):
    """Serve media files from directories"""
    # restrict folders to known safe ones
    allowed_folders = ['outputs', 'results', 'data', 'docs', 'reports', 'visualization']
    # If the folder path starts with an allowed folder, it's safe
    top_dir = folder.split('/')[0].split('\\')[0]
    if top_dir not in allowed_folders:
        return "Not Found", 404
        
    target_dir = os.path.join(BASE_DIR, folder)
    return send_from_directory(target_dir, filename)

if __name__ == '__main__':
    # Run the app, accessible from any IP in the Docker container
    app.run(host='0.0.0.0', port=5000)
