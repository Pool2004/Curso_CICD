# Importar python
FROM python:3.11.0

# Crear directorio de la aplicacion
WORKDIR /Curso_CICD/API

# Copiar los archivos de la aplicacion
COPY . /Curso_CICD/API

# Instalar las dependencias
RUN pip install --no-cache-dir -r /Curso_CICD/API/requirements.txt

# Exponer el puerto de la aplicacion
EXPOSE 8000

# Comando para ejecutar la aplicacion
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]





