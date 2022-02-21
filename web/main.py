import streamlit as st
import pickle
import pandas as pd

movies_dic = pickle.load(open('movie-dic.pkl','rb'))
movies = pd.DataFrame(movies_dic)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selecte_movie_name = st.selectbox(
'Enter movie',
movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    for i in movies_list:
        movie_id = i[0]
        recommended.append(movies.iloc[i[0]].title)
    return  recommended

if st.button('Recommend'):
    recommendations = recommend(selecte_movie_name)
    for i in recommendations:
        st.write(i)