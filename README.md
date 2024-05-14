# Proyecto de Procesamiento de PDF y Generación de Respuestas

Este proyecto implementa una API con FastAPI que permite el procesamiento de documentos PDF para extracción de texto y posterior generación de respuestas a preguntas específicas utilizando los textos extraídos.

## Características

- Procesamiento de documentos PDF para extraer texto.
- Almacenamiento de embeddings y contextos extraídos.
- Generación de respuestas a preguntas basadas en el contexto del documento PDF.

## Instalación de Dependencias

Para ejecutar este proyecto, necesitas instalar las siguientes librerías:

```bash
pip install fastapi uvicorn pydantic numpy cohere openai transformers
```

## Ejecución del servidor
Para ejecutar el servidor API, utiliza el siguiente comando:

```bash
uvicorn main:app --reload
```
Este comando iniciará el servidor en localhost en el puerto 8000, y el modo --reload hace que el servidor se reinicie automáticamente al realizar cambios en el código.

## Uso con Postman
Para probar la API con Postman, sigue estos pasos:

### 1. Procesamiento de PDF
Endpoint: /process-pdf/
Método: GET
URL Completa: http://localhost:8000/process-pdf/?pdf_url=TU_URL_DEL_PDF
Descripción: Este endpoint toma una URL de un documento PDF como parámetro y procesa el documento para extraer texto y almacenar embeddings.
Respuesta Esperada: Un JSON que incluye un mensaje de éxito y un pdf_id que identifica el documento procesado.

### 2. Hacer una pregunta
Endpoint: /ask-question/
Método: GET
URL Completa: http://localhost:8000/ask-question/?pdf_id=EL_PDF_ID&query=TU_PREGUNTA
Descripción: Utiliza el pdf_id obtenido del procesamiento del PDF para hacer una pregunta relacionada con el contenido del documento.
Respuesta Esperada: Un JSON que incluye la pregunta realizada, la respuesta generada y los contextos más relevantes utilizados para generar la respuesta.
Nota
