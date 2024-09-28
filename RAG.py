import globals
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


class RAG:
    def __init__(self):
      pass

    def scrape_char(self,url):
        response = requests.get(url)

        if response.status_code != 200:
            return f"Failed to retrieve content. Status code: {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')
        article_text = [para.get_text(strip=True) for para in paragraphs if para.get_text(strip=True)]

        return article_text

    def splitter(self,docs):
        chunked_docs = []
        for i in range(20):
          splitter = RecursiveCharacterTextSplitter(chunk_size=300)
          chunked_docs.extend(splitter.split_text(docs[i]))
        return chunked_docs

    def embeddings(self,chunked_docs):
        response = globals.co.embed(texts=chunked_docs, model="embed-english-v2.0") 
        embeddings = response.embeddings
        embeddings = np.array(embeddings)
        return embeddings

    def faiss_index(self,embeddings):
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)
        return index

    def retrieve(self,query, index, k=2):
        query_embedding = globals.co.embed(texts=[query], model="embed-english-v2.0").embeddings[0]
        query_embedding = np.array(query_embedding)
        query_embedding = query_embedding.reshape(1, -1) 
        distances, indices = index.search(query_embedding, k)
        return indices

    def generate_response(self,context,query):
        response = globals.co.generate(
          model='command-xlarge-nightly',
          prompt="This is a character gussing game ,don't say the name of the character in the answer, answer the user question in one line based on this context: " + context + " Query: " + query,
          max_tokens=300,
          temperature=0.5,
        )
        return response.generations[0].text

    def rag_chatbot(self,query, index, documents):
        relevant_docs = self.retrieve(query, index)
        context = "\n".join([documents[i] for i in relevant_docs[0]])

        response = self.generate_response(context, query)

        return response