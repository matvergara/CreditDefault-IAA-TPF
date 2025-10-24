import pandas as pd
from pathlib import Path

def load_raw_data():
    """
    Carga datos crudos desde ./data/raw
    """
    ruta = Path(__file__).resolve().parents[2] / "data" / "raw" / "credit_defaults.csv"
    dataset = pd.read_csv(ruta, sep=";", header=1)
    return dataset