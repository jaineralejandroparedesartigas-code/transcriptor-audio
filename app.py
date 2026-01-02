import streamlit as st
import whisper
import os
import time
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# --- 1. CARGA DE CONFIGURACIÓN ---
load_dotenv()
usuarios_string = os.getenv("USUARIOS_PERMITIDOS", "")
USUARIOS_AUTORIZADOS = [u.strip().lower() for u in usuarios_string.split(",") if u]
CLAVE_MAESTRA = os.getenv("CLAVE_MAESTRA", "proyectos2025")

if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)
db = firestore.client()

# --- 2. LOGIN ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔐 Acceso Protegido")
    mail = st.text_input("Correo:").lower().strip()
    pas = st.text_input("Contraseña:", type="password")
    if st.button("Ingresar"):
        if mail in USUARIOS_AUTORIZADOS and pas == CLAVE_MAESTRA:
            st.session_state["authenticated"], st.session_state["user_email"] = True, mail
            st.rerun()
        else: st.error("🚫 Error de acceso.")
    st.stop()

# --- 3. INTERFAZ ---
menu = st.sidebar.radio("Menú", ["🎙️ Transcribir", "📜 Mi Historial"])
modelo_ia = st.sidebar.selectbox("Calidad", ["tiny", "base", "small", "medium", "large"], index=2)

if menu == "🎙️ Transcribir":
    st.title("🎙️ Transcribir con Contexto")
    # AQUÍ ESTÁ EL PROMPT QUE PEDISTE
    contexto = st.text_area("📝 Contexto (palabras clave, nombres propios):", placeholder="Ej: Términos médicos, nombres de marcas...")
    archivo = st.file_uploader("Subir MP3 o MP4", type=["mp3", "wav", "m4a", "mp4"])
    
    if archivo and st.button("🚀 Iniciar"):
        with st.spinner("La IA está trabajando..."):
            path_temp = f"temp_{int(time.time())}.{archivo.name.split('.')[-1]}"
            with open(path_temp, "wb") as f: f.write(archivo.getbuffer())
            try:
                model = whisper.load_model(modelo_ia)
                # SE PASA EL CONTEXTO A WHISPER
                res = model.transcribe(path_temp, initial_prompt=contexto)
                db.collection("transcripciones").add({
                    "usuario": st.session_state["user_email"],
                    "texto": res["text"].strip(),
                    "archivo": archivo.name,
                    "fecha": firestore.SERVER_TIMESTAMP
                })
                st.success("¡Listo!")
                st.write(res["text"])
            finally: 
                if os.path.exists(path_temp): os.remove(path_temp)

else:
    st.title("📜 Mi Historial")
    docs = db.collection("transcripciones").where("usuario", "==", st.session_state["user_email"]).order_by("fecha", direction=firestore.Query.DESCENDING).stream()
    for doc in docs:
        item = doc.to_dict()
        with st.expander(f"📄 {item['archivo']}"):
            st.write(item['texto'])
            # BOTÓN DE ELIMINAR QUE PEDISTE
            if st.button("🗑️ Eliminar Registro", key=doc.id):
                db.collection("transcripciones").document(doc.id).delete()
                st.rerun()