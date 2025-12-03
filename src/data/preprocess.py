"""
Módulo de preprocesamiento de datos crudos
"""

import pandas as pd
from src.data import load_data as ld

def eliminar_id(df: pd.DataFrame):
    """
    Elimina la primer columna ID que no es necesaria para el análisis

    Args:
        df: DataFrame original

    Returns:
        Dataframe con columna ID eliminada
    """

    df = df.copy()
    df.drop('ID', axis=1, inplace=True)
    return df

def generar_nombres_columnas_meses():
    """
    Genera los nombres de columnas para meses de deuda, pago y factura

    Returns:
        Tupla con listas de nombres: (meses_deuda, meses_pago, meses_factura)
    """
    meses = ['abr','may','jun','jul','ago','sep']
    meses_deuda = [f'meses_deuda_{mes}' for mes in meses]
    meses_pago = [f'pago_{mes}' for mes in meses]
    meses_factura = [f'factura_{mes}' for mes in meses]
    return meses_deuda, meses_pago, meses_factura

def renombrar_columnas(df: pd.DataFrame):
    """
    Renombra las columnas del DataFrame con nombres descriptivos.

    Args:
        df: DataFrame con columnas originales

    Returns:
        Dataframe con columnas renombradas
    """
    meses_deuda, meses_pago, meses_factura = generar_nombres_columnas_meses()

    nuevas_cols = (
        ['limite_credito','genero','educacion','estado_civil','edad'] + meses_deuda + meses_pago + meses_factura + ['default_oct']
    )
    
    df = df.copy()
    df.columns = nuevas_cols
    return df

def normalizar_categorias(df):
    """
    Normaliza las categorías de educación y estado civil.

    - Educación: agrupa categorías 0, 5, 6 en 4 (otros)
    - Estado civil: agrupa categoría 0 en 3 (otros)

    Args:
        df: DataFrame con categorías originales

    Returns:
        DataFrame con categorías normalizadas
    """
    df = df.copy()

    # Valores no documentados de educación -> categoría "otros" 
    df['educacion'] = df['educacion'].replace({0: 4, 5: 4, 6: 4})

    # Valores no documentados de estado civil -> categoría "otros"
    df['estado_civil'] = df['estado_civil'].replace({0: 3})
    
    return df

def validar_transiciones_deuda(historial: pd.Series) -> bool:
    """
    Valida que las transiciones entre estados de deuda sean lógicas.
    
    Reglas:
    - De no consumo (-2, -1) no puede saltar a 2+ meses de atraso
    - De pago mínimo (0) no puede saltar a 3+ meses de atraso
    - De atraso no puede incrementar más de 1 mes
    
    Args:
        historial: Serie con estados de deuda mensuales
        
    Returns:
        True si las transiciones son válidas, False en caso contrario
    """
    prev = historial.iloc[0]
    
    for nxt in historial.iloc[1:]:
        # De no consumo/pago completo no puede saltar a 2+ meses
        if prev in [-2, -1] and nxt >= 2:
            return False
        
        # De revolving no puede saltar a 3+ meses
        if prev == 0 and nxt >= 3:
            return False
        
        # Los atrasos no pueden incrementar más de 1 mes
        if prev >= 1 and nxt > prev + 1:
            return False
        
        prev = nxt
    
    return True

def filtrar_inconsistencias_deuda(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra registros con transiciones de deuda ilógicas.
    
    Args:
        df: DataFrame con columnas de meses_deuda
        
    Returns:
        DataFrame sin registros con transiciones inválidas
    """
    meses_deuda, _, _ = generar_nombres_columnas_meses()
    mask_validos = df[meses_deuda].apply(validar_transiciones_deuda, axis=1)
    
    registros_eliminados = (~mask_validos).sum()
    print(f"Registros eliminados por inconsistencias de deuda: {registros_eliminados}")
    
    return df[mask_validos].copy()

def filtrar_inconsistencias_factura_pago(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra registros donde el pago es mayor que la factura sin deuda previa.
    
    Elimina casos anómalos donde:
    - Pago de septiembre > factura de septiembre
    - Sin deuda en septiembre ni agosto
    
    Args:
        df: DataFrame con columnas de factura, pago y deuda
        
    Returns:
        DataFrame sin registros inconsistentes
    """
    condicion_anomala = (
        (df['factura_sep'] < df['pago_sep']) &
        (df['meses_deuda_sep'] < 0) &
        (df['meses_deuda_ago'] < 0)
    )
    
    registros_eliminados = condicion_anomala.sum()
    print(f"Registros eliminados por inconsistencias factura-pago: {registros_eliminados}")
    
    return df[~condicion_anomala].copy()

def seleccionar_columnas_septiembre(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selecciona solo columnas demográficas, de septiembre y target.
    
    Args:
        df: DataFrame completo
        
    Returns:
        DataFrame con columnas seleccionadas
    """
    columnas_base = ['limite_credito', 'genero', 'educacion', 'estado_civil', 'edad']
    columnas_sep = [col for col in df.columns if 'sep' in col]
    columnas_target = ['default_oct']
    
    columnas_seleccionadas = columnas_base + columnas_sep + columnas_target
    return df[columnas_seleccionadas].copy()

def preprocesar_datos(df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Pipeline completo de preprocesamiento.
    
    Args:
        df: DataFrame opcional. Si no se proporciona, carga datos raw.
        
    Returns:
        DataFrame preprocesado
    """
    if df is None:
        df = ld.load_raw_data()
    
    print("Iniciando preprocesamiento...")
    print(f"Registros iniciales: {len(df)}")
    
    df = eliminar_id(df)
    df = renombrar_columnas(df)
    df = normalizar_categorias(df)
    df = filtrar_inconsistencias_deuda(df)
    df = filtrar_inconsistencias_factura_pago(df)
    df = seleccionar_columnas_septiembre(df)
    
    print(f"Registros finales: {len(df)}")
    print("Preprocesamiento completado.")

    
    
    return df

if __name__ == "__main__":
    df_procesado = preprocesar_datos()
    print(f"\nShape final: {df_procesado.shape}")
    print(f"\nColumnas: {df_procesado.columns.tolist()}")