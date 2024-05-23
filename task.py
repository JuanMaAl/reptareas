class Task:

  # constructor
  def __init__(self, name, status):
        self.name = name
        self.status = status

  # methods
  def infoTask(self): # print the task name and the task status
    actualStatus = "Pendiente"
    if self.status:
      actualStatus = "Completada"
    print("Tarea: " + self.name + " -> Estado: " + actualStatus)

  def completeTask(self): #change the status attribute
    self.status = True