FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-devel

# Avoid interactive prompts during apt installations
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 libxcb1 && rm -rf /var/lib/apt/lists/*

# Update pip and install MMDetection dependencies (this takes the longest)
RUN pip install --upgrade pip
RUN pip install -U openmim && mim install mmcv-full==1.7.0

# Set up working directory
WORKDIR /workspace

# Copy over requirements first to leverage Docker layer caching
COPY external/qfdet-baseline/requirements/ external/qfdet-baseline/requirements/

# Install QFDet-specific Python requirements and pin yapf
RUN pip install "numpy<2" "yapf==0.40.1" && \
    pip install -r external/qfdet-baseline/requirements/build.txt && \
    pip install -r external/qfdet-baseline/requirements/runtime.txt

# Install Frontend Requirements
RUN pip install Flask>=2.0.0

# Expose frontend port
EXPOSE 5000

# Copy and setup start script
COPY start.sh /workspace/start.sh
RUN chmod +x /workspace/start.sh

# Set default command
CMD ["/workspace/start.sh"]
