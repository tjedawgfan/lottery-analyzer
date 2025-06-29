"""Utilities to fetch and parse lottery drawing data.

Currently the Powerball results are downloaded from the NY Open Data portal
every time the application starts.  In a more robust environment you might
want to cache this data or store it locally to reduce network usage.
"""

import pandas as pd

def load_powerball_data(url: str = "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD"):
    """Download and parse recent Powerball drawing data.

    Parameters
    ----------
    url : str, optional
        Source CSV download URL, by default the NY Open Data API.
    """

    df = pd.read_csv(url)
    df['Draw Date'] = pd.to_datetime(df['Draw Date'])
    df = df.sort_values('Draw Date')
    df[['num1','num2','num3','num4','num5','powerball']] = df['winning_numbers'].str.split(' ', expand=True)
    df[['num1','num2','num3','num4','num5','powerball']] = df[['num1','num2','num3','num4','num5','powerball']].astype(int)
    return df
