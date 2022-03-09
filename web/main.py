import pickle
import pandas as pd
import requests
import streamlit as st

similar = pickle.load(open('similarity.pkl', 'rb'))
dictionary = pickle.load(open('movie-dic.pkl', 'rb'))
movies = pd.DataFrame(dictionary)


st.title('Movie Recommender')
enter_movie_name = st.selectbox('Enter movie', movies['title'].values)


def get_poster(id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=01e0737bd91d2ff025766f7ad4fd784c&language=en-US'.format(id))
    d = res.json()
    return 'https://image.tmdb.org/t/p/w500/'+d['poster_path']


def rec(movie):
    index = movies[movies['title'] == movie].index[0]
    dist = similar[index]
    m_l = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:8]
    rec_mv = []
    rec_mv_poster = []
    for i in m_l:
        id = movies.iloc[i[0]].movie_id
        rec_mv.append(movies.iloc[i[0]].title)
        rec_mv_poster.append(get_poster(id))
    return rec_mv, rec_mv_poster


if st.button('Recommend'):
    name, poster = rec(enter_movie_name)

    col = st.columns(7)

    for x in range(0, 7):
        with col[x]:
            st.text(name[x])
            st.image(poster[x])



