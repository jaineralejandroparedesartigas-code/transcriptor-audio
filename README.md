# 🎙️ Transcriptor de Audio Pro (Whisper + Firebase)

Este proyecto es una herramienta avanzada para transcribir audios (MP3, WAV, M4A) y videos (MP4) utilizando la IA de Whisper.

## ✨ Características
- **🔒 Login Seguro**: Acceso controlado por lista de correos autorizados.
- **🧠 Contexto de IA**: Permite añadir palabras clave para mejorar la precisión técnica.
- **📜 Historial**: Transcripciones guardadas en Firebase con opción de eliminar.
- **🐳 Docker Ready**: Configurado para ejecutarse en cualquier lugar.

## 🚀 Instalación con Docker
1. Clona el repositorio.
2. Agrega tus archivos `.env` y `firebase-key.json` en la raíz.
3. Construye la imagen:
   ```bash
   docker build -t transcriptor-audio .