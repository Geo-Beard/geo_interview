import pandas as pd
import logging

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
