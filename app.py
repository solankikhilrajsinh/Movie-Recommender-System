import streamlit as st
import pickle
import pandas as pd
import requests

# -----------------------------
# TMDB POSTER API (Using V3 API Key)
# -----------------------------
API_KEY = "8ab33365e0960cd0d51a13e295b376ea"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()
        poster = data.get("poster_path")

        if poster:
            return f"https://image.tmdb.org/t/p/w500/{poster}"

        return "https://via.placeholder.com/500x750?text=No+Image"

    except:
        return "https://via.placeholder.com/500x750?text=No+Image"


# RECOMMENDATION FUNCTION
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    sorted_movies = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []
    posters = []

    for i, score in sorted_movies:
        movie_id = movies.iloc[i].movie_id
        recommended_movies.append(movies.iloc[i].title)
        # fetch poster from API
        posters.append(fetch_poster(movie_id))

    return recommended_movies, posters


# LOAD DATA
# This is used for movies that also am getting from the pickle file
movies = pickle.load(open("movies.pkl", "rb"))
movies_list = movies["title"].tolist()

# This is used for movie_dict that also am getting 
# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))


# STREAMLIT UI
st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie to get recommendations:",
    movies_list
)

if st.button("Recommend Movies"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])
