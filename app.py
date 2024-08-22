import os
import pickle
import pandas as pd
import streamlit as st
import requests

# URL or path to your background image
background_image_url = 'https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f'

# Inject custom CSS to set the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('{background_image_url}');
        background-size: cover;
        background-position: center;
    }}
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: inherit;
        filter: blur(78px);
        z-index: -1;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Fetching the poster
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=40e16687ad61b092bf56a1099d0f9542&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Loading the movies_tag file for our recommender
with open('movies_tag.pkl', 'rb') as file:
    movies_tag = pickle.load(file)

movies_tag = pd.DataFrame(movies_tag)

# Loading the similarity file which is the cos_sim
with open('similarity.pkl', 'rb') as file:
    cos_sim = pickle.load(file)

# Loading the movies_data file for movie information
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

# Function to recommend movies and show details
# Function to recommend movies and show details
def recommender(movie):
    movie = movie.lower()
    found = False
    
    for i in range(len(titles)):
        if movie in titles[i]:
            image_url = fetch_poster(id[i])
            # Display the image
            st.image(image_url,width=300)
            # use_column_width=True
            st.write(f"**Title:** {titles[i].capitalize()}")
            
            # Convert crew list to a comma-separated string
            crew_text = ', '.join(crew[i])
            st.write(f"**Director:** {crew_text}")
            
            # Convert cast list to a comma-separated string
            cast_text = ', '.join(cast[i])
            st.write(f"**Cast:** {cast_text}")
            
            st.write(f"**Movie Description:** {info[i]}")
            st.write("---")
            found = True
    
    if not found:
        st.write("Sorry, no movie found with that name.")


# Streamlit app layout
def main():
    st.title("Movie Recommendation System")
    
    st.markdown("""
    Welcome to the Movie Recommendation System!  
    Enter the name of a movie you like, and we'll provide you with details about it.
    """)
    
    # Search bar for movie input
    movie_title = st.text_input("Search for a movie:", "")
    
    # Search button
    if st.button("Search"):
        recommender(movie_title)

# Run the app
if __name__ == "__main__":
    main()
