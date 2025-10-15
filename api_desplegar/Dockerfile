# Importar python
FROM python:3.11.9

# Crear directorio de la aplicacion
WORKDIR /Curso_CICD/api_desplegar

# Copiar los archivos de la aplicacion
COPY . /Curso_CICD/api_desplegar

# Instalar las dependencias
RUN pip install --no-cache-dir -r /Curso_CICD/api_desplegar/requirements.txt

# Exponer el puerto de la aplicacion
EXPOSE 8000

# Comando para ejecutar la aplicacion
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]