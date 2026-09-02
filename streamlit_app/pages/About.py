import streamlit as st
from components.style import load_css
from components.sidebar import render_sidebar

def render_about_page():
    """Render the VisionClassify About Page."""

    # HERO
    st.markdown(
        """
        <div class="hero-section">
            <div class="hero-badge">
                ℹ️ About VisionClassify
            </div>
            <h1>
                About the<br>
                <span>VisionClassify System</span>
            </h1>
            <p class="hero-description">
                A deep learning based image classification platform
                that combines a Streamlit interface, Flask REST API,
                and a trained TensorFlow CNN model.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # PROJECT INFORMATION
    st.markdown(
        """
        <div class="content-card">
            <div class="section-label">
                ABOUT THE PROJECT
            </div>
            <h2>
                VisionClassify
            </h2>
            <p>
                VisionClassify is an image classification application
                designed to demonstrate an end-to-end deep learning
                prediction workflow.
            </p>
            <p>
                Users can upload an image through the Streamlit interface.
                The image is then sent to a Flask REST API, validated and
                preprocessed before being passed to the trained TensorFlow
                convolutional neural network for inference.
            </p>
            <p>
                The system returns the predicted class, confidence score,
                and probability distribution for the supported image
                categories.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # TECHNOLOGY STACK
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-label">
                TECHNOLOGY STACK
            </div>
            <h2>
                Technologies behind the system
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="content-card">
                <div class="tech-item">
                    <strong>Frontend</strong>
                    <span>Streamlit</span>
                </div>
                <div class="tech-item">
                    <strong>Backend</strong>
                    <span>Flask REST API</span>
                </div>
                <div class="tech-item">
                    <strong>Machine Learning</strong>
                    <span>TensorFlow / Keras</span>
                </div>
                <div class="tech-item">
                    <strong>Model Architecture</strong>
                    <span>Convolutional Neural Network</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="content-card">
                <div class="tech-item">
                    <strong>Dataset</strong>
                    <span>CIFAR-10</span>
                </div>
                <div class="tech-item">
                    <strong>Image Input</strong>
                    <span>JPG / JPEG / PNG</span>
                </div>
                <div class="tech-item">
                    <strong>API Method</strong>
                    <span>POST /predict</span>
                </div>
                <div class="tech-item">
                    <strong>Output</strong>
                    <span>Class + Confidence + Probabilities</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # PREDICTION PIPELINE
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-label">
                PREDICTION PIPELINE
            </div>
            <h2>
                From image to prediction
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">
                    📤
                </div>
                <h3>
                    01. Upload
                </h3>
                <p>
                    The user selects an image through the Streamlit
                    prediction interface.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">
                    ⚙️
                </div>
                <h3>
                    02. Process
                </h3>
                <p>
                    Flask validates the uploaded file and the image
                    preprocessing pipeline prepares it for inference.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">
                    🧠
                </div>
                <h3>
                    03. Predict
                </h3>
                <p>
                    The trained CNN performs inference and returns the
                    predicted class with confidence and probabilities.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # SYSTEM DESIGN
    st.markdown(
        """
        <div class="content-card">
            <div class="section-label">
                SYSTEM DESIGN
            </div>
            <h2>
                Separation of responsibilities
            </h2>
            <p>
                The application separates the user interface, API layer,
                prediction service, preprocessing logic, and model
                inference components.
            </p>
            <p>
                Streamlit is responsible for the user-facing interface,
                while Flask exposes the prediction endpoint. The
                prediction service coordinates validation and inference,
                allowing the machine learning pipeline to remain
                independent from the frontend.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # PROJECT SUMMARY
    st.markdown(
        """
        <div class="content-card">
            <div class="section-label">
                PROJECT SUMMARY
            </div>
            <h2>
                End-to-end AI application
            </h2>
            <p>
                VisionClassify demonstrates how a trained deep learning
                model can be integrated into a complete application rather
                than being used only inside a notebook.
            </p>
            <p>
                The project brings together model inference, image
                preprocessing, API development, validation, error
                handling, and an interactive web interface into a single
                classification platform.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def main():
    load_css()
    render_sidebar()
    render_about_page()


if __name__ == "__main__":
    main()