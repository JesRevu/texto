import numpy as np
from openai import OpenAI
import cohere
from transformers import pipeline

# Configuración de API y variables globales
openai_api_key = "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"
client = OpenAI(api_key=openai_api_key)
cohere_apikey = "7IYCa3pcDXXkgSGccqrHcalfkMaClrkeaGHWH5O4"
co = cohere.Client(cohere_apikey)

# Inicializa el pipeline de generación de texto con tu modelo preferido
model_name = "EleutherAI/gpt-neo-2.7B"  # Ejemplo de modelo, ajusta según necesites
text_generator = pipeline('text-generation', model=model_name)

def generate_response(query, pdf_id, embeddings_storage, contexts_storage):
    try:
        # Recuperación de contextos y cálculo de la relevancia
        contexts = contexts_storage.get(pdf_id)
        doc_emb = embeddings_storage.get(pdf_id)
        if not contexts or not doc_emb:
            raise ValueError("No context or embeddings available for this PDF.")

        query_emb = co.embed([query], input_type="search_query", model="embed-english-v3.0").embeddings
        query_emb = np.asarray(query_emb)
        scores = np.dot(query_emb, doc_emb.T)[0]
        max_idx = np.argsort(-scores)[:10]
        most_relevant_contexts = [contexts[idx] for idx in max_idx]

        # Integración de los contextos para crear un prompt más coherente
        combined_context = " ".join(most_relevant_contexts)
        prompt = f"To answer the question: '{query}', consider the following information: {combined_context}"

        # Generación de la respuesta utilizando el modelo de texto
        responses = text_generator(prompt, max_new_tokens=200, num_return_sequences=1)
        synthesized_answer = responses[0]['generated_text'].split('\n')[0]

        return synthesized_answer.strip(), most_relevant_contexts

    except Exception as e:
        # Manejo de cualquier excepción que ocurra durante el proceso
        print(f"An error occurred: {str(e)}")
        return "PDF nos se puede procesar, asegurate de poner bien el id y de que la url este correcta", []
