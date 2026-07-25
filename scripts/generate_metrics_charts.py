import matplotlib.pyplot as plt
import numpy as np
import os

def generate_chart(out_dir, filename, title, ylabel, baseline_val, cmaf_val, color2):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 5))
    
    x = np.arange(2)
    width = 0.5
    
    rects = ax.bar(x, [baseline_val, cmaf_val], width, color=['#ff4a4a', color2])
    
    ax.set_ylabel(ylabel)
    ax.set_title(title, pad=20, fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(['Baseline', 'CMAF'], fontsize=11)
    
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=11, color='white')

    fig.tight_layout()
    out_path = os.path.join(out_dir, filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

def generate_comparison_charts():
    out_dir = '/workspace/results/visualizations/metrics'
    os.makedirs(out_dir, exist_ok=True)

    # mAP
    generate_chart(out_dir, 'chart_map.png', 'mAP Comparison (%)', 'mAP (%)', 0.320*100, 0.354*100, '#00ffcc')
    
    # FPS
    generate_chart(out_dir, 'chart_fps.png', 'Inference FPS', 'Frames Per Second', 4.66, 4.75, '#00ffcc')
    
    # Params
    generate_chart(out_dir, 'chart_params.png', 'Model Size (Parameters)', 'Millions of Parameters', 60.25, 15.65, '#00ffcc')
    
    print(f"Saved individual comparison charts to {out_dir}")

if __name__ == '__main__':
    generate_comparison_charts()
