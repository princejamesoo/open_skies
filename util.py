"""
@File : util.py
@Author: James Obakpolor
@Date : 2024/11/21
"""
import pandas as pd


def convertCode(code, airportsFile='airports.csv'):
    airports = pd.read_csv(airportsFile)
    length = len(code)
    if length == 3:
        return airports.loc[airports['iata'] == code, 'icao'].values[0]
    elif length == 4:
        return airports.loc[airports['icao'] == code, 'iata'].values[0]


def findCountry(code, airportsFile='airports.csv'):
    airports = pd.read_csv(airportsFile)
    length = len(code)
    if length == 3:
        return airports.loc[airports['iata'] == code, 'country'].values[0]
    elif length == 4:
        return airports.loc[airports['icao'] == code, 'country'].values[0]
