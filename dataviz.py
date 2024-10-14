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
