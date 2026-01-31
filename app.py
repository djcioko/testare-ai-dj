import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Stil Vizual (Hercule Design)
st.set_page_config(page_title="HERCULE AI - MULTI-DJ", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    
    /* Buton Spotify (Verde) */
    .btn-spotify > a {
        background-color: #1DB954 !important; color: white !important;
        border-radius: 25px !important; padding: 10px !important;
        text-decoration: none; display: block; text-align: center; font-weight: bold;
    }
    
    /* Buton Festify (Portocaliu) */
    .btn-festify > a {
        background-color: #f25c05 !important; color: white !important;
        border-radius: 25px !important; padding: 10px !important;
        text-decoration: none; display: block; text-align: center; font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Memorie sesiune
if "last_capture_time" not in st.session_state:
    st.session_state.last_capture_time = time.time()
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept analiză..."
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# 2. LISTA COMPLETĂ (100+ PIESE)
TOATA_LISTA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky", "Village People - Y.M.C.A.", 
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", 
    "Justin Timberlake - Can't Stop The Feeling", "Las Ketchup - Asereje", "Los Del Rio - Macarena", 
    "Andra - Iubirea Schimba Tot", "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga", 
    "HI-Q - Gasca mea", "3 Sud Est - Amintirile", "N&D - Vino la mine", "Connect-R - Vara nu dorm", 
    "Smiley - Oarecare", "Vama - Perfect fara tine", "AC/DC - Thunderstruck", "AC/DC - Highway to Hell", 
    "Metallica - Nothing Else Matters", "Bon Jovi - It's My Life", "Queen - Don't Stop Me Now", 
    "Iris - De vei pleca", "Cargo - Daca ploaia s-ar opri", "Phoenix - Andrii Popa", "Holograf - Ti-am dat un inel",
    "Dan Spataru - Drumurile noastre", "Mirabela Dauer - Ioane, Ioane", "Ducu Bertzi - M-am indragostit numai de ea", 
    "Gica Petrescu - I-a mai toarna un paharel", "Zdob si Zdup - Moldoveni s-au nascut", 
    "B.U.G. Mafia - Sa Cante Trompetele", "Parazitii - In focuri", "Eminem - Lose Yourself", 
    "The Weeknd - Blinding Lights", "50 Cent - In Da Club", "Whitney Houston - I Will Always Love You"
]

st.title("🎰 HERCULE AI: THE ULTIMATE DJ ENGINE")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual & Timer")
    
    # Timer 2 min
    elapsed = time.time() - st.session_state.last_capture_time
    st.progress(min(elapsed / 120, 1.0), text=f"Timp până la piesa următoare: {int(max(0, 120 - elapsed))}s")
    
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        st.session_state.last_capture_time = time.time()
        img = Image.open(sursa).convert('RGB')
        st.image(img, width=400)
        
        # RULETA
        piesa = random.choice(TOATA_LISTA)
        st.session_state.nume_piesa = piesa
        st.session_state.search_query = urllib.parse.quote(piesa)
        
        st.markdown(f"### 🎵 AI a selectat: **{piesa}**")
        
        # BUTOANELE TALE
        st.markdown(f'<div class="btn-spotify"><a href="https://open.spotify.com/search/{st.session_state.search_query}" target="_blank">🟢 CAUTĂ ÎN SPOTIFY</a></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="btn-festify"><a href="https://festify.us/party/-OMkDNoyn7nohBDBnLWm" target="_blank">🔥 DESCHIDE FESTIFY PARTY</a></div>', unsafe_allow_html=True)

with col2:
    st.subheader("📺 YouTube Player (Auto-Play)")
    
    if st.session_state.search_query:
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.success(f"Acum rulează: {st.session_state.nume_piesa}")

if elapsed >= 120:
    st.warning("⏰ Au trecut 2 minute! Schimbă vibe-ul cu o poză nouă!")
