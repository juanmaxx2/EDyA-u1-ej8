class Paciente:
    __Nombre = None
    __DNI = None
    __Especialidad = None
    __Tiempo = None

    def __init__(self, nombre, dni, especialidad,tiempo):
        self.__Nombre = nombre
        self.__DNI = dni
        self.__Especialidad = especialidad
        self.__Tiempo = tiempo

    def setTiempo(self,tiempo):
        self.__Tiempo = tiempo

    def getNombre(self):
        return self.__Nombre
    
    def getDNI(self):
        return self.__DNI

    def getEspecialidad(self):
        return self.__Especialidad
    
    def getTiempo(self):
        return self.__Tiempo
    
    def __srt__(self):
        return self.__Nombre + self.__DNI + self.__Especialidad