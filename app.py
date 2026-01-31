import streamlit as st
import random
from PIL import Image

# 1. Configurare & Design Dark
st.set_page_config(page_title="HERCULE AI - DJ VIZUAL", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    iframe { border-radius: 15px; border: 2px solid #ff0000; background-color: black; }
    </style>
    """, unsafe_allow_html=True)

if "yt_search" not in st.session_state:
    st.session_state.yt_search = "trending music"

st.title("🎧 HERCULE AI - Player Negru")
st.write("Analiză automată culori -> Predicție directă melodie")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        # REPARARE EROARE: Convertim în RGB pentru a elimina canalul Alpha (transparența)
        img = Image.open(sursa).convert('RGB') 
        st.image(img, width=300)
        
        with st.spinner('Prezic melodia...'):
            # ANALIZĂ PIXELI (Acum merge pe orice format)
            img_small = img.resize((1, 1))
            r, g, b = img_small.getpixel((0, 0))
            
            # LOGICĂ PREDICȚIE DIRECTĂ (Artist - Piesă)
            if r > g and r > b:
                artist_piesa = "AC/DC - Highway to Hell"
            elif g > r and g > b:
                artist_piesa = "Bob Marley - Three Little Birds"
            elif b > r and b > g:
                artist_piesa = "Billie Eilish - Ocean Eyes"
            elif (r + g + b) > 500:
                artist_piesa = "Pharrell Williams - Happy"
            elif (r + g + b) < 200:
                artist_piesa = "The Weeknd - Blinding Lights"
            else:
                artist_piesa = "Dua Lipa - Levitating"

            st.markdown(f"### 🤖 Predicție Reală: `{artist_piesa}`")
            st.session_state.yt_search = artist_piesa

with col2:
    st.subheader("📺 YouTube Auto-Play")
    # Căutare automată pe baza predicției
    search_term = st.session_state.yt_search.replace(' ', '+')
    yt_url = f"https://www.youtube.com/embed?listType=search&list={search_term}&autoplay=1"
    
    st.markdown(
        f'<iframe width="100%" height="380" src="{yt_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )

st.success(f"Muzica rulează pentru: {st.session_state.yt_search}")
