import streamlit as st 
from constant import *
import numpy as np 
import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import plotly.express as px
import plotly.figure_factory as ff
import requests
import re
import plotly.graph_objects as go
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(page_title='yuri zhang\'s portfolio' ,layout="wide",page_icon='👩‍🔬') 


with st.sidebar:
        components.html(embed_component['linkedin'],height=310)

st.subheader('About Me')
st.write(info['Brief'])

st.subheader('Career snapshot')

    
with st.spinner(text="Building line"):
    with open('mytimeline.json', "r") as f:
        data = f.read()
        timeline(data, width=900)


st.subheader('Skills & Tools ⚒️')
def skill_tab():
    rows,cols = len(info['skills'])//skill_col_size,skill_col_size
    skills = iter(info['skills'])
    if len(info['skills'])%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab()


#st.subheader('Education 📖')

#fig = go.Figure(data=[go.Table(
#    header=dict(values=list(info['edu'].columns),
#                fill_color='royalblue',
#                align='left',height=40,
#                font_size=20),
#    cells=dict(values=info['edu'].transpose().values.tolist(),
#               align='left',height=50,fill_color='lightsteelblue',font_size=16))])

#fig.update_layout(width=900, height=500)
#st.plotly_chart(fig)

st.subheader('Tableau BI Projects 📊')
#st.markdown("""<a href={}> access full profile here</a>""".format(info['tableau']),unsafe_allow_html=True)

st.markdown('<h5><u>Supplier Scorecard</h5>',unsafe_allow_html=True)
st.caption('work sample with Dummy Data')
with st.expander('read data viz sample below'):
    components.html(embed_component['tableau'],height=800)


st.markdown('<h5><u>NIHR Research Award Analysis</h5>',unsafe_allow_html=True)
st.caption('BI Analytics Interview Task')
with st.expander('read data viz sample below'):
    components.html(embed_component['tableau_2'],height=1000)




st.subheader('Data Analytics Projects 📝')
        
def paper_summary(index):
    st.markdown('<h5><u>'+paper_info['name'][index]+'</h5>',unsafe_allow_html=True)
    st.caption(paper_info['role'][index])
    st.caption(paper_info['type'][index]+', '+paper_info['tool'][index]+', '+paper_info['year'][index])
    with st.expander('detailed description'):
        with st.spinner(text="Loading details..."):
                st.write(paper_info['Summary'][index])
                pdfFileObj = open('pdfs/{}'.format(paper_info['file'][index]), 'rb')
                st.download_button('download report/presentation',pdfFileObj,file_name=paper_info['file'][index],mime='pdf')
    


paper_summary(0)
paper_summary(1)
paper_summary(2)
paper_summary(3)

st.subheader('Awards and Scholarship 🥇')
achievement_list = ''.join(['<li>'+item+'</li>' for item in info['achievements']])
st.markdown('<ul>'+achievement_list+'</ul>',unsafe_allow_html=True)


#st.sidebar.caption('Wish to connect?')
st.sidebar.subheader('Contact')
st.sidebar.caption('Email')
st.sidebar.write('📧: zhangyushuangzi@outlook.com')
st.sidebar.write('📧: yurizhang0203@gmail.com')

st.sidebar.caption('Linkedin')
st.sidebar.write('👩‍🔬: www.linkedin.com/in/yurizhang99/')

pdfFileObj = open('pdfs/yuri_resume.pdf', 'rb')
st.sidebar.download_button('download resume',pdfFileObj,file_name='yuri_resume.pdf',mime='pdf')

        

        
        
    
    
