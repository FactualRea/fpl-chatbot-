import os
from dotenv import load_dotenv

load_dotenv()

OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")
Pinecone_API_KEY = os.getenv("PINECONE_API_KEY")
Pinecone_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")