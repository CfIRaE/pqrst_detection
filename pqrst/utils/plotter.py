import matplotlib.pyplot as plt


def plot_signal(signal, peaks):

    """ imput array of 15 entries"""

    # Create figure with 3x3 sub-plots.
    fig, axes = plt.subplots(5, 3)
    fig.subplots_adjust(hspace=0.03, wspace=0.03)

    for i, ax in enumerate(axes.flat):
        # Plot image.
        ax.plot(signal[i])
        ax.plot(peaks[i], [signal[i][j] for j in peaks[i]], 'ro')

    # Ensure the plot is shown correctly with multiple plots
    # in a single Notebook cell.
    plt.show()
