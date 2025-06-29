# 🏗️ Structural Defect Detection AI

## Theme 4 - Structural/Chemical Engineering 

### 📋 Project Overview

This AI system detects structural defects from image data to assist in maintenance and inspection of infrastructure. The model can identify various types of structural flaws including cracks, corrosion, and other defects that may compromise structural integrity.

### 🎯 Key Objectives

- Develop a deep learning model to recognize structural flaws in photos with high accuracy
- Enable confident identification of defect types (rust, cracks, etc.)
- Improve automation of structural inspections
- Reduce maintenance costs and increase safety through early detection

### 💡 Key Features

- Multi-class defect classification
- Support for image, video, and real-time analysis
- High-resolution drone photography compatibility
- Confidence scoring for detected defects

### 👨‍💻 Team Members

- Nathan Vu 
- Xuan Tuan Minh Nguyen

### 🔧 Technology Stack

- Python & Streamlit
- Deep Learning (YOLOv8)
- Computer Vision Libraries
- Roboflow

## 📊 How to Use This Application

### 📦 Installation

0. Required Python Version: 3.12

1. Clone the repository

```bash
git clone https://github.com/NathanVuSwinburne/Structural-Defect-Detection-AI-for-Structural-Engineering.git
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Apply `PYTHONPATH`, could be either export or set it via `.env` file

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

or

```bash
PYTHONPATH=$(pwd) streamlit run 1_Home_Page.py
```

or

```env
PYTHONPATH=$(pwd)
```

4. Run the application

```bash
streamlit run 1_Home_Page.py
```

### Navigation Instructions

This application offers three different ways to detect structural defects:

1. **🖼️ Image Analysis**

   - Navigate to the "Image Prediction" page in the sidebar
   - Upload your structural images
   - Get instant analysis of potential defects

2. **🎬 Video Analysis**

   - Select the "Video Prediction" page
   - Upload video footage of structures
   - Receive frame-by-frame defect detection

3. **📹 Webcam Analysis**
   - Go to the "Webcam Prediction" page
   - Enable your camera when prompted
   - Point your camera at structures for real-time analysis

## 📚 Additional Information

### Research Background

Our research focuses on applying computer vision and deep learning to automate structural inspections, which have traditionally been labor-intensive and sometimes dangerous manual processes.

### Model Training

The AI models were trained on a set of annotated images of 2 structural defects, which are rust and cracks, on the telecommunication towers. However, we believe that the model can still detect defects across different infrastructure types, including bridges, buildings, and industrial facilities.
### Future Development

Future versions will include severity scoring, maintenance recommendations, and integration with structural monitoring systems for continuous assessment.

### Project Stats

- Models: 2(Object detection model and segmentation model)
- Dataset: 3K+ images

### Technical Details

- To be updated
