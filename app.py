from dotenv import load_dotenv
import streamlit as st
import pickle
import requests
import pandas as pd
import os
load_dotenv()
st.set_page_config(page_title="Movie Recommendation System", layout="wide")
st.sidebar.title("MENU")
page = st.sidebar.radio("", ["Home", "Developer"])
if page == "Home":
    st.title("Movie Recommendation System")
    api_key = os.getenv("api_key")
    def fetch_poster(movie_id):
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id, api_key))
        data = response.json()
        poster_path = data['poster_path']
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    select_movie_name = st.selectbox(
        "Select a Movie or Type a Movie Name",
        (movies["title"].values)
    )
    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
        movie_names = []
        movie_names_poster = []
        for i in distance:
            movie_id = movies.iloc[i[0]][0]
            movie_names.append(movies.iloc[i[0]].title)
            movie_names_poster.append(fetch_poster(movie_id))
        return movie_names, movie_names_poster
    similarity = pickle.load(open("similarity.pkl", "rb"))

    if st.button("Recommend"):
        movie_names, posters = recommend(select_movie_name)
        st.write("Recommended Movies")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(movie_names[0])
            st.image(posters[0])
        with col2:
            st.text(movie_names[1])
            st.image(posters[1])
        with col3:
            st.text(movie_names[2])
            st.image(posters[2])
        with col4:
            st.text(movie_names[3])
            st.image(posters[3])
        with col5:
            st.text(movie_names[4])
            st.image(posters[4])

elif page == "Developer":
    st.title("About the Developer")
    st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://wallpapers.com/images/hd/cartoon-kohli-cricket-4k-3ae01vjqfye2xnn8.jpg" 
             alt="John Doe" 
             height="300" 
             width="200" 
             style="border-radius: 40px;">
        <p><strong>AKSHAY KIREET</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)


    st.subheader("Profile")

    st.subheader("About Me")
    st.write("""
    I am a tech enthusiast passionate about artificial intelligence with a proven record of building 
    innovative AI projects. Proficient in the MERN stack, I’ve developed several applications that 
    highlight my programming skills. I excel in data structures and algorithms (DSA) and possess 
    strong organizational and time management abilities. My commitment to continuous learning 
    and staying updated with tech trends ensures I tackle complex challenges effectively. I am 
    also a team player, maintaining positive rapport with everyone.
    """)

    st.subheader("Mission and Vision of Movie Recommendation System")
    st.write("""
    **Mission**: To provide personalized movie recommendations using advanced machine learning algorithms, enhancing the user experience by helping users discover movies they’ll love.  

    **Vision**: To create a seamless and enjoyable platform for movie enthusiasts, leveraging AI to make movie discovery effortless and tailored to individual preferences.
    """)
