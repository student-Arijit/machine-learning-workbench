import streamlit as st
from templates.handler import Handler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

class Signal_Source:
    def __init__(self):
        self.mine_sample = [0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,0.2156,0.3481,0.3337,0.2872,0.4918,0.6552,0.6919,0.7797,0.7464,0.9444,1.0,0.8874,0.8024,0.7818,0.5212,0.4052,0.3957,0.3914,0.325,0.32,0.3271,0.2767,0.4423,0.2028,0.3788,0.2947,0.1984,0.2341,0.1306,0.4182,0.3835,0.1057,0.184,0.197,0.1674,0.0583,0.1401,0.1628,0.0621,0.0203,0.053,0.0742,0.0399,0.0167,0.018,0.0083,0.0057,0.0027,0.0031,0.0065,0.0093,0.0059,0.0022,0.0028]
        self.rock_sample = [0.02,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.066,0.2273,0.31,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.555,0.6711,0.6415,0.7104,0.808,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.051,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.018,0.0084,0.009,0.0032]
        self.default = np.ones((60,))
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

            if 'data' not in st.session_state:
                st.session_state.data = self.default

            c1, c2 = st.columns([1, 3])
            with c1:
                if st.button("🪨 Rock Sample"):
                    st.session_state.data = self.rock_sample
                if st.button("💣 Mine Sample"):
                    st.session_state.data = self.mine_sample
            with c2:
                data = st.text_input(
                    "Enter 60-band frequency by CSV: ",
                    placeholder="Paste 60 comma-seperated frequency values"
                    )
                
                try:
                    st.session_state.data = pd.read_csv(StringIO(data), header=None).iloc[0].tolist()
                except pd.errors.EmptyDataError as e:
                    st.write("You Can also paste the Sonar data to detect.")


            st.markdown("""<p class="signal-title">Frequency Spectrum</p>""", unsafe_allow_html=True)    
            
            y = st.session_state.data
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

    def data_stat(self):
        with st.container(border=True, key="signal_stat"):
            st.markdown("""<p class="signal-title">Signal Statistics</p>""", unsafe_allow_html=True)

            df = np.array(st.session_state.data)

            c1, c2, c3 = st.columns(3)            
            with c1:
                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("Mean")
                    with col2:
                        st.write(np.round(df.mean(), 3))

                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("STD. DEV.")
                    with col2:
                        st.write(np.round(np.std(df), 3))
            
            with c2:
                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("Peak")
                    with col2:
                        st.write(np.round(df.max(), 3))

                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("Energy")
                    with col2:
                        st.write("feat. nt. aval")

            with c3:
                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("Weakest")
                    with col2:
                        st.write(np.round(df.min(), 3))
                
                with st.container(border=True):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("BANDS")
                    with col2:
                        st.write(len(df))