import pandas as pd
import logging
from makeplot import makeplot
from formation_utils import formation_dict_maker, formation_midpoint_maker


logger = logging.getLogger(__name__)
logging.basicConfig(filename='./logging/errors.log',
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def read_data(data_file_path):
    try:
        dfp = data_file_path
        df = None
        if ".txt" in dfp:
            df = pd.read_table(dfp, sep=r'\s+')
        if ".csv" in dfp:
            df = pd.read_csv(dfp, sep=',')
        if df is None:
            raise Exception('Please check file path.')
        return df
    except Exception as error:
        logger.error(f'An error occurred: {error}')
        raise


def demo_plot():
    # Read main log data
    well = read_data("data/WA1.txt")
    # Read biozones
    # biozones = read_data("data/WA1_biozones.csv")

    # Convert biozone CSV to python dict for plotting
    biozones_dict = formation_dict_maker("data/WA1_biozones.csv")
    biozone_midpoints = formation_midpoint_maker(biozones_dict)

    # Set biozone colours
    zone_colors = ["red", "blue", "green", "yellow",
                   "purple", "orange", "cyan", "black"]

    # Generate well log plot - saves to output folder
    makeplot(well['M__DEPTH'],
             well['GR'],
             well['ILD'],
             well['NPHI'],
             well['RHOB'],
             None,
             biozones_dict,
             0,
             4000,
             zone_colors,
             biozone_midpoints)


demo_plot()
