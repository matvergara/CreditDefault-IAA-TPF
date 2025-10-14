from ucimlrepo import fetch_ucirepo

def load_raw_data():
    """
    Carga datos desde UCI ML Repository.
    """
    dataset = fetch_ucirepo(id=350)
    return dataset.data.original