import streamlit as st
from templates.navbar import Navbar

class App:
    def __init__(self):
        self.navbar = Navbar()
        st.set_page_config(page_title="Sonar Object Classifier")
    
    def run(self):
        self.navbar.main()

if __name__ == "__main__":
    app = App()
    app.run()