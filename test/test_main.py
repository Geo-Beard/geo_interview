from src.main import read_data
import pandas as pd
import pytest


def test_read_data_returns_dataframe():
    file_path = "data/WA1.txt"
    data = read_data(file_path)
    assert isinstance(data, pd.DataFrame)


def test_read_data_returns_expected_head_txt():
    file_path = "data/WA1.txt"
    df = read_data(file_path)
    expected_columns = ['M__DEPTH',
                        'SP',
                        'GR',
                        'CALI',
                        'BitSize',
                        'LL8',
                        'ILM',
                        'ILD',
                        'RHOB',
                        'NPHI',
                        'DT',
                        'MudWgt']
    returned_columns = list(df.columns)
    assert expected_columns == returned_columns


def test_read_data_returns_expected_head_csv():
    file_path = "data/WA1_biozones.csv"
    df = read_data(file_path)
    expected_columns = ['biozone', 'top_m', 'base_m']
    returned_columns = list(df.columns)
    assert expected_columns == returned_columns


def test_read_data_returns_error_if_incorrect_path():
    with pytest.raises(Exception) as e:
        file_path = 'incorrect_path'
        read_data(file_path)
    assert 'Please check file path.' in str(e.value)
