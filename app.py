import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

# 1. CONFIGURARE PAGINĂ & API
st.set_page_config(page_title="HERCULE AI - PURE VISION", layout="wide")

# Introdu cheia ta Gemini în Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("⚠️ Te rog adaugă GEMINI_API_KEY în Streamlit Secrets!")

# 2. MEMORIE PERSISTENTĂ
LOG_FILE = "hercule_history.txt"
if "istoric" not in st.session_state:
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            st.session_state.istoric = [l.strip() for l in f.readlines()[::-1][:5]]
    else:
        st.session_state.istoric = []

if "yt_query" not in st.session_state:
    st.session_state.yt_query = "trending music 2026"

st.title("⚡ HERCULE AI: Predicție Reală prin Imagine")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Senzor Vizual")
    foto = st.camera_input("Fă o poză (Camera Web)")
    upload = st.file_uploader("Sau încarcă o fotografie", type=['jpg', 'png', 'jpeg'])
    
    sursa = foto if foto else upload

    if sursa:
        img = Image.open(sursa)
        st.image(img, width=300, caption="Analiză AI în timp real...")
        
        # 3. ANALIZĂ REALĂ GEMINI (Haine, Culori, Față)
        with st.spinner('AI-ul „citește” stilul tău...'):
            prompt = """
            Analizează această imagine. Uită-te la culorile hainelor, stilul vestimentar și expresia feței. 
            Pe baza acestora, generează DOAR numele unei piese muzicale celebre și artistul care s-ar potrivi perfect (ex: 'Nume Piesa - Artist'). 
            Nu scrie alt text.
            """
            response = model.generate_content([prompt, img])
            predictie_muzicala = response.text.strip()

            # AFIȘARE REZULTAT AI
            st.markdown(f"### 🤖 Predicție AI: **{predictie_muzicala}**")
            st.session_state.yt_query = predictie_muzicala
            
            # Salvare în memorie
            with open(LOG_FILE, "a") as f:
                f.write(f"{predictie_muzicala}\n")
            
            st.success("✅ Piesa a fost generată și trimisă în player!")

with col2:
    st.subheader("📺 YouTube Auto-Player")
    # Căutăm automat pe YouTube piesa generată de AI
    search_url = f"https://www.youtube.com/results?search_query={st.session_state.yt_query.replace(' ', '+')}"
    
    # Notă: Pentru autoplay real pe un video specific, ar fi nevoie de YouTube Search API.
    # Aici afișăm un player care caută piesa generată de AI.
    st.info(f"🔍 AI-ul a ales: {st.session_state.yt_query}")
    st.markdown(f"[▶️ Deschide Muzica pe YouTube]({search_url})")
    
    # Iframe de control (Embed automat - alternativă rapidă)
    embed_url = f"https://www.youtube.com/embed?listType=search&list={st.session_state.yt_query}&autoplay=1"
    st.markdown(
        f'<iframe width="100%" height="350" src="{embed_url}" frameborder="0" '
        f'allow="autoplay; encrypted-media; fullscreen" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )
    
    st.divider()
    st.write("📂 **Istoric Predicții AI (Memorie):**")
    for item in st.session_state.istoric:
        st.write(f"✅ {item}")
