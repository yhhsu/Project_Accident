import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Conclusion")

    st.write("### Bilan")
    st.markdown('''
    Niveau d'atteinte par rapport à nos objectifs de départ:
    - **Nettoyage et préparation des données - Done**
    - **Analyse exploratoire des données pour comprendre notre dataset et identifier des potentielles variables impactantes - Done**
    - **Développement et optimisation de différents modèles de Machine Learning - Done**
    - **Interprétation des prédictions notre modèle - Done**
    ''')
    
    
    st.write("### Difficultés rencontrées lors du projet")
    st.markdown('''
    Au cours de notre projet, nous avons rencontré plusieurs phases sur lesquelles nous avons eu des difficultés:
    - **Absence de corrélation flagrante entre nos features et notre variable cible**
    - **Temps considérable passé à d'optimiser un Xgboost qui n'a pas été concluant au final**
    - **Echec dans l'implémentation des SHAP values pour l'interprétation des résultats du modèle**
    - **Faible puissance de calcul de nos machines qui nous ont restreint sur l'optimisation de nos modèles**
    ''')
    

    st.write("### Pistes d'amélioration")
    st.markdown('''
    Avec du recul sur les travaux qui ont été entrepris au cours de notre projet, nous avons discuté de plusieurs pistes d'améliorations interessantes à explorer.
    - **Réfléchir à une autre problématique (se focus uniquement sur un scope en particulier afin de pouvoir profiter de toutes les années de données, par ex : Accidents de vélo ou moto, Se focus sur un département ou une ville en particulier)**
    - **Améliorer la phase de preprocess / Selection des features** - Clusters/ACP pour réduire les dimensions des variables (pour les communes / départements par exemple)
    - **Ajout d'une deuxième couche de modélisation** - Afin de distinguer les personnes "Hospitalisées" des personnes "Décédé" dans notre classe "Grave".
    - **Mieux comprendre l'interprétation de nos résultats** - A l'aide de SHAP par exemple
    ''')
