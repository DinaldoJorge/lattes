import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("star.png")

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 40px;">
            <a href="https://starlink.com/" target="_blank">
                <img src="data:image/png;base64,{img_base64}" 
                     width="300" 
                     style="border-radius:10px; margin-bottom:20px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# ABAIXO
col_left, col_right = st.columns([2,1])

with col_left:
    st.markdown("<div style='margin-bottom:15px; font-size:22px;'><b>Nome Dinaldo Jorge</b></div>", unsafe_allow_html=True)

    # subcolunas (imagem + texto)
    subcol1, subcol2 = st.columns([1,3])

    with subcol1:
        st.image("teste.png")

    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 18px;
            line-height: 1.6;
        ">
            <b>Sobre Dinaldo:</b><br><br>

            Dinaldo Jorge, 49 anos, é um profissional experiente na área de sistemas de telecomunicações, destacando-se pela sólida formação técnica e expertise em infraestrutura de rede, conectividade e suporte de TI.<br><br>

            Com vasta vivência no mercado, busca posições que exijam soluções inovadoras em redes, segurança digital e administração de sistemas.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:20px;'>", unsafe_allow_html=True)
    st.link_button("Acessar", "http://lattes.cnpq.br/4494611683890258")
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.empty()
