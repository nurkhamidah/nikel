import pandas as pd

nickel = pd.read_csv('data/nikel.csv', sep=';')
year = nickel['Category'].unique()
source = nickel['source'].unique()
date = nickel['date'].unique()

def lower(str):
    return str.lower()