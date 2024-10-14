import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

df = pd.read_csv("data_preprocessed.csv")

def app():
    st.title("Data Visualisation")

    st.write('''
    Cette partie de data visualisation nous a permis de comprendre les données et analyser les tendances et les relation entre celles-ci.
    ''')

     # Chart 1
    st.image("1.png", caption = "Evolution des accidents routiers en France")
    st.write('''
    Tout d’abord, Il est intéressant d’observer que le nombre d’accidents en France a drastiquement et continuellement baissé de 2005 à 2015 avant de connaître un léger rebond de 2015 à 2017. Ce qui laisse présager de meilleures précautions prises par les usagers de la route. 
    ''')

    # Chart 2&3
    st.write('''
    Ce nombre d’accident est particulièrement concentré dans deux départements : 
Le 13 (Bouche du Rhône) et le 75 (Paris), départements où il y’a en l’occurrence plus de trafic routier et par ailleurs le plus d’accidents mortels. 
    ''')
    col1, col2 = st.columns(2)
    with col1:
        st.image("2.png")
    with col2:
        st.image("3.png")
    
    # Chart 4&5
    st.write('''
    Statistiquement, il y’a plus d’accidents avec des hommes que des femmes 
    ''')
    col4, col5 = st.columns(2)
    with col4:
        st.image("4.png")
    with col5:
        st.image("5.png")
    st.write('''
   Mais les hommes s’en sortent globalement plus indemnes que les femmes.  
    ''')

    # Chart 6
    st.write('''
    Par ailleurs, notons que le risque d’être hospitalisé ou décédé suite à un accident routier en France évolue avec l’âge à partir des plus de 15 ans.
    ''')
    st.image("6.png")

   
    # Chart 7
    st.write('''
    Au-delà de cela, les piétons et les cyclistes/trottinettes ont plus de risque de finir hospitalisés ou tué après des accidents de la route
    ''')
    st.image("7.png")

    # Chart 8
    st.write('''
    Surtout quand la luminosité n’est pas au rendez-vous notamment la nuit.  
    ''')
    st.image("8.png")

    # Chart 9
    st.write('''
    Dans un second temps, il était pertinent de confirmer nos hypothèses sur les variables les plus pertinentes pour le modèle via la matrice de corrélation heatmap.
    ''')
    st.image("9.png")
    st.write('''
    Naturellement les variables locp (localisation du piéton), actp (action du piéton) et etatp (piéton seul ou non) ont une corrélation significative avec la variable catu(catégorie d’usager), autour de 0.60. Et ces 3 variables pré-citées ont une forte corrélation entre elles, autour de 0.80. 
    ''')

    st.write('''
    Toutefois, aucune variable ne semble avoir à elle seule une corrélation importante avec notre variable cible gravité.
    ''')
