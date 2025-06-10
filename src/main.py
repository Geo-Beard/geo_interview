from src.makeplot import makeplot
from utils.read_data import read_data
from utils.formation_utils import (formation_dict_maker,
                                   formation_midpoint_maker)


def demo_plot():
    # Read main log data
    well = read_data("data/WA1.txt")

    # Convert biozone CSV to python dict for plotting
    biozones_dict = formation_dict_maker("data/WA1_biozones.csv")
    biozone_midpoints = formation_midpoint_maker(biozones_dict)

    # Set biozone colours
    zone_colors = ["red", "blue", "green", "yellow",
                   "purple", "orange", "cyan", "black"]

    # Generate well log plot - saves to output folder
    makeplot(well['M__DEPTH'],
             well['GR'],
             well['LL8'],
             well['ILM'],
             well['ILD'],
             well['NPHI'],
             well['RHOB'],
             well['DT'],
             biozones_dict,
             0,
             3666,
             zone_colors,
             biozone_midpoints)


demo_plot()


# To add:
# - Additional logs to makeplot
# - Continue working on LogPlot class
