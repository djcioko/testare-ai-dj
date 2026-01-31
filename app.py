import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Design Clean
st.set_page_config(page_title="HERCULE AI - TONOMAT", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; background-color: black; }
    .stImage > img { border-radius: 15px; border: 2px solid #555; }
    </style>
    """, unsafe_allow_html=True)

if "query" not in st.session_state:
    st.session_state.query = ""
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = ""

# Lista ta de melodii (Sistemul caută prin text)
LISTA_TOTALA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky",
    "Whitney Houston - I Wanna Dance With Somebody", "Robin Thicke - Blurred Lines",
    "Kaoma - Lambada", "Village People - Y.M.C.A.", "Taylor Swift - Shake It Off",
    "Michel Telo - Ai se eu te pego", "Queen - We Are The Champions",
    "Zdob si Zdup - Moldoveni s-au nascut", "Dan Spataru - Drumurile noastre",
    "B.U.G. Mafia - Sa Cante Trompetele", "Smiley - Oarecare", "Loredana - Zig Zagga",
    "Andra - Iubirea Schimba Tot", "Holograf - Sa nu-mi iei niciodata dragostea"
]

st.title("🎰 HERCULE AI: Tonomat Digital")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Încarcă poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB')
        # Alegem piesa
        if st.session_state.nume_piesa == "" or st.button("🔄 Altă melodie"):
            piesa_aleasa = random.choice(LISTA_TOTALA)
            st.session_state.nume_piesa = piesa_aleasa
            st.session_state.query = urllib.parse.quote(piesa_aleasa)
        
        # Afișăm imaginea și DOAR denumirea sub ea
        st.image(img, width=400)
        st.markdown(f"### 🎵 Melodia detectată: **{st.session_state.nume_piesa}**")

with col2:
    st.subheader("📺 YouTube Auto-Play")
    
    if st.session_state.query:
        # URL de căutare forțat cu mute=0
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )

st.caption("Dacă piesa nu are sunet, dă un click oriunde pe pagină sau pe player pentru a-l activa.")
