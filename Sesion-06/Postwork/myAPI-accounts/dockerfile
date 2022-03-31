# Utilizar la imagen oficial de Python 3
FROM python:3

# Seleccionar el directorio donde trabajaremos
# Copiar el codigo fuente al directorio de trabajo
COPY ./src/ /usr/src/accounts
WORKDIR /usr/src/accounts

# Instalar flask y sus dependencias.
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt --no-color

# Abrir el puerto 80 del contendor
EXPOSE 5000

# Injectar variable de configuracion para flask
ENV FLASK_APP=accounts.py

# Iniciar el servicio
CMD [ "flask", "run", "--host=0.0.0.0" ]