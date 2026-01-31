import streamlit as st
import random
from PIL import Image

# 1. DESIGN DARK (Player Negru) & Configurare
st.set_page_config(page_title="HERCULE AI - DARK PLAYER", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 15px; border: 2px solid #1ed760; background-color: black; }
    </style>
    """, unsafe_allow_html=True)

# Starea pentru predicția curentă
if "yt_search" not in st.session_state:
    st.session_state.yt_search = "trending music"

st.title("🎧 HERCULE AI - Player Negru")
st.write("Analiză haine & față -> Predicție directă melodie -> Auto-Play")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    # Take Photo & Upload
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa)
        st.image(img, width=300)
        
        with st.spinner('Prezic melodia după culori...'):
            # ANALIZĂ PIXELI (Haine și Față)
            img_small = img.resize((1, 1))
            r, g, b = img_small.getpixel((0, 0))
            
            # LOGICĂ PREDICȚIE DIRECTĂ (Artist - Piesă)
            # Sistemul alege o combinație bazată pe valorile RGB detectate
            if r > g and r > b:
                artist_piesa = "AC/DC - Highway to Hell"
            elif g > r and g > b:
                artist_piesa = "Bob Marley - Three Little Birds"
            elif b > r and b > g:
                artist_piesa = "Billie Eilish - Ocean Eyes"
            elif (r + g + b) > 600:
                artist_piesa = "Pharrell Williams - Happy"
            elif (r + g + b) < 150:
                artist_piesa = "The Weeknd - Blinding Lights"
            else:
                artist_piesa = "Dua Lipa - Levitating"

            st.markdown(f"### 🤖 Predicție Reală: `{artist_piesa}`")
            st.session_state.yt_search = artist_piesa

with col2:
    st.subheader("📺 Player Auto-Play")
    # Playerul negru setat pe căutare automată după predicție
    # listType=search aduce direct rezultatul cel mai bun
    yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.yt_search.replace(' ', '+')}&autoplay=1"
    
    st.markdown(
        f'<iframe width="100%" height="380" src="{yt_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )

st.success(f"Muzica pornește pentru: {st.session_state.yt_search}")
