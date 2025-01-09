import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import retrieval_qa
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
load_dotenv()

def setup_qa_system():
    pass


