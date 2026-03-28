# Lógica del sistema (encapsulada)

from modelos.tarea import Tarea
import os


class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.archivo = "tareas.txt"
        self.cargar_tareas()

    # --------- ARCHIVO TXT ---------
    def guardar_tareas(self):
        with open(self.archivo, "w") as f:
            for tarea in self.tareas:
                f.write(str(tarea) + "\n")

    def cargar_tareas(self):
        if not os.path.exists(self.archivo):
            return

        with open(self.archivo, "r") as f:
            for linea in f:
                id_tarea, descripcion, completado = linea.strip().split("|")
                tarea = Tarea(int(id_tarea), descripcion, completado == "True")
                self.tareas.append(tarea)

    # --------- El CRUD ---------
    def agregar_tarea(self, descripcion):
        nuevo_id = len(self.tareas) + 1
        tarea = Tarea(nuevo_id, descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()

    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.marcar_completada()
        self.guardar_tareas()

    def eliminar_tarea(self, id_tarea):
        self.tareas = [t for t in self.tareas if t.id_tarea != id_tarea]
        self.guardar_tareas()

    def listar_tareas(self):
        return self.tareas