import pandas as pd

def load_raw_data() -> pd.DataFrame:
    """
    Carga datos crudos desde data/raw

    Returns:
        Dataframe con datos crudos 
    """
    dataset = pd.read_csv('../data/raw/credit_defaults.csv', sep=";", header=1)
    return dataset

def save_processed_data(df: pd.DataFrame, path = '../data/processed/credit_defaults_clean.csv') -> None:
    """
    Guarda archivo preprocesado en data/processed
    
    Args:
        df: Dataframe preprocesado
        path: Ruta para guardar el csv preprocesado
    
    Returns:
        Guarda el csv en el path indicado
    """
    df.to_csv(path, index=False)