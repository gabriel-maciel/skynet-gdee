FROM python:3.9-slim-buster

# Copiar el contenido de la carpeta actual al contenedor de Docker
COPY . /app

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el bot de Telegram
CMD [ "python", "skynet-bot.py" ]
