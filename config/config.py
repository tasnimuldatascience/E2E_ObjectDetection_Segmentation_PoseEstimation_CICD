from pathlib import Path

# Define root directory
ROOT = Path(__file__).parent.parent

# Directories
IMAGES_DIR = ROOT / 'images'
VIDEO_DIR = ROOT / 'videos'
MODEL_DIR = ROOT / 'weights'

# Default images
DEFAULT_IMAGE = IMAGES_DIR / 'image1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'detectedimage1.jpg'

# Video files
VIDEOS_DICT = {
    'video 1': VIDEO_DIR / 'video1.mp4',
    'video 2': VIDEO_DIR / 'video2.mp4'
}

# Model paths
DETECTION_MODEL = MODEL_DIR / 'yolo11n.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolo11n-seg.pt'
POSE_ESTIMATION_MODEL = MODEL_DIR / 'yolo11n-pose.pt'

# Page configuration
APP_TITLE = "YOLO Streamlit App"
APP_ICON = "🤖"
