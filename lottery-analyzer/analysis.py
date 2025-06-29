"""Utility functions for analyzing lottery numbers.

These helpers operate on :class:`pandas.DataFrame` objects that contain
Powerball drawing data.  They provide a minimal API for determining hot
and cold numbers based on historical draws and for computing a simple
trend score for user-selected numbers.
"""

from collections import Counter


def get_number_frequencies(df, cols):
    """Return a ``Counter`` of number frequencies.

    Parameters
    ----------
    df : :class:`pandas.DataFrame`
        DataFrame containing the drawing data.
    cols : list[str]
        Column names holding individual numbers.

    Returns
    -------
    collections.Counter
        Frequency count of all provided columns combined.
    """

    return Counter(df[cols].values.flatten())


def top_n(freqs, n=5):
    """Return the ``n`` most common numbers.

    ``freqs`` can be either a :class:`collections.Counter` or any mapping of
    numbers to counts.
    """

    counter = Counter(freqs)
    return [num for num, _ in counter.most_common(n)]


def bottom_n(freqs, n=5):
    """Return the ``n`` least common numbers."""

    counter = Counter(freqs)
    return [num for num, _ in counter.most_common()[:-n - 1:-1]]


def estimate_probability(numbers, freqs):
    """Calculate a simple trend score for the provided numbers.

    Parameters
    ----------
    numbers : Iterable[int]
        Numbers selected by the user.
    freqs : Mapping[int, int]
        Frequency counts obtained from :func:`get_number_frequencies`.

    Returns
    -------
    float
        ``sum(freq[n] for n in numbers) / total_draws``
    """

    total = sum(freqs.values())
    return sum(freqs.get(n, 0) for n in numbers) / total


def find_duplicate_draws(df):
    """Return drawing combinations that occurred more than once.

    Parameters
    ----------
    df : :class:`pandas.DataFrame`
        DataFrame containing columns ``num1`` through ``num5`` and ``powerball``.

    Returns
    -------
    :class:`pandas.DataFrame`
        Table of duplicated combinations with a ``count`` column showing how
        many times each occurred.
    """

    combo_cols = ['num1', 'num2', 'num3', 'num4', 'num5', 'powerball']
    dup = df.groupby(combo_cols).size().reset_index(name='count')
    dup = dup[dup['count'] > 1]
    return dup.sort_values('count', ascending=False)

