from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from app.config import (OpenAI_API_KEY, Pinecone_API_KEY, Pinecone_INDEX_NAME,)
from langchain_core import Document 

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

pc = Pinecone(api_key=Pinecone_API_KEY)

index = pc.Index(Pinecone_INDEX_NAME)

vectorstore = PineconeVectorStore(index=index, embedding=embeddings,)

documents = []

for item in raw_documents:
    documents.append(Document(page_content=item["text"], metadata={"source": item["source"], "data_type": "historical"}))

vectorstore.add_documents(documents)