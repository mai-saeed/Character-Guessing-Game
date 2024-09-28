#main
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel, pipeline
import os
import torch
import random
import cohere
import requests
from bs4 import BeautifulSoup
import globals
from RAG import RAG

rag=RAG()
print("Guess the character game , ask the chatbot about him and try to guess. Type 'quit' to exit.") 
print('-----------------------------------------------------------------------------------')
print("choose the category: A: sports , B: History , C: Science ") 
userinput=input('Enter A or B or C')
if userinput not in ['A', 'B', 'C']:
    print("Invalid input. Please enter A, B, or C.")
    exit()
category=globals.MCQ[userinput]
rand=random.randint(0, 2)
docs=rag.scrape_char(globals.urls[category][rand])
chunked_docs=rag.splitter(docs)
embeddings=rag.embeddings(chunked_docs)
index=rag.faiss_index(embeddings)

cnt=0
while True:
    cnt+=1
    if cnt==5:
        print(" the person is ",globals.persons[category][rand])
        break
    user_query = input("You: ")
    if user_query.lower() == 'quit':
        print("Goodbye!")
        break
    response = rag.rag_chatbot(user_query, index, chunked_docs)
    print("Chatbot:", response)
