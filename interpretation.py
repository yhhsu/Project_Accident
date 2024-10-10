import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Interprétation")
    st.write('''
    Dans un premier temps, nos taux de précision n’étaient pas idéaux. Nous avions pour 
    3 modéles pré-entrainés des taux de précision autour de 60-70% ce qui reste encore 
    à  améliorer  surtout  que  les  classes  minoritaires  avaient  des  taux  de  précision  très 
    faibles.
    ''')
    st.write("Par la suite, avec les amélioration apportées,")
    st.write("### XGBoost")
    st.image("xgboost.jpg")
    st.write("### LightGBM")
    st.image("lightgbm.jpg")
    st.write("### SVM")
    st.image("svm.jpg")
    st.write("### Random Forest")
    st.image("random_forest.jpg")
    st.write('''
    Nous convenons donc ensemble que le modèle le plus optimisé dans notre 
    problématique  de  prédiction  de  la  gravité  des  accidents  est  le  Random  Forest  car 
    sur  l’intégralité  de  ses  métriques  surtout  l’Accuracy,  il  surpasse  de  loin  les  autres 
    modèles.
    ''')
    st.write("C’est  donc  le  Random  Forest  qui  est  retenu  comme  modèle  le  plus  optimal  après différentes itérations et différents tests.")
    
