from task import Task

class TaskList:
    def __init__(self, list = []):
        self.list = list

    def addTask(self, name = 'Sin nombre'):
        newTask = Task(name, False)
        self.list.append(newTask)

    def printTasks(self):
        taskNumber = 1
        for task in self.list:
            print('\nNúmero: ' + str(taskNumber))
            task.infoTask()
            taskNumber = taskNumber + 1
