import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    st.title("Jeu de Données")
    st.image("scheme.jpg")

    st.write("### Table Charateristics (16 Colonnes)")
    st.write('''
    - Num_Acc : Identifiant de l'accident
    - jour : Jour de l'accident
    - mois : Mois de l'accident
    - an : Année de l'accident
    - hrmn : Heure de l'accident en heures et minutes (hhmm)
    - lum : Conditions d'éclairage lors de l'accident
    - dep : Département : Code INSEE (Institut National de la Statistique et des Études Économiques) du département
    - com : Commune : Le numéro de la commune est un code attribué par l'INSEE. Le code comporte 3 chiffres alignés à droite
    - int : Type d'intersection
    - atm : Conditions atmosphériques
    - col : Type de collision
    - adr : Adresse postale : variable renseignée pour les accidents survenant en agglomération
    - gps : Codage GPS
    ''')

    st.write("### Table Places (18 Colonnes)")
    st.write('''
    - Num_Acc : Identifiant de l'accident
    - catr : Catégorie de route
    - voie : Numéro de la route
    - V1 : Indice numérique du numéro de la route (exemple : 2 bis, 3 ter, etc.)
    - V2 : Indice alphanumérique de la route
    - circ : Régime de circulation
    - nbv : Nombre total de voies de circulation
    - vosp : Indique l'existence d'une voie réservée, que l'accident ait eu lieu ou non sur cette voie.
    - Prof : Profil longitudinal décrit la pente de la route à l'endroit de l'accident
    - pr : Numéro de PR d'origine (numéro de borne amont)
    - pr1 : Distance en mètres jusqu'au PR (par rapport à la borne amont)
    - plan : Tracé en plan
    - lartpc : Largeur de terre-plein central (TPC) s'il y en a un
    - larrout : Largeur de la chaussée affectée à la circulation des véhicules, hors bandes d'arrêt d'urgence, CPR et places de stationnement
    - surf : État de la surface
    - infra : Aménagement - Infrastructure
    - situ : Situation de l'accident
    - env1 : Point école : à proximité d'une école
    ''')


    st.write("### Table Users (12 Colonnes)")
    st.write('''
    - Acc_number : Identifiant de l'accident.
    - Num_Veh : Identification du véhicule reprise pour chaque usager occupant ce véhicule (y compris les piétons qui sont associés aux véhicules qui les ont percutés).
    - place : Permet de localiser la place occupée dans le véhicule par l'usager au moment de l'accident.
    - catu : Catégorie d'usager.
    - grav : Gravité de l'accident : les usagers blessés sont classés en trois catégories de victimes, plus les indemnes.
    - sex : Sexe de l'usager.
    - Year_on : Année de naissance de l'usager.
    - trip : Raison du déplacement au moment de l'accident.
    - locp : Localisation du piéton.
    - actp : Action du piéton.
    - etatp : Cette variable permet de préciser si le piéton blessé était seul ou non.
    ''')

    st.write("### Table Vehicles (9 Colonnes)")
    st.write('''
    - Num_Acc : Identifiant de l'accident
    - Num_Veh : Identification du véhicule reprise pour chaque usager occupant ce véhicule (y compris les piétons qui sont associés aux véhicules qui les ont percutés) - code alphanumérique
    - GP : Sens de circulation
    - CATV : Catégorie de véhicule
    ''')