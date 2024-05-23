class Task:
  def __init__(self, name, status):
        self.name = name
        self.status = status

  def infoTask(self):
    actualStatus = "Pendiente"
    if self.status:
      actualStatus = "Completada"
    print("Tarea: " + self.name + " -> Estado: " + actualStatus)

  def completeTask(self):
    self.status = True