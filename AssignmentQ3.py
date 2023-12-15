# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:02:51 2023

@author: kaman
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
    if 'Age' in df.columns and 'Name' in df.columns:
        df["age_range"] = df["Age"] // 10 * 10
        
        # Create bins with a 5-year interval
        bins = np.arange(0, df['Age'].max() + 5, 5)
        
        # Streamlit code to display the histogram
        st.title('Age Distribution')
        st.write('This histogram shows the distribution of ages in 5-year intervals.')
        
        # Plotting the histogram
        fig, ax = plt.subplots()
        ax.hist(df['Age'], bins=bins, edgecolor='black')
        
        ax.set_title('Age Distribution')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        
        # Display the plot
        st.pyplot(fig)
    else:
        st.write("Format of the csv file is incorrect")