import matplotlib.pyplot as plt

def plot_histogram(offsets):

    fig, ax = plt.subplots(
        figsize=(10,4)
    )

    ax.hist(
        offsets,
        bins=100
    )

    ax.set_title(
        "Offset Histogram"
    )

    return fig