# pdf_processor.py
import uuid
from langchain.embeddings import OpenAIEmbeddings
from llmsherpa.readers import LayoutPDFReader
import os
import numpy as np
from llmsherpa.readers import LayoutPDFReader
import cohere


# Configuración de API y variables globales
llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
os.environ["OPENAI_API_KEY"] = "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"
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
cohere_apikey = "7IYCa3pcDXXkgSGccqrHcalfkMaClrkeaGHWH5O4"
co = cohere.Client(cohere_apikey)

def process_pdf(pdf_url, embeddings_storage, contexts_storage):
    pdf_reader = LayoutPDFReader(llmsherpa_api_url)
    doc = pdf_reader.read_pdf(pdf_url)

    contexts = [chunk.to_context_text() for chunk in doc.chunks()]
    doc_emb = co.embed(contexts, input_type="search_document", model="embed-english-v3.0").embeddings
    doc_emb = np.asarray(doc_emb)

    pdf_id = str(uuid.uuid4())
    embeddings_storage[pdf_id] = doc_emb
    contexts_storage[pdf_id] = contexts
    
    return pdf_id

