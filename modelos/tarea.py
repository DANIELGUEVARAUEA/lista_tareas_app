# Clase que representa una tarea

class Tarea:
    def __init__(self, id_tarea, descripcion, completado=False):
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.completado = completado

    def marcar_completada(self):
        self.completado = True

    def __str__(self):
        # Formato para guardar en TXT
        return f"{self.id_tarea}|{self.descripcion}|{self.completado}"