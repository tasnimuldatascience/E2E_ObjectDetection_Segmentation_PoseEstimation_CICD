import streamlit as st
from PIL import Image
from config.config import DEFAULT_IMAGE, DEFAULT_DETECT_IMAGE

def load_image(source_image):
    """
    Load and display an image.
    """
    try:
        if source_image is None:
            return Image.open(DEFAULT_IMAGE)
        return Image.open(source_image)
    except Exception as e:
        st.error("Error opening image.")
        st.error(str(e))
        return None

def detect_objects_in_image(model, image, confidence_value):
    """
    Run YOLO object detection on an image.
    """
    try:
        result = model.predict(image, conf=confidence_value)
        boxes = result[0].boxes
        result_plotted = result[0].plot()[:, :, ::-1]

        return result_plotted, boxes
    except Exception as e:
        st.error("Error during object detection.")
        st.error(str(e))
        return None, None
