import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Interprétation")
    st.write("Dans un exercice de modélisation pour une problématique, le choix et les performances sont très importantes mais un aspect clé pour la partie métier est de comprendre comment les décisions de notre modèle ont été prises.")
    st.write("Nous allons dans cette partie identifier les Features les plus importantes de notre modèle et ensuite interpréter une prédiction pour chaque classe prédite".)
    # Partie 1 
    st.write("## 1. Feature Importance")
    # st.code('''
    # # Code pour extraire les features les plus importantes de notre modèle:
    # importances = model_lime.feature_importances_
    # indices = np.argsort(importances)[::-1]
    # ''', language='python')
    st.image("img/feature_importance.png", caption="Features les plus importantes de notre modèle RF Optimisé", use_column_width=True)

    # # Partie 2
    # st.write("## 2. Interprétation d'une prédiction")

    # # Partie 2.A
    # st.write("### 2.A. LIME")

    # # Partie 2.B
    # st.write("### 2.B. Interprétation prédiction de la classe Etat indemne")
    # st.image("img/interpretation_prediction_indemne.png", caption="Interpretation d'une prédiction de classe 'Indemne' - LIME", use_column_width=True)

    # # Partie 2.C
    # st.write("### 2.C. Interprétation prédiction de la classe Etat blessures légères")
    # st.image("img/interpretation_prediction_leger.png", caption="Interpretation d'une prédiction de classe 'Léger' - LIME", use_column_width=True)

    # # Partie 2.D
    # st.write("### 2.D. Interprétation prédiction de la classe Etat grave")
    # st.image("img/interpretation_prediction_grave.png", caption="Interpretation d'une prédiction de classe 'Grave' - LIME", use_column_width=True)

    
