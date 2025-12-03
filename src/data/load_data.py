import pandas as pd

def load_raw_data():
    """
    Carga datos crudos desde ./data/raw
    """
    dataset = pd.read_csv('../data/raw/credit_defaults.csv', sep=";", header=1)
    return dataset