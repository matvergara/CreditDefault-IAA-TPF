import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_classifier(model, X, y, ax=None, proba = False):
    """
    Visualiza un clasificador binario en un espacio bidimensional.

    Genera un scatter plot de las clases verdaderas y superpone la frontera 
    de decisión del modelo. Si se activa `proba=True`, la visualización se 
    basa en la probabilidad predicha para la clase positiva; de lo contrario,
    usa la predicción discreta del modelo.

    Args:
        model: Modelo entrenado con métodos predict() o predict_proba().
        X: Conjunto de features con dos columnas (array o DataFrame).
        y: Vector binario con las clases reales (array o Series).
        ax: Eje de Matplotlib donde dibujar la figura. Si no se pasa, usa el actual.
        proba (bool): Si es True, se grafica la probabilidad de clase positiva;
                      si es False, se grafica la predicción discreta.

    Returns:
        None. Dibuja la visualización sobre el eje indicado.
    """
    if isinstance(X, pd.DataFrame):
        X = X.values
    if isinstance(y, pd.Series):
        y = y.values
    ax = ax or plt.gca()

    # Configuración de colores y puntos
    pallete = ['#4F69D9', '#CC403A']

    ax.scatter(
        X[y == 1, 0], 
        X[y == 1, 1],
        color=pallete[1],
        marker='o',
        s=60,
        alpha=0.6,
        edgecolors='black',
        linewidth=0.8,
        label='Default'
    )

    ax.scatter(
        X[y == 0, 0], 
        X[y == 0, 1],
        color=pallete[0],
        marker='o',  
        s=80,
        alpha=0.4,
        edgecolors='black',
        linewidth=0.8,
        label='No Default'
    )

    ax.axis('tight')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')

    ax.legend(
        loc='upper right',
        frameon=True,
        facecolor='white', 
        fontsize=12, 
        framealpha=1.0, 
        edgecolor='black'
    )

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    xx, yy = np.meshgrid(np.linspace(*xlim, num=200),
                         np.linspace(*ylim, num=200))

    
    if proba:
        Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1].reshape(xx.shape)
    else:
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)


    # Crea el plot coloreado con los resultados
    Z = -Z + 1
    ax.pcolormesh(xx,yy,Z,cmap='bwr_r', vmin = 0, vmax=1, alpha = 0.2)

    ax.set(xlim=xlim, ylim=ylim)