import streamlit as st

# CONFIGURAÇÃO
st.set_page_config(page_title="Perfil", layout="wide")

# CSS para deixar a imagem clicável
st.markdown("""
<style>
.link-img {
    display: flex;
    justify-content: center;
}
.link-img a {
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# TOPO (imagem centralizada + link)
col_top1, col_top2, col_top3 = st.columns([1,2,1])

with col_top2:
    st.markdown('<div class="link-img">', unsafe_allow_html=True)
    
    # imagem normal (garante que carrega)
    st.image("star.png", width=300)
    
    # botão invisível abaixo (funciona como link)
    st.link_button("🔗 Acessar Starlink", "https://starlink.com/")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ABAIXO
col1, col2 = st.columns([1,2])

with col1:
    st.write("Nome Dinaldo Jorge")
    st.image("teste.png")
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")

with col2:
    st.empty()
