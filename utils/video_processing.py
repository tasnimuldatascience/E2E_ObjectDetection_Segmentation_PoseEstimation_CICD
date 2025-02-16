import cv2
import streamlit as st
from config.config import VIDEOS_DICT

def process_video(model, video_key, confidence_value):
    """
    Process and display YOLO predictions on video frames.
    """
    try:
        video_path = VIDEOS_DICT.get(video_key)
        video_cap = cv2.VideoCapture(str(video_path))
        st_frame = st.empty()

        while video_cap.isOpened():
            success, frame = video_cap.read()
            if not success:
                break

            frame_resized = cv2.resize(frame, (720, int(720 * (9/16))))
            result = model.predict(frame_resized, conf=confidence_value)
            result_plotted = result[0].plot()
            st_frame.image(result_plotted, caption="Detected Video", channels="BGR")

        video_cap.release()
    except Exception as e:
        st.error(f"Error processing video: {str(e)}")
