#rotativa
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, scrolledtext


def generar_tabla_sudoku_trig(numeros):
    tabla = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            num = random.choice(numeros)
            # Calcular seno y escalar al rango 1-105
            val = int((math.sin(math.radians(num)) + 1) * 52.5)
            val = max(1, min(val, 105))
            tabla[i][j] = val
    return tabla


def mostrar_tabla_texto(tabla):
    filas = []
    for i, fila in enumerate(tabla):
        fila_str = " ".join(f"{num:3d}" for num in fila)
        filas.append(fila_str)
        if (i + 1) % 3 == 0 and i != 8:
            filas.append("-" * 29)
    return "\n".join(filas)


def mostrar_imagen(tabla):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.matshow(np.ones((9, 9)), cmap="Pastel1")
    for (i, j), val in np.ndenumerate(tabla):
        ax.text(j, i, str(val), va='center', ha='center', fontsize=14)

    for k in range(10):
        lw = 2 if k % 3 == 0 else 1
        ax.axhline(k - 0.5, color='black', linewidth=lw)
        ax.axvline(k - 0.5, color='black', linewidth=lw)
    ax.axis('off')
    plt.title("Rotativa")
    plt.show()


def validar_numeros(entrada):
    try:
        numeros = list(map(int, entrada.strip().split()))
        if 1 <= len(numeros) <= 30 and all(1 <= n <= 105 for n in numeros):
            return numeros
        else:
            return None
    except ValueError:
        return None


def on_generar():
    entrada = entrada_numeros.get()
    numeros = validar_numeros(entrada)
    if numeros is None:
        messagebox.showerror("Error", "Debe ingresar entre 1 y 30 números, todos entre 1 y 105, separados por espacios.")
        return

    global tabla_generada
    tabla_generada = generar_tabla_sudoku_trig(numeros)
    texto_tabla = mostrar_tabla_texto(tabla_generada)
    output_text.config(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, texto_tabla)
    output_text.config(state='disabled')


def on_mostrar_imagen():
    global tabla_generada
    if tabla_generada is None:
        messagebox.showwarning("Atención", "Primero genere la tabla.")
    else:
        mostrar_imagen(tabla_generada)


root = tk.Tk()
root.title("Generador de tabla estilo Sudoku con función trigonométrica")

tk.Label(root, text="Ingrese entre 1 y 30 números (1-105) separados por espacios:").pack(padx=10, pady=5)
entrada_numeros = tk.Entry(root, width=50)
entrada_numeros.pack(padx=10, pady=5)

btn_generar = tk.Button(root, text="Generar tabla con seno", command=on_generar)
btn_generar.pack(padx=10, pady=5)

output_text = scrolledtext.ScrolledText(root, width=35, height=15, state='disabled', font=("Consolas", 12))
output_text.pack(padx=10, pady=5)

btn_imagen = tk.Button(root, text="Mostrar imagen del resultado", command=on_mostrar_imagen)
btn_imagen.pack(padx=10, pady=5)

tabla_generada = None

root.mainloop()
