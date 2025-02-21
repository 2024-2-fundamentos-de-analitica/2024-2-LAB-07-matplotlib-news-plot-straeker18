"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Siga las instrucciones del video https://youtuv.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Configuración de la figura
    plt.figure(figsize=(5, 3), dpi=300)

    # Definición de colores, orden en capas y grosores de línea
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    # Cargar datos
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Generar líneas del gráfico
    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
        )

    # Estilos del gráfico
    plt.title("How People Get Their News", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Añadir puntos y etiquetas al inicio y final de cada línea
    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        plt.scatter(first_year, df[col][first_year], color=colors[col], zorder=zorder[col])
        plt.text(first_year - 0.2, df[col][first_year], f"{col} {df[col][first_year]}%", ha="right", va="center", color=colors[col])

        plt.scatter(last_year, df[col][last_year], color=colors[col])
        plt.text(last_year + 0.2, df[col][last_year], f"{df[col][last_year]}%", ha="left", va="center", color=colors[col])

    # Configuración de los ejes
    plt.xticks(ticks=df.index, labels=df.index, ha="center")

    # Crear directorio de salida si no existe
    os.makedirs("files/plots", exist_ok=True)

    # Guardar la imagen con alta calidad
    plt.tight_layout()
    plt.savefig("files/plots/news.png", dpi=300, bbox_inches="tight")

    # Mostrar el gráfico
    plt.show()