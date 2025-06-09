from utils.read_data import read_data
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def find_peaks_troughs():
    # Read data
    file = "data/WA1.txt"
    well = read_data(file)

    # Grab depth and gamma
    depth = well['M__DEPTH']
    gamma = well['GR']

    # Detect peaks
    peaks, _ = find_peaks(gamma)

    # Detect troughs
    troughs, _ = find_peaks(-gamma)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(depth, gamma, label='Gamma Ray')
    plt.plot(depth[peaks], gamma[peaks], 'ro', label='Peaks')
    plt.plot(depth[troughs], gamma[troughs], 'go', label='Troughs')
    plt.gca().invert_yaxis()  # Depth increases downward
    plt.xlabel('Depth (m)')
    plt.ylabel('Gamma Ray')
    plt.legend()
    plt.title('Peaks and Troughs in Gamma Ray Log')
    plt.show()


find_peaks_troughs()
