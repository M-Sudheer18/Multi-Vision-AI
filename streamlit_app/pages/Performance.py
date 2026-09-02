import streamlit as st
from textwrap import dedent
from components.style import load_css
from components.sidebar import render_sidebar

def render_performance_page():
    """It Renders the Model Performance Page.."""
    # HERO
    st.markdown(
        dedent("""
        <div class="hero-section">
            <div class="hero-badge">
                📊 Model Performance
            </div>
            <h1>
                Evaluate Model<br>
                <span>Performance & Accuracy</span>
            </h1>
            <p class="hero-description">
                Review the performance of the trained TensorFlow CNN
                using evaluation metrics from the CIFAR-10 dataset.
            </p>
        </div>
        """),
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Metrics
    st.markdown(
        """
    <div class="section-heading">
        <div class="section-label">
            EVALUATION METRICS
        </div>
        <h2>
            Model performance indicators
        </h2>
    </div>
    """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4, gap="medium")
    with col1:
        st.metric(
            label="Test Accuracy",
            value="72.00%"
        )

    with col2:
        st.metric(
            label="Best Val Accuracy",
            value="96.22%"
        )

    with col3:
        st.metric(
            label="Precision",
            value="0.75"
        )

    with col4:
        st.metric(
            label="Recall",
            value="0.72"
        )
    st.markdown("<br>", unsafe_allow_html=True)

    # Additional Metrics
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.metric(
            label="F1-Score",
            value="0.72"
        )
    with col2:
        st.metric(
            label="Best Val Loss",
            value="0.1191"
        )
    with col3:
        st.metric(
            label="Best Epoch",
            value="7"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Training Summary
    st.markdown(
        """
    <div class="content-card">
        <div class="section-label">
            TRAINING SUMMARY
        </div>
        <h2>
            Best model checkpoint
        </h2>
        <p>
            The model was trained for a maximum of 20 epochs with
            early stopping enabled. Training stopped at epoch 12
            after the validation performance stopped improving.
        </p>
        <p>
            The best checkpoint was recorded at epoch 7, where the
            model achieved 96.22% validation accuracy and a
            validation loss of 0.1191. The model weights from this
            epoch were restored after early stopping.
        </p>
    </div>
    """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # CLASSIFICATION PERFORMANCE
    st.markdown(
        """
    <div class="section-heading">
        <div class="section-label">
            CLASSIFICATION PERFORMANCE
        </div>
        <h2>
            CIFAR-10 evaluation
        </h2>
    </div>
    """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
    <div class="content-card">
        <div class="tech-item">
            <strong>Test Samples</strong>
            <span>10,000</span>
        </div>
        <div class="tech-item">
            <strong>Test Accuracy</strong>
            <span>72.00%</span>
        </div>
        <div class="tech-item">
            <strong>Macro Precision</strong>
            <span>0.75</span>
        </div>
        <div class="tech-item">
            <strong>Macro Recall</strong>
            <span>0.72</span>
        </div>
        <div class="tech-item">
            <strong>Macro F1-Score</strong>
            <span>0.72</span>
        </div>
        <div class="tech-item">
            <strong>Weighted F1-Score</strong>
            <span>0.72</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Evaluation Metrics
    st.markdown(
        """
    <div class="content-card">
        <div class="section-label">
            EVALUATION DETAILS
        </div>
        <h2>
            Understanding the results
        </h2>
        <p>
            Accuracy represents the overall percentage of test
            images correctly classified by the model.
        </p>
        <p>
            Precision measures how often the model's predictions
            for a class are correct, while recall measures how
            effectively the model identifies samples belonging to
            that class.
        </p>
        <p>
            The F1-score combines precision and recall into a
            single metric and provides a balanced view of
            classification performance.
        </p>
        <p>
            The difference between the 96.22% best validation
            accuracy and the 72.00% test accuracy indicates that
            performance on the independent test dataset is lower
            than the best validation result.
        </p>
    </div>
    """,
        unsafe_allow_html=True
    )

def main():
    load_css()
    render_sidebar()
    render_performance_page()
    
if __name__ == "__main__":
    main()