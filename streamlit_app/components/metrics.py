import streamlit as st

def render_metrics(predicted_class, confidence):
    """Prediction Metrics."""
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Predicted Class",
            value=predicted_class
        )
    with col2:
        st.metric(
            label="Confidence",
            value=confidence
        )