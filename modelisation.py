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
    # X_train_sfm_1 = X_train[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_1.0', 'trajet_4.0', 'trajet_5.0', 'choc_1.0', 'manv_1.0', 'catr_3.0', 'agg_2']]
    # X_test_sfm_1 = X_test[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_1.0', 'trajet_4.0', 'trajet_5.0', 'choc_1.0', 'manv_1.0', 'catr_3.0', 'agg_2']]

    # X_train_sfm_2 = X_train[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_4.0', 'trajet_5.0', 'catr_3.0', 'agg_2']]
    # X_test_sfm_2 = X_test[['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_4.0', 'trajet_5.0', 'catr_3.0', 'agg_2']]
    
    # # Ces variables proviennent d'une feature selection que nous avions faites lorsque nous avions regroupé les moodalités de la variable target différemment. Méthode utilisée Selectkbest
    # X_train_k60 = X_train[['age', 'place_1.0', 'place_2.0', 'catu_2', 'catu_3', 'sexe_2', 'trajet_2.0', 'trajet_4.0', 'trajet_5.0', 'locp_0.0', 'locp_1.0', 'locp_2.0', 'locp_3.0', 'locp_4.0', 'actp_0.0', 'actp_1.0', 'actp_3.0', 'etatp_0.0', 'etatp_1.0', 'etatp_2.0', 'senc_1.0', 'catv_33', 'obs_0.0', 'obs_13.0', 'obs_2.0', 'obs_6.0', 'obs_8.0', 'obsm_0.0', 'obsm_2.0', 'choc_4.0', 'manv_13.0', 'manv_2.0', 'manv_23.0', 'catr_3.0', 'catr_4.0', 'circ_1.0', 'circ_2.0', 'prof_0.0', 'prof_1.0', 'plan_1.0', 'plan_2.0', 'plan_3.0', 'situ_1.0', 'situ_3.0', 'lum_3', 'agg_2', 'int_1', 'int_3', 'col_2.0', 'col_3.0', 'col_4.0', 'col_5.0', 'col_6.0', 'col_7.0', 'com_55', 'dep_130', 'dep_750', 'dep_910', 'dep_920', 'dep_940']]
    # X_test_k60 = X_test[['age', 'place_1.0', 'place_2.0', 'catu_2', 'catu_3', 'sexe_2', 'trajet_2.0', 'trajet_4.0', 'trajet_5.0', 'locp_0.0', 'locp_1.0', 'locp_2.0', 'locp_3.0', 'locp_4.0', 'actp_0.0', 'actp_1.0', 'actp_3.0', 'etatp_0.0', 'etatp_1.0', 'etatp_2.0', 'senc_1.0', 'catv_33', 'obs_0.0', 'obs_13.0', 'obs_2.0', 'obs_6.0', 'obs_8.0', 'obsm_0.0', 'obsm_2.0', 'choc_4.0', 'manv_13.0', 'manv_2.0', 'manv_23.0', 'catr_3.0', 'catr_4.0', 'circ_1.0', 'circ_2.0', 'prof_0.0', 'prof_1.0', 'plan_1.0', 'plan_2.0', 'plan_3.0', 'situ_1.0', 'situ_3.0', 'lum_3', 'agg_2', 'int_1', 'int_3', 'col_2.0', 'col_3.0', 'col_4.0', 'col_5.0', 'col_6.0', 'col_7.0', 'com_55', 'dep_130', 'dep_750', 'dep_910', 'dep_920', 'dep_940']]

    #model_rf_sfm_2_best = joblib.load('models/model_rf_sfm_2_best.joblib')
    
    # Partie présentation des résultats pour différents types de modèles


    st.write('''
    ## Pré-requis: Encodage des variables catégorielle. (Méthode: One Hot Encoding)
    
    Avant de commencer la modélisation, il est essentiel de vérifier le type des variables présentes dans le dataset. Les variables catégorielles doivent être encodées de manière appropriée pour être interprétées par les algorithmes de machine learning.
    Nous avons utilisé le "One Hot Encoding" qui est est une méthode couramment utilisée pour transformer les variables catégorielles en un format numérique.
    ''')
    st.code('''
    # Fonction pour encoder les variables catégorielles
    def convert_category_to_dummies(X):
        cat_columns = X.select_dtypes(include = ["object"]).columns
        X_dummies = pd.get_dummies(X[cat_columns], drop_first = True, prefix = cat_columns)
        X_final = pd.concat([X.drop(columns = cat_columns), X_dummies], axis = 1)
        return X_final
    df = convert_category_to_dummies(df)
    ''', language='python')

    
    # Partie 1
    data1 = {
    'Modèle': ['Xgboost brut', 'Random forest brut', 'Lightgbm brut'],
    'Accuracy': [0.60 , 0.63, 0.59],
    'Recall': [0.57, 0.61, 0.56],
    'F1 Score': [0.58, 0.62, 0.57]
    }

    df1 = pd.DataFrame(data1)
    df1 = df1.set_index('Modèle')

    st.write("## 1. Benchmark - Comparaison de différents type de modèles bruts")
    st.dataframe(df1)

    # Partie 2
    st.write("## 2. Feature Selection")
    st.write('''
    Afin d'optimiser l'entrainement de notre modèle, nous devons choisir judicieusement les features à considérer.
    ''')
    st.write('''
    Il existe différentes méthodes pour sélectionner les meilleures features de notre modèle :
    
    - **Sélection manuelle des features :**
      Une sélection à la main des features qui nous semblent les plus importantes (par exemple à partir de notre exercice de datavizualisation). Cependant, au vu de notre niveau d'expertise sur le sujet des accidents, ainsi qu'au vu du nombre de variables et des interactions, cela ne nous semblait pas pertinent.
    
    - **Réduction via une matrice de corrélation :**
      Une sélection ou réduction des features via une matrice de corrélation en regardant les corrélations entre les variables.
    
    - **Utilisation de modèles avancés :**
      Une sélection des features en utilisant des modèles avancés déjà implémentés sur Python (SelectKBest / SelectFromModel).
    ''')
    
    st.image("img/skb_vs_sfm.png", caption="Comparaison SelectKBest vs SelectFromModel", use_column_width=True)

    st.write("### 2.A. Méthode Corrélation")
    st.code('''
    # Code pour la matrice de corrélation des features:
    corr_matrix = df.corr()
    ''', language='python')
    st.image("img/corr_matrix.png", caption="Features Correlation Matrix ", use_column_width=True)
    st.write("Déjà présenté dans la partie 'Data Visualisation'. Nous n'observions pas de forte corrélations donc nous avons décidé de ne pas prendre de décision à ce stade.")

    st.write("### 2.B. Méthode SelectKbest")
    st.write("Nous avons appliqué une features selection avec un selectKbest qui se base sur une analyse univariée des features. Cette méthode est indépendante du modèle selectionné. Afin de faire plusieurs test, on se base sur une sélection de 10 seuils qui vont sélectionner un nombre de feature compris 10 et 100. Puis on lance un modèle avec chaque sélection de features afin de trouver le set de features qui parvient à obtenir la meilleure accuracy.")
    st.image("img/skb.png", caption="Features Selection sfm Lightgbm", use_column_width=True)
    st.write("On remarque que le nombre de features optimal est 60 avec cette méthode, on garde donc ce set de features.")

    st.write("### 2.C. Méthode 2 : SelectFromModel")
    st.write("Nous avons appliqué une features selection avec un SelectFromModel. Pour cette librairie, le modèle selectionné à une importance sur la sélection de features. On le teste donc avec nos 3 modèles brutes. L'idée est de donner une grille de seuil à tester, et sélectionner le set de features qui parvient à obternir les meilleures performances")
    st.write("#### 2.C.1. LightGBM")
    st.image("img/lightgbm_sfm.png", caption="LightGBM - Features Selection SelectFrom Model", use_column_width=True)
    st.write("#### 2.C.2. Xgboost")
    st.image("img/xgboost_sfm.png", caption="XgBoost - Features Selection SelectFrom Model", use_column_width=True)
    st.write("#### 2.C.3. Random Forest")
    st.image("img/rf_sfm.png", caption="Random Forest - Features Selection SelectFrom Model", use_column_width=True)
    st.write("On remarque que pour le xgboost et le lightgbm, l'accuracy décroit lorsque le seuil augmente. Nous n'avons donc pas été capable de trouver un set de features convenable. Cependant, pour le Random Forest, nous avons trouvé un seuil qui sélectionne un set de variable qui ont de bonnes performances.")
    st.markdown('''
    ### **Conclusion de la Feature Selection**
    
    En conclusion de cette partie Feature Selection, nous décidons de sélectionner 3 sets de features :
    
    - **Les 60 features du SelectKBest.**
    - **Les 16 features sélectionnés du seuil (0.01) du SelectFromModel du Random Forest.**
    - **Les 13 features sélectionnés du seuil (0.00925) du SelectFromModel du Random Forest.**
    ''')
    
    st.code('''
    # Assignation des ensembles de features sélectionnées
    X_k60 = X['age', 'place_1.0', 'place_2.0', 'catu_2', 'catu_3', 'sexe_2', 'trajet_2.0', 'trajet_4.0', 'trajet_5.0', 'locp_0.0', 'locp_1.0', 'locp_2.0', 'locp_3.0', 'locp_4.0', 'actp_0.0', 'actp_1.0', 'actp_3.0', 'etatp_0.0', 'etatp_1.0', 'etatp_2.0', 'senc_1.0', 'catv_33', 'obs_0.0', 'obs_13.0', 'obs_2.0', 'obs_6.0', 'obs_8.0', 'obsm_0.0', 'obsm_2.0', 'choc_4.0', 'manv_13.0', 'manv_2.0', 'manv_23.0', 'catr_3.0', 'catr_4.0', 'circ_1.0', 'circ_2.0', 'prof_0.0', 'prof_1.0', 'plan_1.0', 'plan_2.0', 'plan_3.0', 'situ_1.0', 'situ_3.0', 'lum_3', 'agg_2', 'int_1', 'int_3', 'col_2.0', 'col_3.0', 'col_4.0', 'col_5.0', 'col_6.0', 'col_7.0', 'com_55', 'dep_130', 'dep_750', 'dep_910', 'dep_920', 'dep_940']
    X_sfm_1 = ['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_1.0', 'trajet_4.0', 'trajet_5.0', 'choc_1.0', 'manv_1.0', 'catr_3.0', 'agg_2']
    X_sfm_2 = ['lartpc', 'larrout', 'mois', 'jour', 'hrmn', 'age', 'place_1.0', 'sexe_2', 'trajet_0.0', 'trajet_4.0', 'trajet_5.0', 'catr_3.0', 'agg_2']
    ''', language='python')
    
    # Partie 3
    # Deuxième tableau : Comparaison des modèles avec sélection de caractéristiques
    data2 = {
        'Modèle': [
            'Random forest brut',
            'Random forest avec Features selection "SKB" - 60 features',
            'Random forest avec Features selection "SFM" - seuil (0.01)',
            'Random forest avec Features selection "SFM" - seuil (0.00925)',
            'Random forest avec Features selection "SFM" - seuil (0.00925) - meilleurs paramètres (GridSearch)'
        ],
        'Accuracy': [0.60, 0.68, 0.72, 0.846, 0.849],
        'Recall': [0.61, 0.67, 0.71, 0.835, 0.838],
        'F1 Score': [0.62, 0.67, 0.71, 0.839, 0.840]
    }

    df2 = pd.DataFrame(data2)
    df2 = df2.set_index('Modèle')

    st.write("## 3. Comparaison des différentes phases d'optimisation du Random Forest")
    
    st.markdown('''
    Au cours de notre projet, nous avons testé de plusieurs modèles (Xgboost, LightGBM, Random Forest, SVM) et avons essayé d'apporter différents types d'optimisation (GridSearch, SMOTE):
    - **XGBoost - Optimization des paramètres du modèle + Réechantillonage avec SMOTE**
    - **LightGBM - Optimization des paramètres du modèle + Réechantillonage avec SMOTE**
    - **Random Forest - Réechantillonage avec SMOTE**
    ''')
    st.write("Cependant nous avons décidé de ne présenter que le Random Forest qui est le modèle le plus performant pour notre problèmatique. A l'aide d'optimisation, voici l'évolution des performances que nous avons réussi à atteindre:")
    st.dataframe(df2)

    st.write("Sur notre ensemble de test, nous terminons avec cette matrice de confusion reflétant notre Accuracy")
    
    st.header("Matrices de Confusion reflétant notre Accuracy sur l'ensemble de Test")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Afficher Matrice en Nombre"):
            st.image(
                "img/matrice_confusion_nombre.png",
                caption="Matrice de confusion de l'accuracy (en nombre de cas)",
                use_column_width=True
            )
    
    with col2:
        if st.button("Afficher Matrice en Pourcentage"):
            st.image(
                "img/matrice_confusion_pourcentages.png",
                caption="Matrice de confusion de l'accuracy (en %)",
                use_column_width=True
            )
    
