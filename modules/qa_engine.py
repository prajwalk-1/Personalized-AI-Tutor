from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import pdfplumber
import os

def load_knowledge_base(directory):
    """Load and embed documents."""
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    texts = []
    for file in os.listdir(directory):
        if file.endswith('.pdf'):
            with pdfplumber.open(os.path.join(directory, file)) as pdf:
                texts.append(' '.join([page.extract_text() for page in pdf.pages]))
    vector_store = FAISS.from_texts(texts, embeddings)
    return vector_store

def create_qa_chain(vector_store):
    """Create a QA chain using LangChain."""
    prompt = PromptTemplate(
        input_variables=["question", "context"],
        template="Context: {context}\nQuestion: {question}\nAnswer:"
    )
    qa_chain = RetrievalQA.from_chain_type(
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )
    return qa_chain
