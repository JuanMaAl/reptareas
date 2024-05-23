from task import Task

class TaskList:
    # constructor
    def __init__(self, list = []):
        self.list = list

    # methods - start -
    #Create task
    def addTask(self, name = 'Sin nombre'):
        newTask = Task(name, False)
        self.list.append(newTask) #add new task in the list object

    #Read all tasks
    def printTasks(self):
        taskNumber = 1
        for task in self.list: #print all tasks
            print('\nNúmero: ' + str(taskNumber), end= " -> ")
            task.infoTask() #this method of the task class print the info of the current task 
            taskNumber = taskNumber + 1

    #Update task status
    def updateTask(self, number = 1):
        try: #to avoid the termination of the program if the number is not valid
            indexToUpdate = int(number) -1
            self.list[indexToUpdate].completeTask() #this method of the task class change the task statuts to complete
        except: 
            print("Error en la introducción del número de tarea")

    #Delete a task 
    def deleteTask (self, number = 1):
        try: #to avoid the termination of the program if the number is not valid
            indexToDelete = int(number) - 1
            del self.list[indexToDelete]
        except: 
            print("Error en la introducción del número de tarea")    

    # methods - end -

