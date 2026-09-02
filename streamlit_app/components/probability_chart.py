import streamlit as st
import pandas as pd


def render_probability_chart(probabilities):
    """Display prediction probabilities for all classes."""
    if not probabilities:
        st.info("Probability data is not available.")
        return
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-label">
                PREDICTION ANALYTICS
            </div>
            <h2>
                Class probability distribution
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Prob Dict to DataFrame
    data = pd.DataFrame(
        {
            "class": list(probabilities.keys()),
            "Probability": list(probabilities.values())
        }
    )

    # convert Decimal to percentages
    data["Probability"] = data["Probability"] * 100
    # Sort the High Prob First
    data = data.sort_values(
        by="Probability",
        ascending=False
    )
    st.bar_chart(
        data.set_index("class"),
        y="Probability"
    ) 

    # Display Exact Percentages
    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )