import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Interprétation")
        # Partie 1
        st.write("## 1. Feature Importance")

        # Partie 2
        st.write("## 2. Interprétation d'une prédiction")

        # Partie 2.A
        st.write("### 2.A. LIME")

        # Partie 2.B
        st.write("### 2.B. Interprétation prédiction de la classe 'Etat indemne'")

        # Partie 2.C
        st.write("### 2.C. Interprétation prédiction de la classe 'Etat blessures légères'")

        # Partie 2.D
        st.write("### 2.D. Interprétation prédiction de la classe 'Etat grave'")

    
