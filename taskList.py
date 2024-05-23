from task import Task

class TaskList:
    def __init__(self, list = []):
        self.list = list

    #Create task
    def addTask(self, name = 'Sin nombre'):
        newTask = Task(name, False)
        self.list.append(newTask)

    #Read all tasks
    def printTasks(self):
        taskNumber = 1
        for task in self.list:
            print('\nNúmero: ' + str(taskNumber), end= " -> ")
            task.infoTask()
            taskNumber = taskNumber + 1

    #Update task status
    def updateTask(self, number = 1):
        try:
            indexToUpdate = int(number) -1
            self.list[indexToUpdate].completeTask()
        except:
            print("Error en la introducción del número de tarea")

    #Delete a task 
    def deleteTask (self, number = 1):
        try:
            indexToDelete = int(number) - 1
            del self.list[indexToDelete]
        except:
            print("Error en la introducción del número de tarea")    

    

