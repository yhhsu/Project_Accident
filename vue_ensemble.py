import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Vue d'Ensemble")
    st.write("### Projet Accidents Routiers en France")
    st.write("L’objectif de ce projet est d’essayer de prédire la gravité des accidents routiers en France. Les prédictions seront basées sur les données historiques.")
    st.image("traffic.jpg", caption = "Photo by Quaid Lagan on Unsplash")