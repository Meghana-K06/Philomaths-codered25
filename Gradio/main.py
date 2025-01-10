from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

# Load pre-trained BLIP model and processor from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    # Preprocess the image and generate a caption
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Create a Gradio interface
iface = gr.Interface(fn=generate_caption, 
                     inputs=gr.Image(type="pil"), 
                     outputs=gr.Text(), 
                     live=True, 
                     title="Image Captioning with BLIP Model")

iface.launch()