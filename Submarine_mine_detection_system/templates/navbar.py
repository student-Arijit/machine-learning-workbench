import streamlit as st
from templates.handler import Handler

class Navbar:
    def __init__(self):
        self.css = Handler()
        try:
            self.css.load_css("./Submarine_mine_detection_system/assets/style.css")
        except IsADirectoryError as e:
            st.error(f"Path Error, Empty path, {e}")

    def main(self):
        st.markdown("""
            <div class="nav-main">
                <div class="nav-left">
                    <div class="nav-dots">
                        <div class="dot dot1"></div>
                        <div class="dot dot2"></div>
                        <div class="dot dot3"></div>
                    </div>
                    <div class="nav-heading">Sonar Object Classifier</div>
                </div>
                <div class="nav-descp">60-Band Frequency Analysis | AI-Powered</div>
            </div>
                    """, unsafe_allow_html=True)