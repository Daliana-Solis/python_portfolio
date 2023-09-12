import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/me_photo.jpg")


with col2:
    st.title("Daliana Solis Solis")

    me_descript = """
    I am Daliana S. Solis, a recent graduated from the University of California, Irvine (UCI) with a degree in Informatics,specializing in Human-Computer Interaction, and a minor in Health Informatics. 
    Throughout my academic journey, I developed a deep interest in the fields of product management and data analysis. 
    I've had the opportunity to further explore these interests through various projects and an internship which can be seen here and on my Wix website. 
    
    """
    st.info(me_descript)
