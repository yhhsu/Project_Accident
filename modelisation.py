import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

df = pd.read_csv("data_preprocessed.csv")

def app():
    st.title("Modélisation")

    df = pd.read_csv("data_preprocessed.csv")
    df = df.drop(["num_veh", "Unnamed: 0", "num_acc", "date", "age_group"], axis = 1)
    df = df[df["annee"] == 2015]
    df.replace('nan', -1, inplace=True)
    df.fillna(-1, inplace = True)

    labels = {
        1: 1, # Indemne
        2: 2, # Deces
        3: 2, # Hospitalisé
        4: 3 # Léger
    }

    # Application du mapping
    df['grav'] = df['grav'].map(labels)

    #K25
    X = df[['place', 'catu', 'sexe', 'trajet', 'locp', 'actp', 'etatp', 'senc', 'occutc', 'obs', 'obsm', 'catr', 'circ', 'plan', 'larrout', 'surf', 'situ', 'hrmn', 'lum', 'agg', 'int', 'atm', 'com', 'dep', 'age']]
    y = df['grav']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    from sklearn.ensemble import RandomForestClassifier
    from xgboost import XGBClassifier
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix
    
    def prediction(classifier):
        if classifier == 'Random Forest':
            clf = RandomForestClassifier(n_estimators = 100, random_state = 42)
        elif classifier == 'SVC':
            clf = SVC()
        elif classifier == 'Logistic Regression':
            clf = LogisticRegression()
        clf.fit(X_train, y_train)
        return clf

    def scores(clf, choice):
        if choice == 'Accuracy':
            return clf.score(X_test, y_test)
        elif choice == 'Confusion matrix':
            return confusion_matrix(y_test, clf.predict(X_test))

    choix = ['Random Forest', 'SVC', 'Logistic Regression']
    option = st.selectbox('Choix du modèle', choix)
    st.write('Le modèle choisi est :', option)

    clf = prediction(option)

    display = st.radio('Que souhaitez-vous montrer ?', ('Accuracy', 'Confusion matrix'))
    if display == 'Accuracy':
        st.write(scores(clf, display))
    elif display == 'Confusion matrix':
        st.dataframe(scores(clf, display))
