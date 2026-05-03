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
            <p> hello</p>
            <hr>
                    """, unsafe_allow_html=True)