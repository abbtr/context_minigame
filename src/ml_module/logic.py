import numpy as np
import pandas as pd 
import math
from numpy.linalg import norm
embeddings = {}

def load_embeddings(filepath):
    counter = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if counter == 0:
                counter += 1
                continue
            
            parts = line.strip().split()
            if len(parts) < 2:
                continue  # Skip empty or malformed lines
            token = parts[0]  # word_POS format
            vector = np.array(list(map(float, parts[1:])))
            embeddings[token] = vector
    return embeddings

def cosine_similarity(word1, word2):
    word2_real = word2[0]
    cos = (np.dot(embeddings[word1], embeddings[word2_real]))/((norm(embeddings[word1])*norm(embeddings[word2])))
    return cos


def get_most_similar(word_to_search):
    x = 0
    name = ''

    for word, vector in embeddings.items():
        
        if word == word_to_search:
            continue
        sim = cosine_similarity(word_to_search, word)

        if sim >= x:
            x = sim
            name = word

    return name, x

def create_top(slovo):
    
    top_unsorted = []
    for key,value in embeddings.items():
        top_unsorted.append([key, cosine_similarity(key, slovo)]) 
    
    top_sorted = sorted(top_unsorted, key=lambda x : x[1], reverse=True)
    dictat = {}

    for i,j in enumerate(top_sorted):
        j.append(i)

    for i in top_sorted:
        dictat[i[0]] = i[2]
    
def start_up_ml():
    load_embeddings('src/ml_module/model.txt')

def get_embeddings():
    return embeddings