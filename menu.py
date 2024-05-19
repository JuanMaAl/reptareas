class Menu:
    def __init__(self, menuName = 'MENÚ REPTAREAS'):
        self.menuName = menuName
    
    def printMenu(self):
        print('\n')
        print('  ---------------' + self.menuName + '---------------' )
        print('\n      1- Ver mi lista de tareas')
        print('\n      2- Añadir una nueva tarea')
        print('\n      3- Marcar una tarea como completada')
        print('\n      4- Eliminar una tarea de la lista')
        print('\n      5- Finalizar el programa')
        print('\n  --------------------------------------------' )
        print('\n')

    