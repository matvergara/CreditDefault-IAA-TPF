import pandas as pd

def load_raw_data():
    """
    Carga datos crudos desde data/raw
    """
    dataset = pd.read_csv('../data/raw/credit_defaults.csv', sep=";", header=1)
    return dataset

def save_processed_data(df: pd.DataFrame, path):
    """
    Guarda archivo preprocesado en data/processed
    
    Args:
        df: Dataframe preprocesado
    Returns
    """
    df.to_csv(path, index=False)