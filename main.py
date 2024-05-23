from taskList import TaskList
from menu import Menu

listofTasks = TaskList()

menuPrincipal = Menu()
enUso = True
while enUso == True:
    menuPrincipal.printMenu()
    print('  Escribe con el teclado el número de la acción a ejecutar y pulsa Enter. ')
    accionEscogida = input()
    #estructura de selección tipò switch para las 5 opciones usando if + elif + else
    if accionEscogida == '1':
        listofTasks.printTasks()
        print("\nPulsa Enter para continuar: ")
        input()
    elif accionEscogida == '2':
        listofTasks.printTasks()
        print('\nEscribe el nombre de la variable y pulsa Enter: ')
        nombreVariable = input()
        listofTasks.addTask(nombreVariable) 
    elif accionEscogida == '3':
        listofTasks.printTasks()
        print('\nEscribe el número de la tarea que has completado y pulsa Enter: ')
        tareaCompletada = int(input()) 
        listofTasks.updateTask(tareaCompletada)
    elif accionEscogida == '4':
        listofTasks.printTasks()
        print('\nEscribe el número de la tarea que quieres eliminar y pulsa Enter: ')
        tareaEliminada = int(input()) 
        listofTasks.deleteTask(tareaEliminada)
    elif accionEscogida == '5':
        print('\nPrograma Finalizado, hasta otra\n')
        enUso = False
    else:
        print('\nSe ha introducido una opción no valida')