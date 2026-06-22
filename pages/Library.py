import streamlit as st
from core.database import load_database

database = load_database()


st.header("📚 Music Library")
st.write(f"Total Songs Indexed: {len(database)}")

songs = sorted(database.keys())

cols = st.columns(3)

for i, song in enumerate(songs):
    cols[i % 3].markdown(f"🎵 **{song}**")