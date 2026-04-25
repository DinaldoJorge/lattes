import streamlit as st

col1, col2, col3 = st.columns([1,2,1])

# CENTRO (logo)
with col2:
    st.image("star.png")

# ESQUERDA (nome + imagem + botão)
with col1:
    st.write("Nome Dinaldo Jorge Guedes Santos")
    st.image("teste.png")
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")
