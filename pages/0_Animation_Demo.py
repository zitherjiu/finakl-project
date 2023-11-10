# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#from io import BytesIO
import streamlit as st
import pandas as pd
#from matplotlib import pyplot as plt
import seaborn as sns
#import numpy as np
#import requests




df = pd.read_csv("D:\MISY\Homework\Assignment\\Cleaned_DS_Jobs.csv")



# 设置网页标题
st.title('Final Project:  Analysis based on dataset Data Science Job Posting on Glassdoor')

col1, col2,col3 = st.columns([10,20,10]) 
with col1:
    st.subheader('Things about the dataset:')
    button_click = st.button('Click Me')
    if button_click:
       st.write("This is a dataset of data science job posts in glassdoor and the data inside was scrapped from glassdoor's website.")
       st.write("There are two versions of the data, one is uncleaned and another one is cleaned and the version we downloaded is a cleaned version. Web scrapping, Data cleaning & EDA code are added in the code section.")
with col3:
    st.subheader('Things about the app:')
    button_click = st.button('Click Here')
    if button_click:
        st.write("""Our app is mainly focus on the connections between different variables in the dataset. Our app can be divided into three major parts.""") 
                    
        st.write("""In the first part, We focus our analysis on counting and comparing the number of Different Job Types and Different Onerships in Data Science, mainly using bar charts to display the data.""")
                    
        st.write("""In the second part, we analyze the salary and its related influencing factors. In this part, we use bar chart and heatmap to show data and correlation between variables.""")
                    
        st.write("""In the thrid part, we analyzed the relationship between ranking and company age and size. Since we noticed some data on skills and our major is information management, we also do some research on different programming skills which surprisingly shows that python is an very useful skill.""")

with col2:
    url = "https://img0.baidu.com/it/u=125858522,2865179145&fm=253&fmt=auto&app=138&f=JPEG?w=777&h=500"
    st.image(url)
    

#col3,col4 = st.columns([30,30])

#col5,col7,col6 = st.columns([10,20,10])


#with col6:
    button_click = st.button('ReadMe')
    if button_click:
        st.write("""For the final project, we downloaded a clean_Data Science_job table for the recommend webiste(www.kaggle.com) and the format of this table is .csv
                There are 660 data in this table. Since it's a cleaned dataset, it contains 10 variables, which are: Job Title, Salary Estimate, Job Description, Rating, Company Name, Location, Headquarters, Size, Type of ownership and Industry""")
