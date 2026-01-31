import streamlit as st
import random
import time
from PIL import Image

# 1. Configurare & Design (Revenim la ce a funcționat)
st.set_page_config(page_title="HERCULE AI - DJ VIZUAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    </style>
    """, unsafe_allow_html=True)

# Memorie sesiune
if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM"
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Sistem pregătit!"

# 2. Toată lista ta de melodii cu ID-uri sigure
TOATE_PIESELE = [
    {"nume": "Bruno Mars - Marry You", "id": "OMr9zCvtOfY"},
    {"nume": "Pharrell Williams - Happy", "id": "ZbZSe6N_BXs"},
    {"nume": "Daft Punk - Get Lucky", "id": "5NV6Rdv1a3I"},
    {"nume": "Village People - Y.M.C.A.", "id": "VC_9v-Yv6zI"},
    {"nume": "Taylor Swift - Shake It Off", "id": "nfWlot6h_JM"},
    {"nume": "Michel Telo - Ai se eu te pego", "id": "hcm55lU9knw"},
    {"nume": "Andra - Iubirea Schimba Tot", "id": "W-tP-Y6t1yU"},
    {"nume": "Voltaj - 20 de ani", "id": "mU57v_9u_vY"},
    {"nume": "O-Zone - Dragostea Din Tei", "id": "j_9v_UvF6zI"},
    {"nume": "Zdob si Zdup - Moldoveni s-au nascut", "id": "S1XUOnE66f4"},
    {"nume": "Phoenix - Andrii Popa", "id": "vSInN5_Xv1s"},
    {"nume": "Dan Spataru - Drumurile noastre", "id": "H7I4m8G5zE8"},
    {"nume": "Holograf - Sa nu-mi iei niciodata dragostea", "id": "H8-v_uY8v_A"},
    {"nume": "B.U.G. Mafia - Sa Cante Trompetele", "id": "mE1_v_UvF6U"},
    {"nume": "Enrique Iglesias - Bailando", "id": "b8I-7Wk_Vbc"},
    {"nume": "Don Omar - Danza Kuduro", "id": "7zp1TbLFPp8"},
    {"nume": "Whitney Houston - I Will Always Love You", "id": "3JWTaaS7LdU"},
    {"nume": "AC/DC - Thunderstruck", "id": "v2AC41dglnM"},
    {"nume": "Metallica - Nothing Else Matters", "id": "tAGnKpE4NCI"},
    {"nume": "Ducu Bertzi - M-am indragostit numai de ea", "id": "S-O6v-YhG0I"}
]

st.title("🎰 HERCULE AI - DJ-ul Tău Personal")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    
    if foto:
        img = Image.open(foto).convert('RGB')
        st.image(img, width=400)
        
        # Mixare și alegere la fiecare poză nouă
        piesa = random.choice(TOATE_PIESELE)
        st.session_state.yt_id = piesa['id']
        st.session_state.nume_piesa = piesa['nume']
        
        # Afișăm denumirea sub poză
        st.markdown(f"### 🎵 Melodie: **{piesa['nume']}**")

with col2:
    st.subheader("📺 YouTube Player")
    
    # URL forțat cu cheie unică să se schimbe la fiecare poză
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1&mute=0"
    
    st.markdown(
        f'<iframe key="{st.session_state.yt_id}_{time.time()}" width="100%" height="400" src="{yt_url}" '
        f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    st.success(f"Acum rulează: {st.session_state.nume_piesa}")
