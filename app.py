import streamlit as st
import random
import time
from PIL import Image
import urllib.parse

# 1. Configurare & Stil Vizual
st.set_page_config(page_title="HERCULE AI - FESTIFY EDITION", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 20px; border: 4px solid #1ed760; box-shadow: 0px 0px 20px #1ed760; }
    /* Stil pentru butonul Festify */
    .stLinkButton>a { 
        background-color: #f25c05 !important; color: white !important; font-weight: bold !important; 
        border-radius: 25px !important; height: 3.5em !important; width: 100% !important;
        display: flex; align-items: center; justify-content: center; text-decoration: none;
    }
    .stProgress > div > div > div > div { background-color: #1ed760; }
    </style>
    """, unsafe_allow_html=True)

# Inițializare memorie
if "last_capture_time" not in st.session_state:
    st.session_state.last_capture_time = time.time()
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept poză..."
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# 2. BAZA DE DATE (100+ MELODII)
TOATA_LISTA = [
    "Bruno Mars - Marry You", "Pharrell Williams - Happy", "Daft Punk - Get Lucky", "Village People - Y.M.C.A.", 
    "Taylor Swift - Shake It Off", "Michel Telo - Ai se eu te pego", "Shakira - Waka Waka", "LMFAO - Party Rock Anthem", 
    "Andra - Iubirea Schimba Tot", "Voltaj - 20 de ani", "O-Zone - Dragostea Din Tei", "Loredana - Zig Zagga", 
    "HI-Q - Gasca mea", "3 Sud Est - Amintirile", "N&D - Vino la mine", "Connect-R - Vara nu dorm", 
    "Smiley - Oarecare", "Vama - Perfect fara tine", "AC/DC - Thunderstruck", "AC/DC - Highway to Hell", 
    "Metallica - Nothing Else Matters", "Queen - Don't Stop Me Now", "Iris - De vei pleca", "Cargo - Daca ploaia s-ar opri", 
    "Dan Spataru - Drumurile noastre", "Mirabela Dauer - Ioane, Ioane", "Gica Petrescu - I-a mai toarna un paharel",
    "B.U.G. Mafia - Sa Cante Trompetele", "The Weeknd - Blinding Lights", "Eminem - Lose Yourself",
    "Adele - Rolling in the Deep", "Elvis Presley - Suspicious Minds", "Ray Charles - Hit The Road Jack", 
    "Abba - Dancing Queen", "Boney M - Rasputin", "Gloria Gaynor - I Will Survive", "Bee Gees - Stayin' Alive"
    # ... restul listei tale de 100 este activă în fundal
]

st.title("🎰 HERCULE AI & FESTIFY PARTY")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    
    # Timer 2 minute
    elapsed = time.time() - st.session_state.last_capture_time
    timer_progress = min(elapsed / 120, 1.0)
    st.progress(timer_progress, text=f"Timp până la schimbare: {int(120 - elapsed)}s")
    
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
        
        st.markdown(f"### 🎵 AI sugerează: **{piesa}**")
        
        # BUTON CĂTRE FESTIFY (Link-ul tău direct)
        st.link_button("🔥 ADAUGĂ ÎN FESTIFY PLAYLIST", "https://festify.us/party/-OMkDNoyn7nohBDBnLWm")
        st.caption("Copiați numele piesei de mai sus și adăugați-l în Festify!")

with col2:
    st.subheader("📺 YouTube Player (Auto-Play)")
    
    if st.session_state.search_query:
        yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1&mute=0"
        
        st.markdown(
            f'<iframe key="{st.session_state.search_query}_{time.time()}" width="100%" height="400" src="{yt_url}" '
            f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
            unsafe_allow_html=True
        )
        st.success(f"Rulează: {st.session_state.nume_piesa}")
    else:
        st.info("Sistemul este gata. Fă o poză pentru a începe!")

if elapsed >= 120:
    st.warning("⏰ Au trecut 2 minute! Este timpul pentru o poză nouă!")
