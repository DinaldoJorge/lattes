import streamlit as st

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("star.png")



st.image("teste.png")
st.write("Site Lattes")
st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")
