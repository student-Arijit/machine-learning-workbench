import streamlit as st
from templates.navbar import Navbar
from templates.signal_source import Signal_Source

class App:
    def __init__(self):
        self.navbar = Navbar()
        self.data = Signal_Source()
        st.set_page_config(
            page_title="Sonar Object Classifier", 
            layout="wide"
            )
    
    def run(self):
        self.navbar.main()
        c1, c2 = st.columns(2)
        with c1:
            self.data.data()
            self.data.data_stat()
        
            
if __name__ == "__main__":
    app = App()
    app.run()