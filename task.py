class Task:
  def __init__(self, name, status):
        self.name = name
        self.status = status

  def infoTask(self):
    actualStatus = "Pendiente"
    if self.status == True:
      actualStatus = "Completada"
    print("Tarea: " + self.name + "\nEstado de la tarea: " + actualStatus)