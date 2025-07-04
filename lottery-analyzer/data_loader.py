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

    Notes
    -----
    The source CSV uses columns named ``"Draw Date"`` and ``"Winning Numbers"``.
    loader renames them to ``"draw_date"`` and ``"winning_numbers"`` for easier
    downstream processing.
    """

    df = pd.read_csv(url)
    # Normalize key columns from the CSV to lowercase names for easier use
    df.rename(columns={'Draw Date': 'draw_date',
                       'Winning Numbers': 'winning_numbers'}, inplace=True)
    df['draw_date'] = pd.to_datetime(df['draw_date'])
    df = df.sort_values('draw_date')
    df[['num1','num2','num3','num4','num5','powerball']] = df['winning_numbers'].str.split(' ', expand=True)
    df[['num1','num2','num3','num4','num5','powerball']] = df[['num1','num2','num3','num4','num5','powerball']].astype(int)
    return df
