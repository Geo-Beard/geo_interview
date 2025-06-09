import matplotlib.pyplot as plt
from main import read_data


def build_plot(figsize=(15, 10)):
    fig, ax = plt.subplots(figsize=figsize)
    fig.delaxes(ax)
    return fig


def build_axes():
    # fig = build_plot()
    well = read_data("data/WA1.txt")
    ax1 = plt.subplot2grid((1, 10), (0, 0), rowspan=1, colspan=3)
    ax1.plot(well["GR"], well['M__DEPTH'], color="green", linewidth=0.5)
    ax1.set_xlabel("Gamma")
    ax1.xaxis.label.set_color("green")
    ax1.set_xlim(0, 150)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    ax1.set_xticks([0, 50, 100, 150])
    ax1.text(0.05, 1.04, 0, color='green',
             horizontalalignment='left', transform=ax1.transAxes)
    ax1.text(0.95, 1.04, 150, color='green',
             horizontalalignment='right', transform=ax1.transAxes)
    ax1.set_xticklabels([])
    plt.show()


build_axes()
