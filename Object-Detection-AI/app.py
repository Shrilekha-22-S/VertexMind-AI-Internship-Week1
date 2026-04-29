import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Load model
model = YOLO("yolov8n.pt", task="detect")

st.title("🚀 AI Object Detection App")

st.write("Upload an image and detect objects using YOLOv8")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    image = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Run detection
    results = model(image)

    # Annotated output
    annotated_img = results[0].plot()

    st.image(annotated_img, caption="Detected Objects", use_column_width=True)

    st.success("Detection completed 🚀")