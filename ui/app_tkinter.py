import tkinter as tk
from tkinter import messagebox


class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # --------- ENTRY ---------
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Evento ENTER (teclado)
        self.entry.bind("<Return>", self.evento_enter)

        # --------- LISTBOX ---------
        self.lista = tk.Listbox(root, width=40)
        self.lista.pack(pady=10)

        # Evento doble clic (ratón)
        self.lista.bind("<Double-1>", self.evento_doble_click)

        # --------- BOTONES ---------
        tk.Button(root, text="Añadir Tarea", command=self.agregar).pack(pady=5)
        tk.Button(root, text="Marcar Completada", command=self.completar).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar).pack(pady=5)

        self.actualizar_lista()

    # --------- EVENTOS ---------
    def evento_enter(self, event):
        self.agregar()

    def evento_doble_click(self, event):
        self.completar()

    # --------- FUNCIONES ---------
    def agregar(self):
        texto = self.entry.get()

        if texto == "":
            messagebox.showwarning("Error", "Ingrese una tarea")
            return

        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        indice = seleccion[0]
        tarea = self.servicio.listar_tareas()[indice]

        self.servicio.completar_tarea(tarea.id_tarea)
        self.actualizar_lista()

    def eliminar(self):
        seleccion = self.lista.curselection()

        if not seleccion:
            return

        indice = seleccion[0]
        tarea = self.servicio.listar_tareas()[indice]

        self.servicio.eliminar_tarea(tarea.id_tarea)
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.servicio.listar_tareas():
            texto = tarea.descripcion

            if tarea.completado:
                texto = "[✔] " + texto

            self.lista.insert(tk.END, texto)