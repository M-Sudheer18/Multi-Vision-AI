import streamlit as st

def render_prediction_card(predicted_class, confidence):
    """Displays The main prediction result card."""

    st.markdown(
        f"""
        <div class="prediction-card">
            <div class="prediction-label">
                PREDICTION RESULT
            </div>
            <div class="prediction-class">
                {predicted_class}
            </div>
            <div class="prediction-confidence">
                Confidence: <strong>{confidence}</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )