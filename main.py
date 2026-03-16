import tkinter as tk
from tkinter import messagebox

# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = entrada_tarea.get().strip()

    if tarea == "":
        messagebox.showwarning("Campo vacío", "Por favor, ingrese una tarea.")
        return

    lista_tareas.insert(tk.END, tarea)
    entrada_tarea.delete(0, tk.END)

# Función para limpiar el campo o eliminar la tarea seleccionada
def limpiar_tarea():
    seleccion = lista_tareas.curselection()

    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        entrada_tarea.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas Personales")
ventana.geometry("450x350")
ventana.resizable(False, False)

# Título principal
titulo = tk.Label(
    ventana,
    text="Gestor de Tareas Personales",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Frame para entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

label_tarea = tk.Label(frame_entrada, text="Nueva tarea:")
label_tarea.grid(row=0, column=0, padx=5)

entrada_tarea = tk.Entry(frame_entrada, width=30)
entrada_tarea.grid(row=0, column=1, padx=5)

# Frame para botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    width=12,
    command=agregar_tarea
)
btn_agregar.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    width=12,
    command=limpiar_tarea
)
btn_limpiar.grid(row=0, column=1, padx=10)

# Etiqueta para lista
label_lista = tk.Label(ventana, text="Tareas registradas:")
label_lista.pack()

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=45, height=10)
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
