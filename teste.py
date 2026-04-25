import streamlit as st

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("star.png")

with col1:
    st.write("Nome Dinaldo Jorge Guedes Santos")

with col1: 
    st.image("teste.png")

st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")
