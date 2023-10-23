
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def vecindario(arr, x, y):
    vecinos = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            vecinos += arr[(x + i) % arr.shape[0], (y + j) % arr.shape[1]]
    return vecinos - arr[x, y]

def juego_de_la_vida(arr):
    nueva_generacion = arr.copy()
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            vecinos = vecindario(arr, i, j)
            if arr[i, j] == 1:
                if vecinos < 2 or vecinos > 3:
                    nueva_generacion[i, j] = 0
            else:
                if vecinos == 3:
                    nueva_generacion[i, j] = 1
    return nueva_generacion

# Configura el tamaño del tablero y el número de generaciones
tamaño_tablero = 50
generaciones = 100

# Crea un tablero aleatorio
tablero = np.random.choice([0, 1], tamaño_tablero * tamaño_tablero).reshape(tamaño_tablero, tamaño_tablero)

# Configura la animación
fig, ax = plt.subplots()
im = ax.imshow(tablero, cmap='binary')

def actualizar(frame):
    global tablero
    tablero = juego_de_la_vida(tablero)
    im.set_array(tablero)
    return im,

ani = animation.FuncAnimation(fig, actualizar, frames=generaciones, interval=100, blit=True)
plt.show()
