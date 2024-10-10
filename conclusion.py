import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Conclusion")
    st.write("### Difficultés rencontrées lors du projet")
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
    st.write('''
    Ainsi nous avons consacré une quantité considérable de temps à l’instanciation des 
    modèles,  et  ces  derniers  nécessitaient  des  durées  d’exécution  extrêmement 
    prolongées en raison de la volumétrie importante du jeu de données. Cette situation 
    a considérablement ralenti notre progression et a exigé des ressources 
    computationnelles substantielles.  De plus, d’un point  de vue IT, la puissance  de 
    stockage et la capacité computationnelle des ordinateurs de certains membres de 
    l’équipe n’étaient pas adaptées, ce qui a encore accentué les défis rencontrés.
    ''')
