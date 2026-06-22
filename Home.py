import streamlit as st
from modes.single_clip import render as single_clip
from modes.batch_mode import render as batch_mode
from core.database import load_database

database = load_database()

st.title("🎵 Music Identifier")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🎵 Single Clip",
        use_container_width=True
    ):
        st.session_state.mode = "Single Clip"

with col2:

    if st.button(
        "📁 Batch Mode",
        use_container_width=True
    ):
        st.session_state.mode = "Batch Mode"

if "mode" not in st.session_state:
    st.session_state.mode = "Single Clip"

if st.session_state.mode == "Single Clip":
    single_clip(database)

elif st.session_state.mode == "Batch Mode":
    batch_mode(database)