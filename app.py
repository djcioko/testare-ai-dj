import streamlit as st
import random
from PIL import Image

# Configurare aplicație
st.set_page_config(page_title="HERCULE AI - DJ VIZUAL", layout="wide")

# Starea pentru căutarea curentă (Predictia)
if "search_query" not in st.session_state:
    st.session_state.search_query = "trending music"

st.title("⚡ HERCULE AI: DJ Vizual Instant")
st.write("Fă o poză ca să prezic melodia potrivită pentru hainele și starea ta!")

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
        
        with st.spinner('AI-ul prezice melodia după culori...'):
            # ANALIZĂ VIZUALĂ: Citim pixelii pentru a genera o predicție reală
            img_small = img.resize((1, 1))
            rgb = img_small.getpixel((0, 0)) 
            r, g, b = rgb
            
            # LOGICĂ DE PREDICȚIE (Transformăm culorile în genuri muzicale)
            if r > g and r > b:
                vibe = "Energie Roșie / Intens"
                predictie = "Rock Hits 2026"
            elif g > r and g > b:
                vibe = "Vibe Verde / Relaxat"
                predictie = "Chill Lo-Fi Beats"
            elif b > r and b > g:
                vibe = "Stil Albastru / Elegant"
                predictie = "Jazz Piano Classics"
            elif sum(rgb) > 600:
                vibe = "Alb/Luminos / Vesel"
                predictie = "Happy Pop Hits"
            elif sum(rgb) < 150:
                vibe = "Negru/Închis / Street"
                predictie = "Deep Underground Techno"
            else:
                vibe = "Colorat / Mixt"
                predictie = "Top Global Summer Hits"

            st.markdown(f"### 🤖 Analiză Vibe: `{vibe}`")
            st.markdown(f"### 🎵 Melodie Prezisă: **{predictie}**")
            
            # Salvăm predicția pentru player
            st.session_state.search_query = predictie
            st.success("✅ YouTube caută acum melodia!")

with col2:
    st.subheader("📺 YouTube Player")
    # Player care caută AUTOMAT predicția AI-ului
    # Folosim embed de tip search pentru a aduce piesa prezisă
    yt_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.search_query}&autoplay=1"
    
    st.markdown(
        f'<iframe width="100%" height="400" src="{yt_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )

st.info("Sistemul analizează culorile (RGB) din haine și transformă datele în căutare muzicală.")
