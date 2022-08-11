# IMPORTING PACKAGES

import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import floor
from termcolor import colored as cl

from matplotlib import style
from matplotlib import rcParams


def get_historical_data(api_key, symbol, start_date, end_date):
    # api_key = "YOUR API KEY"
    api_url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&outputsize=5000&apikey={api_key}"
    raw_df = requests.get(api_url).json()
    df = pd.DataFrame(raw_df["values"]).iloc[::-1].set_index("datetime").astype(float)
    df = df[df.index >= start_date]
    df = df[df.index <= end_date]
    df.index = pd.to_datetime(df.index)
    return df


def run() -> None:
    style.use("fivethirtyeight")
    rcParams["figure.figsize"] = (20, 10)

    api_key = "b2035a9732004b5bad0c2ff8f0ef3b88"
