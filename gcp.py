import os
import re
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import FAISS
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.schema import Document
from vertexai.language.models import TextEmbeddingModel

class VertexTextEmbedding:
    def __init__(self, model_name="textembedding-gecko"):
        # Load the Vertex AI Text Embedding Model
        self.model = TextEmbeddingModel.from_pretrained(model_name)
        
    def embed_documents(self, documents):
        # Create embeddings for each document
        return [self.model.get_embeddings([doc])[0] for doc in documents]
    
    def embed_query(self, text):
        # Embed a single query
        return self.model.get_embeddings([text])[0]

class RAG:
    def __init__(self, pdf_path, chunking_method, faiss_vector_store=None, input_chunks=None):
        '''
        pdf_path: path to the PDF files
        chunking_method: name of the chunking method
        '''
        # save a copy of the original text using PyPDF2
        self.text = self.read_pdf(pdf_path)
        
        self.chunks=None
        if input_chunks:
            self.chunks=[Document(page_content=chunk) for chunk in input_chunks]
        else:
            self.chunks=self.get_chunks(pdf_path, chunking_method)
            
        # Initialize the Vertex AI Text Embedding model
        self.embedding_model = VertexTextEmbedding(model_name="textembedding-gecko")
        
        # Initialize different retrievers, including faiss_retriever and bm25_retriever
        if faiss_vector_store is None:  # faiss store is slow to create if the embedding model is large, so we load a pre-computed one
            self.faiss_vector_store = FAISS.from_documents(self.chunks, self.embedding_model)
        else:
            self.faiss_vector_store = faiss_vector_store
            
        self.faiss_retriever = self.faiss_vector_store.as_retriever(search_kwargs={"k": 3})  # k is the number of returned chunks

        self.bm25_retriever = BM25Retriever.from_documents(self.chunks)
        self.bm25_retriever.k = 3  # k is the number of returned chunks

        # Create the ensemble retriever, which will sort all returned documents by order based on its sorting criteria
        self.ensemble_retriever = EnsembleRetriever(retrievers=[self.faiss_retriever, self.bm25_retriever], weights=[0.5, 0.5])


import pandas as pd

# Sample DataFrame with 53 rows (replace this with your actual DataFrame)
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}  # Example DataFrame
df = pd.DataFrame(data)

# Duplicate the DataFrame 100 times
df_repeated = pd.concat([df] * 100, ignore_index=True)

# Create the 'id' column with row numbers (1 to 5300)
df_repeated['id'] = df_repeated.index + 1

# Display the resulting DataFrame
print(df_repeated)


import pandas as pd
import json

# Sample DataFrame with 'id' and 'embeddings' (replace this with your actual DataFrame)
data = {'id': [1, 2, 3], 'embeddings': ['embedding1', 'embedding2', 'embedding3']}
df = pd.DataFrame(data)

# Define the filename for the JSONL file
filename = 'output.jsonl'

# Open the file in write mode
with open(filename, 'w') as f:
    # Iterate through each row of the DataFrame
    for _, row in df.iterrows():
        # Create a dictionary for each row
        json_line = {"id": row['id'], "embedding": row['embeddings']}
        # Write the JSON dictionary as a JSONL (one line per dictionary)
        f.write(json.dumps(json_line) + '\n')

# The 'output.jsonl' file will be created in your current directory.
print(f"JSONL file '{filename}' created successfully!")

https://github.com/Sahilvohra58/gen-ai-on-google-cloud/blob/main/RAG_LLMOps_with_GCP.ipynb
