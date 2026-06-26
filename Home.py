import streamlit as st
from modes.single_clip import render as single_clip
from modes.batch_mode import render as batch_mode
from core.database import load_database

database = load_database()

if "mode" not in st.session_state:
    st.session_state.mode = "Single Clip"

st.title("🎵 Music Identifier")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🎵 Single Clip",
        use_container_width=True,
        type="primary" if st.session_state.mode == "Single Clip" else "secondary"
    ):
        st.session_state.mode = "Single Clip"
        st.rerun()

with col2:
    if st.button(
        "📁 Batch Mode",
        use_container_width=True,
        type="primary" if st.session_state.mode == "Batch Mode" else "secondary"
    ):
        st.session_state.mode = "Batch Mode"
        st.rerun()

st.divider()

if st.session_state.mode == "Single Clip":
    single_clip(database)
else:
    batch_mode(database)