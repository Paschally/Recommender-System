import pickle
import streamlit as st
import requests

st.set_page_config(page_title="movie recommender")
st.header("Movie Recommendation System Using Content-Based Filtering")

# Load the movie list and cosine similarity matrix
movies = pickle.load(open("movie_list.pkl", 'rb'))
cos_sim = pickle.load(open("similarity.pkl", 'rb'))

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(cos_sim[index])), reverse=True, key=lambda x: x[1])
    movie_names = []
    for i in distances[1:6]:  # Skip the first one because it is the movie itself
        movie_names.append(movies.iloc[i[0]].title)
    return movie_names

movie_selection = movies['title'].values

movie_selected = st.selectbox(
    "Select a movie to get recommendations",
    movie_selection
)

if st.button("Show recommendation"):
    movie_names = recommend(movie_selected)
    if movie_names:
        st.write("Check out below movies:")
        for name in movie_names:
            st.write("-",name)
    else:
        st.write("No recommendations found.")
