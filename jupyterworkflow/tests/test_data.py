import jupyterworkflow.data as jwd
import pandas as pd

def test_fremont_data():
    data = jwd.get_fremont_data()
    assert all(data.columns == [u'East', u'West', u'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
