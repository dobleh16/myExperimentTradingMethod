import tkinter as tk
from tkinter import messagebox

# Función para mostrar la información de acuerdo a la opción seleccionada
def mostrar_info(opcion):
    if opcion == "Comprar":
        mensaje = (
            "CUANDO ENTRAR A LA ALTA:\n"
            "1. LAS VELAS DEBEN ESTAR POR ENCIMA DE LA MEDIA MOVIL Y SER DE COLOR AZUL.\n"
            "2. Usa la pantalla 2 para entrar al trade.\n"
            "3. Ingresa cuando el oscilador se mueve de abajo a la línea superior.\n"
            "\n"
            "RECORDEMOS:\n"
            "EN LA PRIMERA PANTALLA QUE ES LA FRANJA MAS GRANDE LAS VELAS DEBEN ESTAR POR ENCIMA DE LA MEDIA MOVIL\n"
            "EN LA SEGUNDA PANTALLA QUE ES LA FRANJA DONDE VAMOS A OPERAR, LAS VELAS DEBEN ESTAR POR ENCIMA DE LA MEDIA MOVIL "
            "Y EL OSCILADOR SE DEBE MOVER DESDE ABAJO HACIA ARRIBA.\n"
            "\n"
            "CONFIGURACION DE INDICADORES:\n"
            "1. TIPO DE VELAS: HEIKEN ASHI\n"
            "2. OSCILADOR: ESTOCÁSTICO 14,3,3\n"
            "3. MOVING AVERAGE: 9, 14, 21 (LA MAS RECOMENDABLE ES LA 21)\n"
        )
    else:
        mensaje = (
            "CUANDO ENTRAR A LA BAJA:\n"
            "1. LAS VELAS DEBEN ESTAR POR DEBAJO DE LA MEDIA MOVIL Y SER DE COLOR ROJO.\n"
            "2. Usa la pantalla 2 para entrar al TRADE.\n"
            "3. Ingresa cuando el oscilador se mueve de la línea superior a la línea inferior.\n"
            "\n"
            "RECORDEMOS:\n"
            "EN LA PRIMERA PANTALLA QUE ES LA FRANJA MAS GRANDE LAS VELAS DEBEN ESTAR POR DEBAJO DE LA MEDIA MOVIL\n"
            "EN LA SEGUNDA PANTALLA QUE ES LA FRANJA DONDE VAMOS A OPERAR, LAS VELAS DEBEN ESTAR POR DEBAJO DE LA MEDIA MOVIL "
            "Y EL OSCILADOR SE DEBE MOVER DESDE ARRIBA HACIA ABAJO.\n"
            "\n"
            "CONFIGURACION DE INDICADORES:\n"
            "1. TIPO DE VELAS: HEIKEN ASHI\n"
            "2. OSCILADOR: ESTOCÁSTICO 14,3,3\n"
            "3. MOVING AVERAGE: 9, 14, 21 (LA MAS RECOMENDABLE ES LA 21)\n"
        )

    messagebox.showinfo(f"Información para {opcion}", mensaje)

# Función para mostrar el mensaje tipo LED
def mostrar_mensaje_led(mensajes):
    if mensajes:
        label_teleprompter.config(text=mensajes[0])  # Mostrar el primer mensaje
        mensajes.pop(0)  # Eliminar el mensaje mostrado
        root.after(10000, mostrar_mensaje_led, mensajes)  # Llamar de nuevo después de 10 segundos

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Método Trading Para Operaciones Binarias a la larga")
root.geometry("600x400")  # Ajustar tamaño de la ventana

# Etiqueta de introducción
label_intro = tk.Label(root, text="Selecciona una opción:", font=("Arial", 14))
label_intro.pack(pady=10)

# Opción de compra o venta
variable_opcion = tk.StringVar(value="Comprar")  # Valor por defecto

radio_compra = tk.Radiobutton(root, text="Cuando Comprar?", variable=variable_opcion, value="Comprar", font=("Arial", 12))
radio_compra.pack(anchor='w')

radio_venta = tk.Radiobutton(root, text="Cuando Vender?", variable=variable_opcion, value="Vender", font=("Arial", 12))
radio_venta.pack(anchor='w')

# Mensaje tipo LED
mensajes_teleprompter = [
    "No más de 5 operaciones por día.",
    "La franja ideal debe ser 1 hora-15 minutos.",
    "Sabiendo que la pantalla de los 15 minutos es donde vas a ejecutar las operaciones.",
    "No persigas pérdida. Si pierdes más de 2 seguidas, deja de operar por el día.",
    "Elige siempre que las operaciones terminen antes de una noticia porque, si entra en la noticia, puede afectar mucho la vela.",
    "No hagas operaciones donde veas el mercado que sube o baja mucho."
]

label_teleprompter = tk.Label(root, text="", font=("Arial", 12), wraplength=580)
label_teleprompter.pack(pady=10)

# Iniciar el teleprompter
mostrar_mensaje_led(mensajes_teleprompter)

# Botón para mostrar información
btn_mostrar = tk.Button(root, text="Mostrar Información", command=lambda: mostrar_info(variable_opcion.get()),
                        font=("Arial", 12))
btn_mostrar.pack(pady=20)

# Iniciar el loop de la interfaz
root.mainloop()
