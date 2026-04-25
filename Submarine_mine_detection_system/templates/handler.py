import streamlit as st
from pathlib import Path

class Handler:
    def _read_file(self, file_path) -> str:
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found {path}")
        
        return path.read_text(encoding="UTF-8")

    def load_css(self, file_path) -> None:
        try:
            css_content = self._read_file(file_path)
            st.markdown(
                f"<style>{css_content}</style>", 
                unsafe_allow_html=True
            )
        
        except FileNotFoundError as e:
            st.error(f"Failed to load CSS File: {e}")