import pinecone
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from google.cloud import aiplatform
from google.cloud.aiplatform import generative_models
from langchain.vectorstores import Pinecone

# Step 1: Initialize Pinecone and Store PDF in Vector DB
pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
index_name = "auditor-notes-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=384)
index = pinecone.Index(index_name)

# Load and parse the PDF
loader = PyPDFLoader("auditor_notes.pdf")
documents = loader.load()

# Chunk the documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Generate embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
chunk_embeddings = embedding_model.embed_documents([chunk.page_content for chunk in chunks])

# Store embeddings in Pinecone
for i, (chunk, embedding) in enumerate(zip(chunks, chunk_embeddings)):
    index.upsert([(f"doc_{i}", embedding, {"text": chunk.page_content})])

# Step 2: Initialize Gemini Pro
aiplatform.init(project="your-project-id", location="us-central1")
gemini_pro_model = generative_models.GenerativeModel.from_pretrained("gemini-pro")

# Step 3: Set up Pinecone retriever
vector_store = Pinecone(index, embedding_model.embed_query, "text")
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Step 4: Query Gemini Pro with retrieved chunks
def query_gemini_with_retrieved_chunks(query, retriever, model):
    relevant_chunks = retriever.get_relevant_documents(query)
    context = "\n".join([chunk.metadata['text'] for chunk in relevant_chunks])

    prompt = f"""
    You are an expert financial analyst. Below are some excerpts from an auditor's report.

    Auditor Report Excerpts:
    {context}

    Based on this information, explain why the company's revenue increased.
    """
    
    response = model.predict(prompt)
    return response.text

# Example query
query = "Why did the company's revenue increase?"
response = query_gemini_with_retrieved_chunks(query, retriever, gemini_pro_model)

print("Gemini Pro Response:", response)
