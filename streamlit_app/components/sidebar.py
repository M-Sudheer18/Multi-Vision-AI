import streamlit as st


def render_sidebar():
    """Render the VisionClassify navigation sidebar."""

    with st.sidebar:

        # Brand
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="sidebar-brand-icon">👁️</div>
                <div>
                    <div class="sidebar-brand-name">VisionClassify</div>
                    <div class="sidebar-brand-subtitle">
                        Image Classification
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Navigation Label
        st.markdown(
            '<div class="sidebar-section-label">NAVIGATION</div>',
            unsafe_allow_html=True
        )

        # Navigation
        st.page_link(
            "app.py",
            label="Home",
            icon="🏠"
        )

        st.page_link(
            "pages/Prediction.py",
            label="Prediction",
            icon="🔍"
        )

        st.page_link(
            "pages/Performance.py",
            label="Performance",
            icon="📊"
        )

        st.page_link(
            "pages/About.py",
            label="About",
            icon="ℹ️"
        )

        # Divider
        st.markdown(
            "<hr>",
            unsafe_allow_html=True
        )

        # Sidebar Footer
        st.markdown(
            """
            <div class="sidebar-footer">
                <div class="sidebar-status-dot"></div>
                <div>
                    <div class="sidebar-status-title">
                        System Ready
                    </div>
                    <div class="sidebar-status-text">
                        VisionClassify
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )