import streamlit as st
import pandas

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


conte2 = 'Below are some of the Python applications I have worked on.'
st.subheader(conte2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" +row['image'])

        #later add your own URL
        #f"[Source Code]({row['url']})"
        st.write("[Source Code](https://pythonhow.com)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" +row['image'])
        st.write("[Source Code](https://pythonhow.com)")

