import streamlit as st

# 1. Page Configuration (Must be the very first command)
st.set_page_config(
    page_title="Image Classification | Hub",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# from pathlib import Path
from components.style import load_css
from components.sidebar import render_sidebar


# HERO
def render_hero():
    """Main Landing Page.."""
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-badge">
                ✨ Image Classification
            </div>
            <h1>
                Understand Images<br>
                <span>with Deep Learning</span>
            </h1>
            <p class="hero-description">
                VisionClassify is a modern image classification platform
                powered by a trained Convolutional Neural Network and
                a Flask-based prediction API.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Project Overview
def render_overview():
    "Render the Main Project Overview..."
    col1, col2 = st.columns([1.7, 1], gap="large")
    with col1:
        st.markdown(
            """
            <div class="content-card">
                <div class="section-label">
                    PROJECT OVERVIEW
                </div>
                <h2>
                    Image Classification System
                </h2>
                <p>
                    VisionClassify allows users to upload an image and
                    receive an AI-generated classification result.
                    The application combines a Streamlit interface,
                    Flask REST API, image preprocessing, and a trained
                    TensorFlow CNN model.
                </p>
                <p>
                    The complete prediction pipeline validates the uploaded
                    file, preprocesses the image, performs model inference,
                    and returns the predicted class together with confidence
                    and probability information.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="content-card">
                <div class="section-label">
                    TECHNOLOGY STACK
                </div>
                <div class="tech-item">
                    <strong>Frontend</strong>
                    <span>Streamlit</span>
                </div>
                <div class="tech-item">
                    <strong>Backend</strong>
                    <span>Flask REST API</span>
                </div>
                <div class="tech-item">
                    <strong>Model</strong>
                    <span>TensorFlow CNN</span>
                </div>
                <div class="tech-item">
                    <strong>Dataset</strong>
                    <span>CIFAR-10</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )    

# System Capabilities..
def render_capabilities():
    """Capabilities of the Applictaion.."""
    st.markdown(
        """<div class="section-heading">
            <div class="section-label">
                SYSTEM CAPABILITIES
            </div>
            <h2>
                Everything needed for<br>
                image classification
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown(
            """<div class="feature-card">
                <div class="feature-icon">
                    📤
                </div>
                <h3>
                    Image Upload
                </h3>
                <p>
                    Upload an image through the Streamlit interface
                    and send it directly to the prediction pipeline.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """<div class="feature-card">
                <div class="feature-icon">
                    🧠
                </div>
                <h3>
                    CNN Inference
                </h3>
                <p>
                    The trained TensorFlow CNN analyzes the processed
                    image and calculates probabilities for each class.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """<div class="feature-card">
                <div class="feature-icon">
                    📊
                </div>
                <h3>
                    Prediction Analytics
                </h3>
                <p>
                    View the predicted class, confidence score,
                    and probability distribution across the classes.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
def render_footer():
    "Application Footer.."
    st.markdown(
        """ <div class="app-footer">
            VisionClassify · Image Classification Platform
        </div>
        """,
        unsafe_allow_html=True
    )


# Main App
def main():
    load_css()
    render_sidebar()
    st.markdown("<br>", unsafe_allow_html=True)
    render_hero()
    st.markdown("<br>", unsafe_allow_html=True)
    render_overview()
    st.markdown("<br>", unsafe_allow_html=True)
    render_capabilities()
    st.markdown("<br>", unsafe_allow_html=True)
    render_footer()


if __name__ == "__main__":
    main()