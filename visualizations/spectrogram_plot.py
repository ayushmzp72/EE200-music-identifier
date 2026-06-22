import matplotlib.pyplot as plt

def plot_spectrogram(
    f,
    t,
    spectrogram_db
):

    fig, ax = plt.subplots(
        figsize=(10,4)
    )

    ax.pcolormesh(
        t,
        f,
        spectrogram_db,
        shading="gouraud"
    )

    ax.set_title(
        "Spectrogram"
    )

    return fig