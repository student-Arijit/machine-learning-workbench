import streamlit as st
from templates.handler import Handler

class Predict:
    def __init__(self):
        self.css = Handler()
        try:
            self.css.load_css("./Submarine_mine_detection_system/assets/style.css")
        except IsADirectoryError as e:
            st.error(f"Path Error, Empty path, {e}")
    
    def predict(self):
        with st.container(border=True, key="predict"):
            st.write(st.session_state.data)