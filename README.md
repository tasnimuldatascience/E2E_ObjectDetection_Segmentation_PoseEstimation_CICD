# End2End YOLOv11 Streamlit App

This project is a **Streamlit-based application** that performs **Object Detection, Segmentation, and Pose Estimation** using YOLOv11 models.

## 🚀 Features

- **Object Detection:** Detect objects in images and videos using YOLOv11.
- **Segmentation:** Perform instance segmentation to segment objects in an image.
- **Pose Estimation:** Identify human poses in images and videos.
- **User-friendly UI:** Built using Streamlit for easy interaction.

---

## 🏗️ Project Structure

```
YOLO11_STREAMLIT/
│── config/
│   ├── config.py                 # Configuration file (paths, constants)
│── images/
│   ├── image1.jpg                # Sample image
│   ├── detectedimage1.jpg         # Processed image
│── utils/
│   ├── image_processing.py       # Image processing utilities
│   ├── model_loader.py           # Model loading functions
│   ├── video_processing.py       # Video processing utilities
│── videos/
│   ├── video1.mp4                # Sample video 1
│   ├── video2.mp4                # Sample video 2
│── weights/                      # Folder for YOLO model weights
│── app.py                        # Main Streamlit application
│── requirements.txt               # Required dependencies
│── .gitignore                     # Ignore unnecessary files
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/YOLO11_STREAMLIT.git
cd YOLO11_STREAMLIT
```

### 2️⃣ Install Dependencies

Create a virtual environment and install required packages:

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```sh
streamlit run app.py
```

---

## 📂 Configuration (config.py)

Modify `config/config.py` to update paths and parameters:

```python
ROOT = Path(__file__).parent.parent
IMAGES_DIR = ROOT / 'images'
VIDEO_DIR = ROOT / 'videos'
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolo11n.pt'
```

---

## 🎯 Usage

### **🔹 Image Processing**

1. Upload an image via the sidebar.
2. Choose the **model type** (Detection, Segmentation, or Pose Estimation).
3. Click "Detect Objects" to process the image.

### **🔹 Video Processing**

1. Select a sample video or upload your own.
2. Choose the **model type** (Detection, Segmentation, or Pose Estimation).
3. Click "Detect Video Objects" to run YOLO on video frames.

---

## 🔧 Troubleshooting

- **Issue:** Model not loading?

  - Ensure the weights are in the `weights/` folder.
  - Check `config.py` for correct paths.

- **Issue:** App crashes on large videos?

  - Try resizing the video before uploading.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 💡 Acknowledgments

- **Ultralytics YOLOv11** for the core object detection model.
- **Streamlit** for the interactive UI.

---

Enjoy using the **YOLO11 Streamlit App**! 🚀

