import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Conclusion")
    st.write('''
    Nous avons rencontré deux principaux verrous scientifiques. Le premier était 
    l’absence de corrélation significative entre les variables individuelles et la variable 
    cible, à savoir la gravité de l’accident. Cette absence de corrélation a compliqué la 
    modélisation prédictive, nécessitant des approches plus sophistiquées pour extraire 
    des informations pertinentes. Le second obstacle était notre a priori selon lequel le 
    modèle  XGBoost  serait  le  plus  performant.  Cette  hypothèse  nous  a  conduits  à 
    investir  un  temps  considérable  dans  l’optimisation  de  ce  modèle,  malgré  des 
    résultats initialement décevants. Cette focalisation excessive sur XGBoost a retardé 
    l’exploration d’autres modèles potentiellement plus adaptés à notre problématique.
    ''')
