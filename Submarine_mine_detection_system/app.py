import streamlit as st
from templates.navbar import Navbar
from templates.signal_source import Signal_Source
from templates.predict import Predict

class App:
    def __init__(self):
        self.navbar = Navbar()
        self.data = Signal_Source()
        self.predict = Predict()
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
        with c2:
            self.predict.predict()
            
if __name__ == "__main__":
    app = App()
    app.run()