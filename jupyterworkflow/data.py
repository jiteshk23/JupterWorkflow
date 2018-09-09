"""
Jupyter workflow data functions
"""

import os
import urllib
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv'

def get_fremont_data(filename='Freemont.csv', url=FREMONT_URL, force_download=False):
    """Download and cache Fremont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force redownload of data

    Returns
    -------
    data: pandas.Dataframe
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urllib.urlretrieve(url, 'Freemont.csv')
    data = pd.read_csv('Freemont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)
    data.columns = ['East', 'West']
    data['Total'] = data['East'] + data['West']
    return data
