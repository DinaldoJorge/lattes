import streamlit as st

# TOPO (imagem centralizada)
col_top1, col_top2, col_top3 = st.columns([1,2,1])
with col_top2:
    st.image("star.png")

# ABAIXO DA IMAGEM (conteúdo lado a lado)
col1, col2 = st.columns([1,2])

with col1:
    st.write("Nome Dinaldo Jorge")
    st.image("teste.png")
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")

with col2:
    st.empty()  # pode colocar algo aqui depois
