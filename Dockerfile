# 1. Usar una imagen de Python oficial
FROM python:3.10-slim

# 2. Instalar FFmpeg (VITAL para audios de WhatsApp y MP4)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# 3. Crear carpeta de trabajo
WORKDIR /app

# 4. Copiar los archivos del proyecto
COPY . .

# 5. Instalar las librerías
RUN pip install --no-cache-dir -r requirements.txt

# 6. Exponer el puerto de Streamlit
EXPOSE 8501

# 7. Comando para arrancar
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]