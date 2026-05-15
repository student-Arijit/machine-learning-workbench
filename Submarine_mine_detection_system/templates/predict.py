import streamlit as st
from templates.handler import Handler
import pickle
import numpy as np

class Predict:
    def __init__(self):
        self.css = Handler()
        try:
            self.css.load_css("./Submarine_mine_detection_system/assets/style.css")
        except IsADirectoryError as e:
            st.error(f"Path Error, Empty path, {e}")
    
    def predict(self):
        with st.container(border=True, key="predict"):
            with open("./Submarine_mine_detection_system/models/model.pkl", "rb") as file:
                model = pickle.load(file)

            nparray = np.asarray(st.session_state.data)
            data_reshaped = nparray.reshape(1, -1)

            prediction = model.predict(data_reshaped)
            probability = model.predict_proba(data_reshaped)

            is_mine = prediction[0] == "M"
            label = "MINE" if is_mine else "ROCK"
            mine_conf = probability[0][0] * 100
            rock_conf = probability[0][1] * 100
            primary_conf = mine_conf if is_mine else rock_conf

            accent = "#ff3b3b" if is_mine else "#3bdfff"
            icon = "💣" if is_mine else "🪨"

            st.markdown(f"""

            <div class="sonar-card">
                <div class="status-line">
                    <div class="status-dot"></div>
                    SYSTEM ACTIVE · MODEL INFERENCE COMPLETE
                </div>
            <div class="sonar-header">▶ SONAR CLASSIFICATION RESULT</div>
            <div class="sonar-result">
                <div class="sonar-icon">{icon}</div>
                <div>
                <div class="sonar-label">{label}</div>
                <div class="sonar-sublabel">OBJECT DETECTED · {primary_conf:.1f}% CONFIDENCE</div>
                </div>
            </div>
            <div class="divider"></div>
            <div class="conf-row">
                <div class="conf-item">
                <div class="conf-meta">
                    <span>💣 MINE PROBABILITY</span>
                    <span>{mine_conf:.2f}%</span>
                </div>
                <div class="conf-track">
                    <div class="conf-fill mine" style="width:{mine_conf}%"></div>
                </div>
                </div>
                <div class="conf-item">
                <div class="conf-meta">
                    <span>🪨 ROCK PROBABILITY</span>
                    <span>{rock_conf:.2f}%</span>
                </div>
                <div class="conf-track">
                    <div class="conf-fill rock" style="width:{rock_conf}%"></div>
                </div>
                </div>
            </div>
            
            </div>
            """, unsafe_allow_html=True)