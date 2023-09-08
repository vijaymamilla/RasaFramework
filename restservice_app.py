from fastapi import FastAPI, Request
from typing import Dict
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = FastAPI()


@app.get("/api/v1/health", summary="Health check", description="Check if the API is up.")
async def get_health_check_status() -> Dict:
    """Generate a health check response for the applications."""
    return {"status": "UP", "details": "Application is running normally."}

# Load data, embeddings, and model.  Adjust the paths as needed
df = pd.read_csv('dataset.csv', low_memory=False, encoding='utf-8')
embedings_matrix = np.load("embeddings_matrix_v1.npy")
bert = SentenceTransformer('all-MiniLM-L6-v2')

def get_top(searchQuery, k=1):
    search_arr = np.array([searchQuery])
    search_embeddings = bert.encode(search_arr)
    similarity_matrix = cosine_similarity(search_embeddings, embedings_matrix)
    top_k_ids = np.argsort(similarity_matrix[0])[-k:][::-1]

    responses = ""
    for id_ in top_k_ids:
        row = df.iloc[id_]

        responses = " ".join([row['Content'].strip(), row['Source'].strip()])

    return responses

def get_top_k_matches(searchQuery, k=1):
    search_arr = np.array([searchQuery])
    search_embeddings = bert.encode(search_arr)
    similarity_matrix = cosine_similarity(search_embeddings, embedings_matrix)
    top_k_ids = np.argsort(similarity_matrix[0])[-k:][::-1]

    responses = []
    for id_ in top_k_ids:
        row = df.iloc[id_]
        answer = {
            "Title": row['Title'],
            "Source": row['Source'],
            "DateOfScrapping": row['DateOfScrapping'],
            "Content": row['Content']
        }
        responses.append(answer)

    return responses

@app.get("/api/v1/qa", summary="Question Answers", description="Returns Answer.")
async def qa(prompt):
    result = get_top(prompt)
    response = result
    return response

if __name__ == '__main__':
    print('main function called')