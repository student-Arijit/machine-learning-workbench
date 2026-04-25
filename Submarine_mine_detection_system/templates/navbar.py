import streamlit as st
from handler import Handler

class Navbar:
    def __init__(self):
        self.css = Handler()
        self.css.load_css("")

    def main(self):
        st.markdown("""
            
            <hr>
                    """, unsafe_allow_html=True)