# 🎙️ Transcriptor de Reuniones y WhatsApp

Este es un transcriptor profesional que utiliza la tecnología **OpenAI Whisper**. Está optimizado para funcionar en servidores (VPS) y procesar audios de WhatsApp (.ogg), MP3 y WAV.

## 🛠️ Requisitos previos para el VPS
Antes de instalar las librerías de Python, el sistema operativo del servidor debe tener instalado **FFmpeg**.

- **En Ubuntu/Debian:** `sudo apt update && sudo apt install ffmpeg -y`

## 🚀 Instalación y Despliegue
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv .venv`
3. Activar el entorno:
   - Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Iniciar la aplicación: `streamlit run app.py`

## 🔐 Acceso
- **Usuario:** admin
- **Contraseña:** 1234