import streamlit as st
from templates.handler import Handler
import numpy as np
import matplotlib.pyplot as plt

class Signal_Source:
    def __init__(self):
        self.css = Handler()
        try:
            self.css.load_css("./Submarine_mine_detection_system/assets/style.css")
        except IsADirectoryError as e:
            st.error(f"Path Error, Empty path, {e}")

    #dialog box will be added
    
    def data(self):
        with st.container(border=True, key="my_container"):
            col1, col2, col3 = st.columns([1,2,0.5])
            with col1:
                st.markdown("""<p class="signal-title">Signal Source</p>""", unsafe_allow_html=True)
            with col3:
                if st.button("RUN"):
                    st.write("dsj")
            
            c1, c2 = st.columns([1, 3])
            with c1:
                if st.button("🪨 Rock Sample"):
                    st.write("r")
                if st.button("💣 Mine Sample"):
                    st.write("m")
            with c2:
                st.text_input(
                    "Enter 60-band frequency by CSV: ",
                    placeholder="Paste 60 comma-seperated frequency values"
                    )
            st.markdown("""<p class="signal-title">Frequency Spectrum</p>""", unsafe_allow_html=True)    
            
            
            y = np.random.randint(1, 10, 60)
            x = np.arange(len(y))
            fig, ax = plt.subplots(figsize=(10, 2))
            fig.patch.set_facecolor("#0a0f1c00")
            ax.set_facecolor("#0a0f1c00")
            ax.set_xticks([])
            ax.set_yticks([])
            for spine in ax.spines.values():
                spine.set_visible(False)

            ax.bar(x, y, color='#00e5ff', width=0.8)
            st.pyplot(fig)

            st.markdown("""<p class="signal-title">Band Editor</p>""", unsafe_allow_html=True)
            
            