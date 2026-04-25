import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO para converter imagem em base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# converter a imagem
img_base64 = get_base64_image("star.png")

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center;">
            <a href="https://starlink.com/" target="_blank">
                <img src="data:image/png;base64,{img_base64}" width="300" style="border-radius:10px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# ABAIXO
col_left, col_right = st.columns([1,2])

with col_left:
    st.write("Nome Dinaldo Jorge")
    st.image("teste.png")
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")

with col_right:
    st.empty()
