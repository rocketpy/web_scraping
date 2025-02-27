# OmniParser - Screen Parsing tool for Pure Vision Based GUI Agent

# https://github.com/microsoft/OmniParser


# Install

"""
First clone the repo, and then install environment:

cd OmniParser
conda create -n "omni" python==3.12
conda activate omni
pip install -r requirements.txt
Ensure you have the V2 weights downloaded in weights folder (ensure caption weights folder is called icon_caption_florence). If not download them with:

# download the model checkpoints to local directory OmniParser/weights/
for f in icon_detect/{train_args.yaml,model.pt,model.yaml} icon_caption/{config.json,generation_config.json,model.safetensors}; 
do huggingface-cli download microsoft/OmniParser-v2.0 "$f" --local-dir weights; done mv weights/icon_caption weights/icon_caption_florence 
"""

# Gradio Demo
# python gradio_demo.py


# Examples:

from util.utils import get_som_labeled_img, check_ocr_box, get_caption_model_processor, get_yolo_model
import torch
from ultralytics import YOLO
from PIL import Image


device = 'cuda'
model_path='weights/icon_detect/model.pt'

som_model = get_yolo_model(model_path)

som_model.to(device)
print('model to {}'.format(device))
