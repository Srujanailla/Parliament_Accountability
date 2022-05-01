# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 00:15:04 2022

@author: hp
"""

import streamlit as st

import pandas as pd
import numpy as np
import re
import missingno as msno
import warnings
warnings.filterwarnings("ignore")

#Visualizations
import plotnine as pn
import seaborn as sns
import matplotlib.pyplot as plt


#WordCloud
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



#Text preprocessing
from sklearn.feature_extraction.text import CountVectorizer

st.title("Parliamentary Members Accountability Dashboard")

tab_selected = st.sidebar.radio("Navigation", ("Election Manifesto Word Clouds","Party Composition", "Question Hour Data Overview", "MP diagnosis" ))

if tab_selected =="Election Manifesto Word Clouds":
    
    with open("C:/Users/hp/Political_accountability_dashboard/BJP_manifesto.txt") as f:
     BJP_manifesto = f.read()
     
     # Create and generate a word cloud image:
     wordcloud = WordCloud().generate(BJP_manifesto)

     # Display the generated image:
     fig= plt.figure(figsize=(40,40))
     ax=plt.axes()
     plt.imshow(wordcloud, interpolation='bilinear')
     plt.axis("off")
     st.pyplot(fig)
    
    
    
    
    
#st.write("""
### Which ministry gets asked the most questions?""")

#dataset_name = st.selectbox("Filter on ministries who are:", ("flooded with questions", "Not really")) 


#data = pd.read_csv("C:/Users/hp/Desktop/DSPP - GU/Data_Science_II_Spring/Project/Data/rajyasabha_questions_and_answers_2017.csv")

#fig= plt.figure(figsize=(10,8))
#ax=plt.axes()
#plt.rcParams.update({'font.size': 20})
#sns.countplot('ministry', data = data, order = data['ministry'].value_counts().index)
#plt.ylabel('')
#plt.xlabel('')
#ax.set_xticks([])
#st.pyplot(fig)