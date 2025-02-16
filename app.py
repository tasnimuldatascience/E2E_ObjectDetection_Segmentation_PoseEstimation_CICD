import streamlit as st
from utils.model_loader import load_model
from utils.image_processing import load_image, detect_objects_in_image
from utils.video_processing import process_video
from config.config import APP_TITLE, APP_ICON, VIDEOS_DICT
from PIL import Image

# Set Page Config
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

# Header
st.header("Object Detection, Segmentation, and Pose Estimation using YOLOv11")

# Sidebar Configuration
st.sidebar.header("Model Configurations")
model_type = st.sidebar.radio("Select Task", ["Detection", "Segmentation", "Pose Estimation"])
confidence_value = float(st.sidebar.slider("Model Confidence", 25, 100, 40)) / 100

# Load YOLO Model
model = load_model(model_type)
if not model:
    st.stop()  # Stop execution if model loading fails

# Image/Video Selection
st.sidebar.header("Input Source")
source_radio = st.sidebar.radio("Select Source", ["Image", "Video"])

if source_radio == "Image":
    source_image = st.sidebar.file_uploader("Upload an Image...", type=["jpg", "png", "jpeg", "bmp", "webp"])
    
    col1, col2 = st.columns(2)
    with col1:
        image = load_image(source_image)
        if image:
            st.image(image, caption="Input Image", use_container_width=True)  # ✅ Updated

    with col2:
        if st.sidebar.button("Detect Objects"):
            detected_image, boxes = detect_objects_in_image(model, image, confidence_value)
            if detected_image is not None:
                st.image(detected_image, caption="Detected Objects", use_container_width=True)  # ✅ Updated
                with st.expander("Detection Results"):
                    for box in boxes:
                        st.write(box.data)


elif source_radio == "Video":
    source_video = st.sidebar.selectbox("Choose a Video...", list(VIDEOS_DICT.keys()))
    with open(VIDEOS_DICT[source_video], 'rb') as video_file:
        video_bytes = video_file.read()
        if video_bytes:
            st.video(video_bytes)
    
    if st.sidebar.button("Detect Video Objects"):
        process_video(model, source_video, confidence_value)
