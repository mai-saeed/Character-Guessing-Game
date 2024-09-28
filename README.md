# Character Guessing Game

## Overview

This project is a **character guessing game** that integrates **Retrieval-Augmented Generation (RAG)**, **Wikipedia data scraping**, and a **chatbot**. The game allows users to select a category of characters, from which a random character's data is scraped from Wikipedia. The bot gives clues about the character, but without revealing the name, and the player has to guess the character within five chances.

## Features

- **Data Scraping**: Wikipedia pages are scraped using BeautifulSoup, and only the `<p>` tags are retained for the main content.
- **Text Preprocessing**: HTML tags are removed, and paragraphs are split into chunks using recursive splitting to maintain context.
- **Embeddings**: The paragraphs are embedded using **Cohere**, chosen after experimentation with different models (including GPT-2).
- **Vector Database**: **Faiss** is used for efficient similarity search and to store the embeddings for fast retrieval.
- **Retrieval-Augmented Generation (RAG)**: When the user queries, the query is embedded and matched with the vector database to find the two most relevant chunks. These are passed to the generator to create a clue, following the game rule to avoid naming the character.
- **Game Rules**: The player interacts with the bot, which provides clues based on the retrieved context, and has five chances to guess the character.
- **Future Enhancements**: Plans to integrate an API using **FastAPI** and build a simple GUI for interactivity.
