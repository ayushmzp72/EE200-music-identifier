import streamlit as st
import pandas as pd
import librosa

from core.fingerprint import fingerprint_audio
from core.matcher import match_song

def render(database):

    files = st.file_uploader(
        "Upload Query Clips",
        type=["mp3","wav"],
        accept_multiple_files=True
    )

    if files:

        with st.spinner("Analyzing audios and identifying songs..."):

            results = []

            for file in files:

                audio, sr = librosa.load(
                    file,
                    sr=22050
                )

                hashes, *_ = fingerprint_audio(
                    audio,
                    sr
                )

                prediction, _ = match_song(
                    hashes,
                    database
                )

                if prediction is None:
                    prediction = "Unknown"

                results.append(
                    [file.name, prediction]
                )

            df = pd.DataFrame(
                results,
                columns=[
                    "filename",
                    "prediction"
                ]
            )

            st.dataframe(df)

            st.download_button(
                "Download results.csv",
                df.to_csv(index=False),
                file_name="results.csv"
            )