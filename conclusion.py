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
    st.write("### Bilan")
    st.write('''
    Notre contribution principale dans l’atteinte des objectifs du projet a été centrée 
    sur l’optimisation et l’évaluation des modèles prédictifs. Ceci constituait un rôle clé 
    dans l’analyse exploratoire des données, identifiant les tendances et les corrélations 
    cruciales pour la modélisation. Depuis la dernière itération, nous n’avons pas 
    modifié le modèle utilisé, car le modèle Random Forest s’est avéré être le plus 
    performant avec un taux de précision de 84% et un rappel de 76%. Surtout pour le 
    taux de prédiction de la classe “décédé” a atteint 69%, un résultat significatif 
    compte tenu des défis posés par la nature déséquilibrée des données.
    ''')
    st.write('''
    Les résultats obtenus avec le modèle Random Forest ont surpassé nos attentes 
    initiales et se sont avérés supérieurs aux benchmarks établis. Le modèle a 
    démontré une capacité robuste à prédire la gravité des accidents, avec des 
    métriques de performance élevées en termes de précision et de rappel. Comparé 
    aux benchmarks, notre modèle a montré une amélioration notable, 
    particulièrement dans la prédiction des cas les plus graves, ce qui est crucial pour 
    les applications pratiques du modèle.
    ''')
    st.write('''
    Pour chacun des objectifs du projet, nous avons atteint des résultats significatifs. Le 
    nettoyage et la préparation des données ont permis de créer un jeu de données 
    propre et exploitable. L’analyse exploratoire des données a révélé des insights 
    précieux sur les facteurs influençant la gravité des accidents. Le développement et 
    l’optimisation du modèle Random Forest ont conduit à des performances élevées, 
    validées par des métriques rigoureuses. En termes d’intégration et de 
    déploiement, le modèle est prêt à être utilisé dans des processus métiers tels que 
    l’optimisation de la prise en charge médicale des accidents et l’ajustement des 
    tarifs d’assurance.
    ''')
    st.write('''
    Pour augmenter les performances de notre modèle, nous suggérons d’explorer des 
    techniques de traitement des données déséquilibrées, telles que le 
    suréchantillonnage des classes minoritaires ou l’utilisation de méthodes de 
    pondération. De plus, l’intégration de nouvelles variables explicatives pourrait 
    améliorer la précision des prédictions. Notre projet a contribué à un accroissement 
    de la connaissance scientifique en identifiant les facteurs clés influençant la gravité 
    des accidents et en démontrant l’efficacité des modèles de machine learning dans 
    ce domaine. Les résultats obtenus seront partagés avec la communauté 
    scientifique pour encourager des recherches futures et des applications pratiques. 
    ''')
