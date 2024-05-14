# Proyecto de Procesamiento de PDF y Generación de Respuestas

Este proyecto implementa una API con FastAPI que permite el procesamiento de documentos PDF para extracción de texto y posterior generación de respuestas a preguntas específicas utilizando los textos extraídos. Utiliza modelos de embeddings y generación de texto de OpenAI y Cohere.

## Características

- Procesamiento de documentos PDF para extraer texto.
- Almacenamiento de embeddings y contextos extraídos.
- Generación de respuestas a preguntas basadas en el contexto del documento PDF.

## Instalación de Dependencias

Para ejecutar este proyecto, necesitas instalar las siguientes librerías:

```bash
pip install fastapi uvicorn pydantic numpy cohere openai transformers
