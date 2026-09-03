import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Criação da matriz do livro
A = np.array([
    [0.95, 0.04, 0, 0],
    [0.05, 0.85, 0, 0],
    [0,    0.10, 1, 0],
    [0,    0.01, 0, 1]
])

x = np.array([1.0, 0.0, 0.0, 0.0])
dias = 100
historico = [x]

for t in range(dias):
    x = A @ x
    historico.append(x)
historico = np.array(historico)

# Configuração da figura e eixos
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, dias)
ax.set_ylim(0, 1.00)
ax.set_xlabel('Tempo $t$ (dias)')
ax.set_ylabel('$x_t$ (Percentual)')
ax.set_title('Dinâmica de Epidemia')

cores = ["#1831C2", '#CC0000', '#2E8B57', "#675238"] 
labels = ['Suscetíveis', 'Infectados', 'Recuperados', 'Falecidos']
linhas = [ax.plot([], [], lw=2, color=cores[i], label=labels[i])[0] for i in range(4)]
ax.legend(loc='center right')

# Função de animação
def atualizar(frame):
    for i in range(4):
        linhas[i].set_data(range(frame), historico[:frame, i])
    return linhas

# Criação da animação
ani = FuncAnimation(fig, atualizar, frames=len(historico), interval=30, blit=True, repeat=True, repeat_delay=3000)

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()