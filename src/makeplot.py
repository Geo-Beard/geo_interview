import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def makeplot(depth, gamma, sp, res, res2, res3, neut, dens, dt,
             formations_dict, topdepth, bottomdepth, colors,
             formation_midpoints):
    fig, ax = plt.subplots(figsize=(15, 10))
    # Removes default 0-1 axes as we're using subplots
    fig.delaxes(ax)

    # Set up the plot axes
    # GR
    ax1 = plt.subplot2grid((1, 13), (0, 0), rowspan=1, colspan=3)
    # Res (LL8)
    ax2 = plt.subplot2grid((1, 13), (0, 3), rowspan=1, colspan=3, sharey=ax1)
    # Res (ILM)
    ax3 = ax2.twiny()
    # Res (ILD)
    ax4 = ax3.twiny()
    # Neutron
    ax5 = plt.subplot2grid((1, 13), (0, 6), rowspan=1, colspan=3, sharey=ax1)
    # Density shared with Neutron
    ax6 = ax5.twiny()
    # DT
    ax7 = plt.subplot2grid((1, 13), (0, 9), rowspan=1, colspan=3, sharey=ax1)
    # Biozones
    ax8 = plt.subplot2grid((1, 13), (0, 12), rowspan=1, colspan=1, sharey=ax1)
    # SP
    ax9 = ax1.twiny()

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    # Added from base
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax5.twiny()
    ax14.xaxis.set_visible(False)
    ax15 = ax6.twiny()
    ax15.xaxis.set_visible(False)
    ax16 = ax7.twiny()
    ax16.xaxis.set_visible(False)
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

    # Adding peaks and troughs detection for Gamma

    # Ensure gamma and depth are numpy arrays for indexing
    gamma = np.array(gamma)
    depth = np.array(depth)

    # Detect peaks (high gamma values)
    peaks, _ = find_peaks(gamma, prominence=30, distance=60)

    # Detect troughs (low gamma values)
    troughs, _ = find_peaks(-gamma, prominence=30, distance=60)

    # Plot markers on gamma track
    ax1.plot(gamma[peaks], depth[peaks], 'ro', markersize=3,
             label='Peaks')     # red dots for peaks
    ax1.plot(gamma[troughs], depth[troughs], 'bo', markersize=3,
             label='Troughs')  # blue dots for troughs

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

    # SP
    ax9.plot(sp, depth, color="blue", linewidth=0.5)
    ax9.set_xlabel("SP")
    ax9.set_xlim(-160, 40)
    ax9.xaxis.label.set_color("blue")
    ax9.tick_params(axis='x', colors="blue")
    ax9.spines["top"].set_position(("axes", 1.06))
    ax9.spines["top"].set_visible(True)
    ax9.spines["top"].set_edgecolor("blue")
    ax9.set_xticks([-160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40])
    ax9.text(0.05, 1.07, -160, color='blue',
             horizontalalignment='left', transform=ax9.transAxes)
    ax9.text(0.95, 1.07, 40, color='blue',
             horizontalalignment='right', transform=ax9.transAxes)
    ax9.set_xticklabels([])

    # Resistivity track (LL8)
    ax2.plot(res, depth, color="red", linewidth=0.5)
    ax2.set_xlabel("Resistivity (LL8)")
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

    # Resistivity track (ILM)
    ax3.plot(res2, depth, color="blue", linewidth=0.5)
    ax3.set_xlabel("Resistivity (ILM)")
    ax3.set_xlim(0.2, 2000)
    ax3.xaxis.label.set_color("blue")
    ax3.tick_params(axis='x', colors="blue")
    ax3.spines["top"].set_position(("axes", 1.06))
    ax3.spines["top"].set_visible(True)
    ax3.spines["top"].set_edgecolor("blue")
    ax3.set_xticks([0.1, 1, 10, 100, 1000])
    ax3.semilogx()
    ax3.text(0.05, 1.07, 0.1, color='blue',
             horizontalalignment='left', transform=ax3.transAxes)
    ax3.text(0.95, 1.07, 1000, color='blue',
             horizontalalignment='right', transform=ax3.transAxes)
    ax3.set_xticklabels([])

    # Resistivity track (ILD)
    ax4.plot(res3, depth, color="green", linewidth=0.5)
    ax4.set_xlabel("Resistivity (ILD)")
    ax4.set_xlim(0.2, 2000)
    ax4.xaxis.label.set_color("green")
    ax4.tick_params(axis='x', colors="green")
    ax4.spines["top"].set_position(("axes", 1.09))
    ax4.spines["top"].set_edgecolor("green")
    ax4.spines["top"].set_visible(True)
    ax4.set_xticks([0.1, 1, 10, 100, 1000])
    ax4.semilogx()
    ax4.text(0.05, 1.1, 0.1, color='green',
             horizontalalignment='left', transform=ax4.transAxes)
    ax4.text(0.95, 1.1, 1000, color='green',
             horizontalalignment='right', transform=ax4.transAxes)
    ax4.set_xticklabels([])
    # # Adding peaks and troughs detection for Res

    # # Ensure res is numpy array for indexing, already have depth
    # resistivity = np.array(res)

    # # Detect peaks (high gamma values)
    # peaks, _ = find_peaks(resistivity, prominence=5, distance=10)

    # # Detect troughs (low gamma values)
    # troughs, _ = find_peaks(-resistivity, prominence=5, distance=10)

    # # Plot markers on res track
    # ax2.plot(res[peaks], depth[peaks], 'ro', markersize=3,
    #          label='Peaks')     # red dots for peaks
    # ax2.plot(res[troughs], depth[troughs], 'bo', markersize=3,
    #          label='Troughs')  # blue dots for troughs

    # Density track
    ax5.plot(dens, depth, color="red", linewidth=0.5)
    ax5.set_xlabel("Density")
    ax5.set_xlim(1.95, 2.95)
    ax5.xaxis.label.set_color("red")
    ax5.tick_params(axis='x', colors="red")
    ax5.spines["top"].set_edgecolor("red")
    ax5.set_xticks([1.95, 2.45, 2.95])
    ax5.text(0.05, 1.04, 1.95, color='red',
             horizontalalignment='left', transform=ax5.transAxes)
    ax5.text(0.95, 1.04, 2.95, color='red',
             horizontalalignment='right', transform=ax5.transAxes)
    ax5.set_xticklabels([])

    # Neutron track placed ontop of density track
    ax6.plot(neut, depth, color="blue", linewidth=0.5)
    ax6.set_xlabel('Neutron')
    ax6.xaxis.label.set_color("blue")
    ax6.set_xlim(45, -15)
    ax6.tick_params(axis='x', colors="blue")
    ax6.spines["top"].set_position(("axes", 1.08))
    ax6.spines["top"].set_visible(True)
    ax6.spines["top"].set_edgecolor("blue")
    ax6.set_xticks([45,  15, -15])
    ax6.text(0.05, 1.1, 45, color='blue',
             horizontalalignment='left', transform=ax6.transAxes)
    ax6.text(0.95, 1.1, -15, color='blue',
             horizontalalignment='right', transform=ax6.transAxes)
    ax6.set_xticklabels([])

    # DT
    ax7.plot(dt, depth, color="blue", linewidth=0.5)
    ax7.set_xlabel('Sonic (DT)')
    ax7.set_xlim(200, 0)
    ax7.xaxis.label.set_color("blue")
    ax7.tick_params(axis='x', colors="blue")
    ax7.spines["top"].set_edgecolor("blue")
    ax7.set_xticks([200,  100, 0])
    ax7.text(0.05, 1.04, 200, color='blue',
             horizontalalignment='left', transform=ax7.transAxes)
    ax7.text(0.95, 1.04, 0, color='blue',
             horizontalalignment='right', transform=ax7.transAxes)
    ax7.set_xticklabels([])

    ax8.set_xticklabels([])
    ax8.text(0.5, 1.02, 'Biozones', fontweight='bold',
             horizontalalignment='left', rotation="vertical",
             transform=ax8.transAxes)

    # Adding in neutron density shading
    x1 = dens
    x2 = neut

    x = np.array(ax5.get_xlim())
    z = np.array(ax6.get_xlim())

    nz = ((x2-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

    ax5.fill_betweenx(depth, x1, nz, where=x1 >= nz,
                      interpolate=True, color='green')
    ax5.fill_betweenx(depth, x1, nz, where=x1 <= nz,
                      interpolate=True, color='yellow')

    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax5, ax7]:
        ax.set_ylim(bottomdepth, topdepth)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))

    for ax in [ax1, ax2, ax5, ax7, ax8]:
        # loop through the formations dictionary and zone colors
        for depth, color in zip(formations_dict.values(), colors):
            # use the depths and colors to shade across the subplots
            ax.axhspan(depth[0], depth[1], color=color, alpha=0.1)

    for ax in [ax2, ax3, ax4, ax5, ax6, ax7, ax8]:
        plt.setp(ax.get_yticklabels(), visible=False)

    for label, formation_mid in zip(formations_dict.keys(),
                                    formation_midpoints):
        ax8.text(0.5, formation_mid, label, rotation=0, ha='center',
                 verticalalignment='center', fontweight='bold',
                 fontsize='small')

    # Mark sequence strat picks
    for ax in [ax1, ax2, ax5, ax7]:
        # MRS 2 - B2a
        ax.axhline(y=3070, color='b', linestyle='dashed')
        # MFS 1 - B2b
        ax.axhline(y=3220, color='purple', linestyle='dashed')
        # MRS 1 - B3
        ax.axhline(y=3246, color='b', linestyle='dashed')

    plt.tight_layout()
    fig.subplots_adjust(wspace=0)
    plt.savefig('output/figure.png', dpi=300)
