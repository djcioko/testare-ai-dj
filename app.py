import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Design
st.set_page_config(page_title="HERCULE AI - DJ TOTAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 25px #1ed760; }
    .stMarkdown h3 { color: #1ed760; }
    </style>
    """, unsafe_allow_html=True)

if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept analiză..."

# 2. TOATĂ LISTA TA (Căutare prin text - Fără ID-uri care să se blocheze)
TOATA_LISTA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky",
    "Village People - Y.M.C.A.", "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego",
    "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", "Justin Timberlake - Can't Stop The Feeling",
    "Las Ketchup - Asereje", "Los Del Rio - Macarena", "Andra - Iubirea Schimba Tot",
    "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga",
    "HI-Q - Gasca mea", "3 Sud Est - Amintirile", "N&D - Vino la mine",
    "Connect-R - Vara nu dorm", "Smiley - Oarecare", "Vama - Perfect fara tine",
    "AC/DC - Thunderstruck", "AC/DC - Highway to Hell", "Metallica - Nothing Else Matters",
    "Bon Jovi - It's My Life", "Queen - Don't Stop Me Now", "Iris - De vei pleca",
    "Cargo - Daca ploaia s-ar opri", "Phoenix - Andrii Popa", "Holograf - Ti-am dat un inel",
    "Dan Spataru - Drumurile noastre", "Mirabela Dauer - Ioane, Ioane", "Ducu Bertzi - M-am indragostit numai de ea",
    "Gica Petrescu - I-a mai toarna un paharel", "Zdob si Zdup - Moldoveni s-au nascut", "Angela Similea - Sa mori de dragoste ranita",
    "Constantin Enceanu - Stai cu mine omule", "Ionut Dolanescu - M-a facut mama oltean", "Damian & Brothers - In statie la Lizeanu",
    "Puiu Codreanu - Beau de bucurie", "B.U.G. Mafia - Sa Cante Trompetele", "B.U.G. Mafia - Cine e cu noi",
    "Parazitii - In focuri", "Eminem - Lose Yourself", "The Weeknd - Blinding Lights", "50 Cent - In Da Club"
]

st.title("🎰 HERCULE AI - TONOMATUL CARE NU SE BLOCHEAZĂ")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        # RULETA - Extrage piesa și pregătește link-ul de căutare
        piesa = random.choice(TOATA_LISTA)
        st.session_state.nume_piesa = piesa
        st.session_state.search_query = urllib.parse.quote(piesa)
        
        st.markdown(f"### 🎵 Melodie Aleasă: **{piesa}**")

with col2:
    st.subheader("📺 YouTube Player")
    
    if st.session_state.search_query:
        # Folosim listType=search pentru a găsi mereu o variantă care merge
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.success(f"Acum rulează: {st.session_state.nume_piesa}")

st.info("Sistemul caută acum piesa prin text, deci nu mai există ID-uri invalide. Orice poză va genera o piesă funcțională!")
