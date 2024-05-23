from taskList import TaskList
from menu import Menu

listofTasks = TaskList()

menuPrincipal = Menu()
enUso = True
while enUso == True:
    menuPrincipal.printMenu()
    print('  Escribe con el teclado el número de la acción a ejecutar y pulsa Enter. ')
    selectedAction = input()
    #selection like a switch for the five options using if + elif + else
    if selectedAction == '1':
        listofTasks.printTasks()
        print("\nPulsa Enter para continuar: ")
        input()
    elif selectedAction == '2':
        listofTasks.printTasks()
        print('\nEscribe el nombre de la variable y pulsa Enter: ')
        variableName = input()
        listofTasks.addTask(variableName) 
    elif selectedAction == '3':
        listofTasks.printTasks()
        print('\nEscribe el número de la tarea que has completado y pulsa Enter: ')
        completedTask = int(input()) 
        listofTasks.updateTask(completedTask)
    elif selectedAction == '4':
        listofTasks.printTasks()
        print('\nEscribe el número de la tarea que quieres eliminar y pulsa Enter: ')
        removedTask = int(input()) 
        listofTasks.deleteTask(removedTask)
    elif selectedAction == '5':
        print('\nPrograma Finalizado, hasta otra\n')
        enUso = False
    else:
        print('\nSe ha introducido una opción no valida')