import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit import components
from data import *

st.set_page_config(
    page_title="Streamlit Dashboard for Nickel Research",
    page_icon="💖",
    layout='wide',
)

with open('style.css') as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown('<h1>Nickel Research Dashboard</h1>', unsafe_allow_html=True)

pages = option_menu("", ['Data', 'Topic Modeling'], 
    icons=['file-earmark-text', 'bag-fill'], default_index=0, orientation="horizontal")

if pages == 'Data':
    col1a, col1b, col1c = st.columns([3,2,3], gap = 'large')
    with col1b:
        opt0 = st.selectbox(label = '**Choose Language**',
                            options = ['Indonesia', 'English'])
        nickel = nickel[nickel['lang'] == opt0]
        opt1 = st.selectbox(label = '**Filter based on:**', 
                            options = ['Title', 'Date', 'Source', 'Year'])
        if opt1  == 'Title':
            opt2 = st.text_input('**Input Keyword:**')
            data = nickel[nickel['title'].apply(lower).str.contains(opt2.lower())==True].dropna()
        else:
            if opt1 == 'Date':
                opt1 = 'date'
                opt_data = date
            elif opt1 == 'Year':
                opt1 = 'Category'
                opt_data = year
            else:
                opt1 = 'source'
                opt_data = source
            opt2 = st.selectbox(label = '**Choose {}:**'.format(opt1),
                                options = opt_data)
            data = nickel[nickel[opt1] == opt2].dropna()
    with st.expander("**Results retrieved :**"):
        st.dataframe(data)
    col2a, col2b, col2c = st.columns([3,2,3], gap = 'large')
    with col2b:
        opt3 = st.selectbox("**Choose news index to be displayed:**", data.index)
    data2 = data.loc[opt3, :]
    with st.container(border = True):
        st.markdown('<h2><b>{}</b></h2>'.format(data2.title), unsafe_allow_html = True)
        st.markdown('<div class="txt2"><b>{} - {}</b></div>'.format(data2.source, data2.date), unsafe_allow_html = True)
        " "
        st.markdown('<div class="txt">{}</div>'.format(data2.text.replace('\n', '<br>')), unsafe_allow_html = True)

else:
    col3a, col3b, col3c, col3d = st.columns([1,2,2,1])
    with col3b:
        opt4 = st.selectbox(label = '**Choose Language**',
                            options = ['Indonesia', 'English'])
    with col3c:
        opt5 = st.selectbox(label = '**Choose Year**',
                            options = ['All', '2020', '2021', '2022', '2023-present']) #set(list(year2) + ['All'])
        
    with open('data/LDA_{}_{}.html'.format(opt4, opt5), 'r') as file:
        html_lda = file.read()
    
    col4a, col4b, col4c = st.columns([1,7,1], gap = 'small')
    with col4b:    
        st.header('Topic Modeling for {} Articles in {} Time'.format(opt4, opt5))
        components.v1.html(html_lda, width=2000, height=1500, scrolling=True)