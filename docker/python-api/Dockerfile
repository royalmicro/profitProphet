FROM python:3.12.4-bookworm

# Establish workdir
WORKDIR /app

COPY ../../app/ . 

# Instala las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto que usa la aplicación (ajústalo según tu aplicación)
EXPOSE 5000

# Make the shell script executable
RUN chmod +x bin/start.sh

# Run the shell script
CMD ["./bin/start.sh"]
