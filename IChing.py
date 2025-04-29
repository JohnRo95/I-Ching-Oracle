import random
import tkinter as tk
from tkinter import ttk

# Diccionario de los 64 hexagramas (número: (nombre en chino, representación binaria invertida, nombre común))
ICHING = {
    1: ("乾", [1, 1, 1, 1, 1, 1], "El Creador"),
    2: ("坤", [0, 0, 0, 0, 0, 0], "El Receptivo"),
    3: ("屯", [1, 0, 0, 0, 1, 0], "La Dificultad Inicial"),
    4: ("蒙", [0, 1, 0, 0, 0, 1], "La Necedad Juvenil"),
    5: ("需", [1, 1, 1, 0, 1, 0], "La Espera"),
    6: ("訟", [0, 1, 0, 1, 1, 1], "El Conflicto"),
    7: ("師", [0, 0, 0, 1, 0, 1], "El Ejército"),
    8: ("比", [1, 0, 1, 0, 0, 0], "La Unión"),
    9: ("小畜", [1, 1, 1, 1, 0, 1], "El Poder Domesticador de lo Pequeño"),
    10: ("履", [1, 0, 1, 1, 1, 0], "La Conducta"),
    11: ("泰", [1, 1, 1, 0, 0, 0], "La Paz"),
    12: ("否", [0, 0, 0, 1, 1, 1], "El Estancamiento"),
    13: ("同人", [1, 0, 0, 0, 0, 1], "La Comunidad con el Hombre"),
    14: ("大有", [1, 1, 1, 0, 0, 1], "La Posesión de lo Grande"),
    15: ("謙", [0, 0, 0, 1, 1, 0], "La Modestia"),
    16: ("豫", [0, 1, 1, 1, 0, 0], "El Entusiasmo"),
    17: ("隨", [1, 0, 0, 1, 1, 0], "El Seguimiento"),
    18: ("蠱", [0, 1, 1, 0, 0, 1], "La Corrupción"),
    19: ("臨", [1, 1, 0, 0, 0, 0], "El Acercamiento"),
    20: ("觀", [0, 0, 0, 0, 1, 1], "La Contemplación"),
    21: ("噬嗑", [1, 0, 0, 1, 0, 1], "La Mordedura Jugosa"),
    22: ("賁", [1, 0, 0, 1, 1, 1], "La Gracia"),
    23: ("剝", [0, 0, 0, 0, 0, 1], "El Despojamiento"),
    24: ("復", [1, 0, 0, 0, 0, 0], "El Retorno"),
    25: ("无妄", [1, 1, 1, 0, 0, 1], "La Inocencia"),
    26: ("大畜", [1, 0, 0, 1, 1, 1], "El Gran Poder Domesticador"),
    27: ("頤", [1, 0, 0, 0, 0, 1], "La Nutrición"),
    28: ("大過", [0, 1, 1, 1, 1, 0], "La Gran Preponderancia"),
    29: ("坎", [0, 1, 0, 0, 1, 0], "Lo Abismal"),
    30: ("離", [1, 0, 1, 1, 0, 1], "Lo Adherente"),
    31: ("咸", [0, 0, 1, 1, 1, 0], "La Influencia"),
    32: ("恆", [0, 1, 1, 1, 0, 0], "La Duración"),
    33: ("遯", [0, 0, 1, 1, 1, 1], "La Retirada"),
    34: ("大壯", [1, 1, 1, 1, 0, 0], "El Gran Poder"),
    35: ("晉", [0, 0, 0, 1, 0, 0], "El Progreso"),
    36: ("明夷", [0, 0, 1, 0, 0, 0], "El Oscurecimiento de la Luz"),
    37: ("家人", [1, 1, 0, 1, 0, 1], "La Familia"),
    38: ("睽", [1, 0, 1, 0, 0, 1], "La Oposición"),
    39: ("蹇", [0, 0, 1, 0, 1, 1], "La Obstrucción"),
    40: ("解", [1, 1, 0, 1, 0, 0], "La Liberación"),
    41: ("損", [0, 0, 1, 0, 0, 1], "La Disminución"),
    42: ("益", [1, 0, 0, 1, 1, 0], "El Aumento"),
    43: ("夬", [1, 1, 1, 1, 1, 0], "La Irrupción"),
    44: ("姤", [0, 1, 1, 1, 1, 1], "El Encuentro"),
    45: ("萃", [0, 0, 0, 1, 1, 0], "La Reunión"),
    46: ("升", [0, 1, 1, 0, 0, 0], "El Ascenso"),
    47: ("困", [0, 1, 0, 1, 1, 0], "El Acosamiento"),
    48: ("井", [0, 1, 1, 0, 1, 0], "El Pozo"),
    49: ("革", [1, 0, 1, 1, 1, 0], "La Revolución"),
    50: ("鼎", [0, 1, 1, 1, 0, 1], "El Caldero"),
    51: ("震", [1, 0, 0, 1, 0, 0], "El Trueno"),
    52: ("艮", [0, 0, 1, 0, 0, 1], "La Quietud"),
    53: ("漸", [0, 0, 1, 1, 1, 0], "El Desarrollo"),
    54: ("歸妹", [1, 0, 0, 1, 1, 1], "La Muchacha que se Casa"),
    55: ("豐", [1, 0, 1, 1, 1, 1], "La Abundancia"),
    56: ("旅", [1, 1, 1, 0, 1, 1], "El Viajero"),
    57: ("巽", [0, 1, 1, 0, 1, 1], "Lo Suave"),
    58: ("兌", [1, 1, 0, 1, 1, 0], "Lo Sereno"),
    59: ("渙", [0, 1, 0, 0, 0, 0], "La Dispersión"),
    60: ("節", [0, 0, 0, 1, 1, 1], "La Limitación"),
    61: ("中孚", [1, 1, 0, 0, 1, 1], "La Verdad Interior"),
    62: ("小過", [0, 0, 1, 1, 0, 0], "La Preponderancia de lo Pequeño"),
    63: ("既濟", [1, 0, 1, 0, 1, 0], "Después de la Cruzada"),
    64: ("未濟", [0, 1, 0, 1, 0, 1], "Antes de la Cruzada"),
}

def tirar_moneda():
    return 3 if random.choice(["Cara", "Cruz"]) == "Cara" else 2

def generar_linea():
    resultado_monedas = [tirar_moneda() for _ in range(3)]
    suma = sum(resultado_monedas)
    if suma == 9:
        return 1, True
    elif suma == 6:
        return 0, True
    elif suma == 8:
        return 1, False
    elif suma == 7:
        return 0, False

def generar_hexagrama():
    hexagrama = []
    mutando = False
    for _ in range(6):
        linea, mutacion = generar_linea()
        hexagrama.append(linea)
        if mutacion:
            mutando = True
    return list(reversed(hexagrama)), mutando

def encontrar_hexagrama(hexagrama_generado):
    for numero, (nombre_chino, representacion, nombre_comun) in ICHING.items():
        if representacion == hexagrama_generado:
            return numero, nombre_chino, nombre_comun
    return None, None, None

def dibujar_hexagrama_tk(canvas, hexagrama, x, y, escala=20):
    ancho_linea = 5 * escala
    alto_linea = 1 * escala
    separacion = 1 * escala

    for i, linea in enumerate(hexagrama):
        y_pos = y + i * (alto_linea + separacion)
        x_centro = x

        if linea == 1:  # Yang
            canvas.create_line(x_centro - ancho_linea / 2, y_pos, x_centro + ancho_linea / 2, y_pos, width=2)
        else:  # Yin
            canvas.create_line(x_centro - ancho_linea / 2, y_pos, x_centro - ancho_linea / 4 - 2, y_pos, width=2)
            canvas.create_line(x_centro + ancho_linea / 4 + 2, y_pos, x_centro + ancho_linea / 2, y_pos, width=2)

def mostrar_resultado():
    pregunta = pregunta_entry.get()
    resultado_text.delete(1.0, tk.END)
    hexagrama_principal, mutacion = generar_hexagrama()
    numero_principal, nombre_chino_principal, nombre_comun_principal = encontrar_hexagrama(hexagrama_principal)

    resultado_text.insert(tk.END, f"Pregunta: {pregunta}\n\n")
    resultado_text.insert(tk.END, "Hexagrama Principal:\n")
    dibujar_hexagrama_tk(canvas, hexagrama_principal, 150, 100)
    resultado_text.insert(tk.END, f"Número: {numero_principal}\n")
    resultado_text.insert(tk.END, f"Nombre Chino: {nombre_chino_principal}\n")
    resultado_text.insert(tk.END, f"Nombre Común: {nombre_comun_principal}\n")

    if mutacion:
        hexagrama_mutado = [(1 - linea) for linea in hexagrama_principal]
        numero_mutado, nombre_chino_mutado, nombre_comun_mutado = encontrar_hexagrama(hexagrama_mutado)
        resultado_text.insert(tk.END, "\nHexagrama Mutado:\n")
        dibujar_hexagrama_tk(canvas, hexagrama_mutado, 400, 100)
        resultado_text.insert(tk.END, f"Número: {numero_mutado}\n")
        resultado_text.insert(tk.END, f"Nombre Chino: {nombre_chino_mutado}\n")
        resultado_text.insert(tk.END, f"Nombre Común: {nombre_comun_mutado}\n")

    resultado_text.insert(tk.END, "\nQue la sabiduría del I Ching te guíe desde León, Guanajuato.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Oráculo del I Ching")

# Etiqueta y entrada para la pregunta
pregunta_label = ttk.Label(ventana, text="¿Qué es lo que quieres saber hoy?")
pregunta_label.pack(pady=10)
pregunta_entry = ttk.Entry(ventana, width=50)
pregunta_entry.pack(pady=5)

# Botón para generar el resultado
generar_boton = ttk.Button(ventana, text="Consultar el I Ching", command=mostrar_resultado)
generar_boton.pack(pady=10)

# Lienzo para dibujar los hexagramas
canvas = tk.Canvas(ventana, width=600, height=250)
canvas.pack(pady=10)

# Área de texto para mostrar el resultado textual
resultado_text = tk.Text(ventana, height=10, width=70)
resultado_text.pack(pady=10)

ventana.mainloop()