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
    # Display the first 10 rows of the dataframe
    st.write("Displaying first 10 rows of the dataset:")
    st.dataframe(df.head(10))
    st.write(f"Dataframe shape: {df.shape}")
        
    # Show statistical summary of the dataframe
    st.write("Summary statistics:")
    st.dataframe(df.describe())
    # Option to display NA values
    if st.checkbox("Afficher les NA"):
        st.write("Missing values in each column:")
        st.dataframe(df.isna().sum())

    # Chart 1
    df_accidents_par_annee = df.groupby('annee').size().reset_index(name='nombre_accidents')
    # Create the figure and line plot
    plt.figure(figsize=(20, 14))
    sns.lineplot(x='annee', y='nombre_accidents', data=df_accidents_par_annee, marker='o')
    # Add a title and labels
    plt.title("Nombre d'accidents de la route en France de 2005 à 2018", fontsize=18)
    plt.ylabel("Nombre d'accidents", fontsize=14)
    plt.xlabel("Années", fontsize=14)
    # Display the plot in Streamlit
    st.pyplot(plt)


    # Chart 2
    # Group by year and severity (grav)
    counts = df.groupby(['annee', 'grav']).size().reset_index(name='count')
    # Pivot the counts to get a table for stacked bar chart
    pivot_counts = counts.pivot_table(index='annee', columns='grav', values='count', fill_value=0)
    # Calculate the ratio of each severity level per year
    pivot_counts_ratio = pivot_counts.div(pivot_counts.sum(axis=1), axis=0)
    # Create a figure
    plt.figure(figsize=(10, 6))
    # Plot the data as a stacked bar chart
    pivot_counts_ratio.plot(kind='bar', stacked=True)
    # Add title and labels
    plt.title("Ratio d'apparition de chaque modalité de gravité par année", fontsize=14)
    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Ratio", fontsize=12)
    plt.legend(title="Gravité")
    # Display the plot in Streamlit
    st.pyplot(plt)


    # Chart 3
    # List of month labels in French
    review_labels = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    # Create the figure
    plt.figure(figsize=(20, 14))
    # Plot the count of accidents by month
    ax = sns.countplot(x="mois", data=df)

    # Set custom x-axis labels for months
    ax.set_xticklabels(review_labels)

    # Add title and labels
    plt.title("Nombre d'accidents par mois", fontsize=18)
    plt.ylabel("Nombre d'accidents", fontsize=14)
    plt.xlabel("Mois", fontsize=14)

    # Display the plot in Streamlit
    st.pyplot(plt)

    # Chart 4
    fig = plt.figure()
    sns.countplot(x = 'grav', data = df)
    st.pyplot(fig)
