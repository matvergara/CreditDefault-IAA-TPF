import pandas as pd

def load_raw_data(ruta="./data/raw/credit_defaults.csv"):
    """
    Carga datos crudos desde ./data/raw
    """
    dataset = pd.read_csv(ruta, sep=";", header=1)
    return dataset