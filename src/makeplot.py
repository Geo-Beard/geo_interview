import matplotlib.pyplot as plt
import numpy as np


def makeplot(depth, gamma, res, neut, dens, dtc, formations_dict, topdepth,
             bottomdepth, colors, formation_midpoints):
    fig, ax = plt.subplots(figsize=(15, 10))
    # Removes default 0-1 axes
    fig.delaxes(ax)

    # Set up the plot axes
    ax1 = plt.subplot2grid((1, 10), (0, 0), rowspan=1, colspan=3)
    ax2 = plt.subplot2grid((1, 10), (0, 3), rowspan=1, colspan=3, sharey=ax1)
    ax3 = plt.subplot2grid((1, 10), (0, 6), rowspan=1, colspan=3, sharey=ax1)
    ax4 = ax3.twiny()
    ax5 = plt.subplot2grid((1, 10), (0, 9), rowspan=1, colspan=1, sharey=ax1)

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)

    # Gamma Ray track

    # Setting up the track and curve
    ax1.plot(gamma, depth, color="green", linewidth=0.5)
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

    # Setting Up Shading for GR
    left_col_value = 0
    right_col_value = 150
    span = abs(left_col_value - right_col_value)
    cmap = plt.get_cmap('hot_r')
    color_index = np.arange(left_col_value, right_col_value, span / 100)
    # loop through each value in the color_index
    for index in sorted(color_index):
        index_value = (index - left_col_value)/span
        color = cmap(index_value)  # obtain color for color index value
        ax1.fill_betweenx(depth, gamma, right_col_value,
                          where=gamma >= index,  color=color)

    # Resistivity track
    ax2.plot(res, depth, color="red", linewidth=0.5)
    ax2.set_xlabel("Resistivity")
    ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    ax2.set_xticks([0.1, 1, 10, 100, 1000])
    ax2.semilogx()
    ax2.text(0.05, 1.04, 0.1, color='red',
             horizontalalignment='left', transform=ax2.transAxes)
    ax2.text(0.95, 1.04, 1000, color='red',
             horizontalalignment='right', transform=ax2.transAxes)
    ax2.set_xticklabels([])

    # Density track
    ax3.plot(dens, depth, color="red", linewidth=0.5)
    ax3.set_xlabel("Density")
    ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    ax3.set_xticks([1.95, 2.45, 2.95])
    ax3.text(0.05, 1.04, 1.95, color='red',
             horizontalalignment='left', transform=ax3.transAxes)
    ax3.text(0.95, 1.04, 2.95, color='red',
             horizontalalignment='right', transform=ax3.transAxes)
    ax3.set_xticklabels([])

    # Neutron track placed ontop of density track
    ax4.plot(neut, depth, color="blue", linewidth=0.5)
    ax4.set_xlabel('Neutron')
    ax4.xaxis.label.set_color("blue")
    ax4.set_xlim(45, -15)
    ax4.tick_params(axis='x', colors="blue")
    ax4.spines["top"].set_position(("axes", 1.08))
    ax4.spines["top"].set_visible(True)
    ax4.spines["top"].set_edgecolor("blue")
    ax4.set_xticks([45,  15, -15])
    ax4.text(0.05, 1.1, 45, color='blue',
             horizontalalignment='left', transform=ax4.transAxes)
    ax4.text(0.95, 1.1, -15, color='blue',
             horizontalalignment='right', transform=ax4.transAxes)
    ax4.set_xticklabels([])

    ax5.set_xticklabels([])
    ax5.text(0.5, 1.1, 'Biozones', fontweight='bold',
             horizontalalignment='center', transform=ax5.transAxes)

    # Adding in neutron density shading
    x1 = dens
    x2 = neut

    x = np.array(ax3.get_xlim())
    z = np.array(ax4.get_xlim())

    nz = ((x2-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    ax3.fill_betweenx(depth, x1, nz, where=x1 >= nz,
                      interpolate=True, color='green')
    ax3.fill_betweenx(depth, x1, nz, where=x1 <= nz,
                      interpolate=True, color='yellow')

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3]:
        ax.set_ylim(bottomdepth, topdepth)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))

    for ax in [ax1, ax2, ax3, ax5]:
        # loop through the formations dictionary and zone colors
        for depth, color in zip(formations_dict.values(), colors):
            # use the depths and colors to shade across the subplots
            ax.axhspan(depth[0], depth[1], color=color, alpha=0.1)

    for ax in [ax2, ax3, ax4, ax5]:
        plt.setp(ax.get_yticklabels(), visible=False)

    for label, formation_mid in zip(formations_dict.keys(),
                                    formation_midpoints):
        ax5.text(0.5, formation_mid, label, rotation=90,
                 verticalalignment='center', fontweight='bold',
                 fontsize='large')

    plt.tight_layout()
    fig.subplots_adjust(wspace=0)
    plt.savefig('output/figure.png')
