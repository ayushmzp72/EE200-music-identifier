import matplotlib.pyplot as plt

def plot_constellation(
    peak_times,
    peak_freqs
):

    fig, ax = plt.subplots(
        figsize=(10,4)
    )

    ax.scatter(
        peak_times,
        peak_freqs,
        s=5
    )

    ax.set_title(
        "Constellation Map"
    )

    return fig