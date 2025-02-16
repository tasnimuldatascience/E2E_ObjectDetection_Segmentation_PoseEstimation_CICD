import streamlit as st
from ultralytics import YOLO
from config.config import DETECTION_MODEL, SEGMENTATION_MODEL, POSE_ESTIMATION_MODEL

def load_model(model_type):
    """
    Load the YOLO model based on user selection.
    """
    model_paths = {
        "Detection": DETECTION_MODEL,
        "Segmentation": SEGMENTATION_MODEL,
        "Pose Estimation": POSE_ESTIMATION_MODEL
    }

    try:
        model_path = model_paths.get(model_type)
        return YOLO(model_path)
    except Exception as e:
        st.error(f"Error loading model: {model_path}")
        st.error(str(e))
        return None
