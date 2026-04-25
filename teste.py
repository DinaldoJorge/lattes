import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Perfil",
    layout="wide"
)

# TOPO (imagem centralizada e clicável)
col_top1, col_top2, col_top3 = st.columns([1,2,1])

with col_top2:
    st.markdown(
        """
        <div style="text-align: center;">
            <a href="https://starlink.com/" target="_blank">
                <img src="star.png" width="300">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ABAIXO DA IMAGEM (conteúdo lado a lado)
col1, col2 = st.columns([1,2])

with col1:
    st.write("Nome Dinaldo Jorge")
    st.image("teste.png")
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")

with col2:
    st.empty()  # espaço para conteúdo futuro
