import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Structural Defect Detection", page_icon="🔍", layout="wide"
)

# Header section with title and subtitle
st.title("🏗️ Structural Defect Detection AI")
st.subheader("Theme 4 - Structural/Chemical Engineering | Group 2")

# Create columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
    ### 📋 Project Overview
    This AI system detects structural defects from image data to assist in maintenance and inspection of infrastructure.
    The model can identify various types of structural flaws including cracks, corrosion, and other defects that
    may compromise structural integrity.

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
    """
    )

with col2:
    st.markdown(
        """
    ### 👨‍💻 Team Members
    - Nathan Vu 
    - Xuan Tuan Minh Nguyen 
    ### Contributors
    - Aidid Yassin 
    - Leon Nhor 
    - Matthew Hadkins

    ### 🔧 Technology Stack
    - Python & Streamlit
    - Deep Learning (YOLOv8)
    - Computer Vision Libraries
    - Roboflow
    """
    )

# Navigation section
st.markdown("---")
st.header("📊 How to Use This Application")

st.markdown(
    """
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

Select your preferred method from the sidebar navigation menu above ☝️
"""
)

# Additional project information
st.markdown("---")
st.header("📚 Additional Information")

# Create three columns for additional info
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Research Background")
    st.markdown(
        """
    Our research focuses on applying computer vision and deep learning to automate structural inspections,
    which have traditionally been labor-intensive and sometimes dangerous manual processes.
    """
    )

with col2:
    st.subheader("Model Training")
    st.markdown(
        """
    The AI models were trained on thousands of annotated images of various structural defects
    across different infrastructure types including bridges, buildings, and industrial facilities.
    """
    )

with col3:
    st.subheader("Future Development")
    st.markdown(
        """
    Future versions will include severity scoring, maintenance recommendations,
    and integration with structural monitoring systems for continuous assessment.
    """
    )

# Navigation sidebar
with st.sidebar:
    st.title("Navigation")
    st.success("Select a page above to begin detection")

    # Project stats
    st.subheader("Project Stats")
    col1, col2 = st.columns(2)
    col1.metric("⚙️ Models", "2")
    col2.metric("🖼️ Dataset", "3k+ images")
