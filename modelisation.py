import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

df = pd.read_csv("data_preprocessed.csv")


def app():
    st.title("Modélisation")

    df = pd.read_csv("data_preprocessed.csv")
    df = df[df["annee"] == 2015].reset_index(drop=True)

    df.replace('nan', -1, inplace=True)
    df.fillna(-1, inplace = True)
    col_to_convert_object = ["catu", "sexe", "catv", "situ", "lum", "agg", "int", "atm", "col", "place", "trajet", "locp", "actp", "etatp", "senc", "obs", "obsm", "choc", "manv", "catr", "circ", "vosp",
    "prof", "plan", "surf", "infra", "situ", "atm", "col", "dep", "com"]

    for col in col_to_convert_object:
        df[col] = df[col].astype('str')

    df = df.drop(["num_veh", "Unnamed: 0", "num_acc", "date", "age_group"], axis = 1)

    labels = {
        1: 1, # Indemne
        2: 2, # Deces
        3: 2, # Hospitalisé
        4: 3 # Léger
    }

    st.write("Les colonnes du DataFrame sont :", df.columns.tolist())
    
    # Application du mapping
    df['grav'] = df['grav'].map(labels)

    # On crée une fonction pour transformer nos modalités catégorielle en one hot encoding afin d'alimenter nos modèles.
    def convert_category_to_dummies(X):
        cat_columns = X.select_dtypes(include=['object']).columns
        X_dummies = pd.get_dummies(X[cat_columns], drop_first=True, prefix=cat_columns)
        X_final = pd.concat([X.drop(columns=cat_columns), X_dummies], axis=1)
        return X_final

    df = convert_category_to_dummies(df)
    # On définit nos variables explicatives et la target de notre modèle.
    X = df.drop("grav", axis = 1)
    y = df.grav

    # On sépare nos données en set d'entrainement, et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    # Features selection issues de la méthode SelectFromModel avec random forest
    X_train_sfm_1 = X_train[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_1.0', 'trajet_4.0', 'trajet_5.0', 'choc_1.0', 'manv_1.0', 'catr_3.0', 'agg_2']]
    X_test_sfm_1 = X_test[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_1.0', 'trajet_4.0', 'trajet_5.0', 'choc_1.0', 'manv_1.0', 'catr_3.0', 'agg_2']]

    X_train_sfm_2 = X_train[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_4.0', 'trajet_5.0', 'catr_3.0', 'agg_2']]
    X_test_sfm_2 = X_test[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_4.0', 'trajet_5.0', 'catr_3.0', 'agg_2']]

    
    # Ces variables proviennent d'une feature selection que nous avions faites lorsque nous avions regroupé les moodalités de la variable target différemment. Méthode utilisée Selectkbest
    X_train_k60 = X_train[['age', 'place_1.0', 'place_2.0', 'catu_2', 'catu_3', 'sexe_2', 'trajet_2.0', 'trajet_4.0', 'trajet_5.0', 'locp_0.0', 'locp_1.0', 'locp_2.0', 'locp_3.0', 'locp_4.0', 'actp_0.0', 'actp_1.0', 'actp_3.0', 'etatp_0.0', 'etatp_1.0', 'etatp_2.0', 'senc_1.0', 'catv_33', 'obs_0.0', 'obs_13.0', 'obs_2.0', 'obs_6.0', 'obs_8.0', 'obsm_0.0', 'obsm_2.0', 'choc_4.0', 'manv_13.0', 'manv_2.0', 'manv_23.0', 'catr_3.0', 'catr_4.0', 'circ_1.0', 'circ_2.0', 'prof_0.0', 'prof_1.0', 'plan_1.0', 'plan_2.0', 'plan_3.0', 'situ_1.0', 'situ_3.0', 'lum_3', 'agg_2', 'int_1', 'int_3', 'col_2.0', 'col_3.0', 'col_4.0', 'col_5.0', 'col_6.0', 'col_7.0', 'com_55', 'dep_130', 'dep_750', 'dep_910', 'dep_920', 'dep_940']]
    X_test_k60 = X_test[['age', 'place_1.0', 'place_2.0', 'catu_2', 'catu_3', 'sexe_2', 'trajet_2.0', 'trajet_4.0', 'trajet_5.0', 'locp_0.0', 'locp_1.0', 'locp_2.0', 'locp_3.0', 'locp_4.0', 'actp_0.0', 'actp_1.0', 'actp_3.0', 'etatp_0.0', 'etatp_1.0', 'etatp_2.0', 'senc_1.0', 'catv_33', 'obs_0.0', 'obs_13.0', 'obs_2.0', 'obs_6.0', 'obs_8.0', 'obsm_0.0', 'obsm_2.0', 'choc_4.0', 'manv_13.0', 'manv_2.0', 'manv_23.0', 'catr_3.0', 'catr_4.0', 'circ_1.0', 'circ_2.0', 'prof_0.0', 'prof_1.0', 'plan_1.0', 'plan_2.0', 'plan_3.0', 'situ_1.0', 'situ_3.0', 'lum_3', 'agg_2', 'int_1', 'int_3', 'col_2.0', 'col_3.0', 'col_4.0', 'col_5.0', 'col_6.0', 'col_7.0', 'com_55', 'dep_130', 'dep_750', 'dep_910', 'dep_920', 'dep_940']]

    #model_rf_sfm_2_best = joblib.load('models/model_rf_sfm_2_best.joblib')
    
    # Partie présentation des résultats pour différents types de modèles
    data1 = {
    'Modèle': ['Xgboost brut', 'Random forest brut', 'Lightgbm brut'],
    'Accuracy': [0.60 , 0.63, 0.59],
    'Recall': [0.57, 0.61, 0.56],
    'F1 Score': [0.58, 0.62, 0.57]
    }

    df1 = pd.DataFrame(data1)
    df1 = df1.set_index('Modèle')

    st.write("## Comparaison de différents type de modèles bruts")
    st.dataframe(df1)

    # Deuxième tableau : Comparaison des modèles avec sélection de caractéristiques
    data2 = {
        'Modèle': [
            'Random forest brut',
            'Random forest avec Features selection "SKB" - 60 features',
            'Random forest avec Features selection "SFM" - seuil (0.01)',
            'Random forest avec Features selection "SFM" - seuil (0.00925)',
            'Random forest avec Features selection "SFM" - seuil (0.00925) - meilleurs paramètres'
        ],
        'Accuracy': [0.60, 0.68, 0.72, 0.846, 0.849],
        'Recall': [0.61, 0.67, 0.71, 0.835, 0.838],
        'F1 Score': [0.62, 0.67, 0.71, 0.839, 0.840]
    }

    df2 = pd.DataFrame(data2)
    df2 = df2.set_index('Modèle')

    st.write("## Comparaison des différentes phases d'optimisation du Random Forest")
    st.dataframe(df2)
