import streamlit as st
import librosa

from core.fingerprint import fingerprint_audio
from core.matcher import match_song

from visualizations.spectrogram_plot import plot_spectrogram
from visualizations.constellation_plot import plot_constellation
from visualizations.histogram_plot import plot_histogram

def render(database):

    uploaded = st.file_uploader(
        "Upload Audio",
        type=["mp3","wav"]
    )

    if uploaded:

        with st.spinner("Analyzing audio and identifying song..."):

            audio, sr = librosa.load(
                uploaded,
                sr=22050
            )

            (
                hashes,
                f,
                t,
                spectrogram_db,
                peak_freqs,
                peak_times
            ) = fingerprint_audio(
                audio,
                sr
            )

            song, offsets = match_song(
                hashes,
                database
            )

        if song is None:

            st.error(
                "❌ Song not recognized in database"
            )

        else:

            st.success(
                f"🎵 Recognized Song: {song}"
            )


        with st.spinner("Creating visualizations..."):

            st.pyplot(
                plot_spectrogram(
                    f,
                    t,
                    spectrogram_db
                )
            )

            st.pyplot(
                plot_constellation(
                    peak_times,
                    peak_freqs
                )
            )

            st.pyplot(
                plot_histogram(
                    offsets
                )
            )