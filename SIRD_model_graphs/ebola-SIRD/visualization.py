import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from config import *

def plotar_grafico(df_dados: pd.DataFrame, titulo: str, y_scale: str, y_lim=(0, 1)):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_xlim(0, len(df_dados) - 1)
    ax.set_ylim(*y_lim)
    ax.set_yscale(y_scale)
    ax.set_xlabel('Dias')
    ax.set_ylabel('Proporção da População')
    ax.set_title(titulo)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    linhas = {}
    for i, coluna in enumerate(df_dados.columns):
        linhas[coluna], = ax.plot([], [], label=labels[i], color=colors[i], lw=2)
        
    ax.legend(loc='center right')
    texto_dia = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=10)

    def init():
        for linha in linhas.values(): linha.set_data([], [])
        texto_dia.set_text('')
        return list(linhas.values()) + [texto_dia]

    def update(frame):
        x = list(range(frame + 1))
        for col, linha in linhas.items():
            linha.set_data(x, df_dados[col].iloc[:frame + 1])
        texto_dia.set_text(f'Dia {frame}')
        return list(linhas.values()) + [texto_dia]

    anim = FuncAnimation(fig, update, frames=len(df_dados), init_func=init, blit=False, interval=80)
    plt.close()
    return HTML(anim.to_jshtml())