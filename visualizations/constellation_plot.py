import matplotlib.pyplot as plt

def plot_constellation(
    f,
    t,
    spectrogram_db,
    peak_times,
    peak_freqs
):

    fig, ax = plt.subplots(figsize=(14, 6))

    # Spectrogram
    mesh = ax.pcolormesh(
        t,
        f,
        spectrogram_db,
        shading="gouraud",
        cmap="viridis"
    )

    # Detected peaks
    ax.scatter(
        peak_times,
        peak_freqs,
        color="red",
        s=8,
        alpha=0.8,
        label="Detected Peaks"
    )

    ax.set_title(
        "Spectrogram with Constellation Map",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Time (sec)", fontsize=12)
    ax.set_ylabel("Frequency (Hz)", fontsize=12)

    ax.set_ylim(0, 5000)

    ax.grid(
        linestyle="--",
        alpha=0.25
    )

    ax.legend(loc="upper right")

    cbar = fig.colorbar(mesh, ax=ax)
    cbar.set_label("Intensity (dB)")

    plt.tight_layout()

    return fig