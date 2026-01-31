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

# Baza de date cu ID-uri reale pentru pornire instantanee
if "yt_id" not in st.session_state:
    st.session_state.yt_id = "v2H4l9RpkwM"
if "nume_piesa" not in st.session_state:
    st.session_state.nume_piesa = "Aștept analiză..."

st.title("🎧 HERCULE AI - Player Negru")
st.write("Analiză automată -> Predicție directă -> YouTube Auto-Play")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză")
    upload = st.file_uploader("Sau încarcă o poză", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        # Reparare eroare RGB
        img = Image.open(sursa).convert('RGB') 
        st.image(img, width=300)
        
        with st.spinner('Prezic melodia...'):
            img_small = img.resize((1, 1))
            r, g, b = img_small.getpixel((0, 0))
            
            # LOGICĂ PREDICȚIE CU ID-URI REALE (Pentru a nu rămâne playerul negru)
            if r > g and r > b:
                piesa = {"nume": "AC/DC - Highway to Hell", "id": "l482T0yNkeo"}
            elif g > r and g > b:
                piesa = {"nume": "Bob Marley - Three Little Birds", "id": "HNBCVM4KbUM"}
            elif b > r and b > g:
                piesa = {"nume": "Billie Eilish - Ocean Eyes", "id": "viimfQi_pUw"}
            elif (r + g + b) > 500:
                piesa = {"nume": "Pharrell Williams - Happy", "id": "ZbZSe6N_BXs"}
            elif (r + g + b) < 200:
                piesa = {"nume": "The Weeknd - Blinding Lights", "id": "4NRXx6U8ABQ"}
            else:
                piesa = {"nume": "Dua Lipa - Levitating", "id": "TUVcZfQe-Kw"}

            st.markdown(f"### 🤖 Predicție Reală: `{piesa['nume']}`")
            st.session_state.yt_id = piesa['id']
            st.session_state.nume_piesa = piesa['nume']

with col2:
    st.subheader("📺 YouTube Auto-Play")
    # Folosim ID direct pentru a forța playerul să încarce piesa, nu căutarea
    yt_url = f"https://www.youtube.com/embed/{st.session_state.yt_id}?autoplay=1&mute=0"
    
    # Truc: Schimbăm cheia iframe-ului ca Streamlit să îl reîncarce forțat la fiecare poză
    st.markdown(
        f'<iframe key="{st.session_state.yt_id}" width="100%" height="380" src="{yt_url}" '
        f'frameborder="0" allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    st.success(f"Acum cântă: {st.session_state.nume_piesa}")
