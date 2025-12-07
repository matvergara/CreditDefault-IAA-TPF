import matplotlib.pyplot as plt
import seaborn as sns

def set_custom_style():
    """
    Configura el estilo de los gráficos.
    
    Args:
        None
        
    Returns:
        None
    """
    # Paleta de colores estándar
    my_palette = ["#2E4057", "#4F69D9", "#06D6A0", "#CC403A", "#FFD166"]
    
    # 2. Configurar el tema base de Seaborn
    sns.set_theme(style="white", palette=my_palette)
    
    # 3. Ajustes finos con Matplotlib (rcParams)
    plt.rcParams.update({
        'font.family': 'sans-serif',        # Fuente limpia
        'axes.spines.top': False,           # Quitar borde superior
        'axes.spines.right': False,         # Quitar borde derecho
        'axes.spines.left': True,           # Mantener eje Y
        'axes.spines.bottom': True,         # Mantener eje X
        'axes.grid': True,                  # Activar grilla
        'grid.alpha': 0.3,                  # Grilla sutil (transparencia)
        'grid.linestyle': '--',             # Grilla punteada
        'axes.titlesize': 14,               # Tamaño título
        'axes.titleweight': 'bold',         # Título en negrita
        'axes.labelsize': 12,               # Tamaño etiquetas ejes
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'figure.figsize': (10, 6),           # Tamaño por defecto de la figura
        'figure.dpi': 300
    })
    
    print("Estilo de gráficos aplicado correctamente.")