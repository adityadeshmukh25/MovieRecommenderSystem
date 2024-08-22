import os
import pickle
import pandas as pd
import numpy as np


# Loading the  movies_tag file for our recommender
with open('movies_tag.pkl', 'rb') as file:
    movies_tag = pickle.load(file)

movies_tag = pd.DataFrame(movies_tag)

# Loading the similarity file which is the cos_sim
with open('similarity.pkl', 'rb') as file:
    cos_sim = pickle.load(file)

with open('movies_data.pkl', 'rb') as file:
    movies_data = pickle.load(file)
movies_data = pd.DataFrame(movies_data)

# Correcting the order of titles
titles = list(movies_tag['title'])
titles = [x.lower() for x in titles]

# Extracting movie information
id = list(movies_data['id'])
crew = list(movies_data['crew'])
cast = list(movies_data['cast'])
info = list(movies_data['overview'])

def recommender(movie):
    for i in range(len(titles)):
        if movie in titles[i]:
            print(titles[i])
            print(id[i])
            print(crew[i])
            print(cast[i])
            print(info[i])


user = input("Enter movie name: ")
recommender(user)

