from paciente import Paciente
from colaEncadenada import ColaE
from colaSecuencial import ColaS
import random

if __name__ == "__main__":
    tiempoSimulacion = (4*60)
    tiempoLlegada = 1
    tiempoAtencionTurnos = 2
    tiempoAtencionEspecialidades = 20
    tiempoEspecialidades = []
    colaTurnos = ColaE()
    colaEspecialidades = []
    cantsinTurnos = 0
    cantEspecialidadesAtendidas = []
    sumEspecialidades = []
    for i in range(4):
        colaEspecialidades.append(ColaS(10))
        tiempoEspecialidades.append(tiempoAtencionEspecialidades+1)
        sumEspecialidades.append(0)
        cantEspecialidadesAtendidas.append(0)
    tiempoActualTurnos = tiempoAtencionTurnos + 1
    cantTurnosAtendidos = 0 
    reloj = 0
    for i in range(tiempoSimulacion):
        num = random.random()
        if num<(1/tiempoLlegada):
            colaTurnos.insertar(Paciente('a',3,random.randint(0,4),reloj))
        if reloj<60:
            if tiempoActualTurnos == tiempoAtencionTurnos + 1:
                if colaTurnos.vacio() == False:
                    pacienteEnTurnos = colaTurnos.suprimir()
                    tiempoActualTurnos = tiempoAtencionTurnos
            else:
                tiempoActualTurnos -= 1
                if tiempoActualTurnos == 0:
                    sumEsperas = reloj - pacienteEnTurnos.getTiempo()
                    cantTurnosAtendidos +=1
                    pacienteEnTurnos.setTiempo(reloj)
                    if colaEspecialidades[pacienteEnTurnos.getEspecialidad()].lleno() == False:
                        colaEspecialidades[pacienteEnTurnos.getEspecialidad()].insertar(pacienteEnTurnos)
                    else:
                        cantsinTurnos +=1
                    tiempoActualTurnos = tiempoAtencionTurnos + 1
        else:
            if colaTurnos.vacio() == False:
                for i in range(colaTurnos.getCantidad()):
                    colaTurnos.suprimir()
                    cantsinTurnos += 1
        for i in range(len(colaEspecialidades)):
            if tiempoEspecialidades[i] == tiempoAtencionEspecialidades+1:
                if colaEspecialidades[i].vacio() == False:
                    paciente = colaEspecialidades[i].suprimir()
                    sumEspecialidades[i] += reloj - paciente.getTiempo()
                    tiempoEspecialidades[i] = tiempoAtencionEspecialidades
                    cantEspecialidadesAtendidas[i] += 1
            else:
                tiempoEspecialidades[i] -= 1
                if tiempoEspecialidades[i] == 0:
                    tiempoEspecialidades[i] = tiempoAtencionEspecialidades + 1
    print("\nLa cantidad de personas que no pudieron obtener el turno: {}".format(cantsinTurnos))
    print("El tiempo promedio de espera para sacar turnos es: {}".format(sumEsperas/cantTurnosAtendidos))
    for i in range(4):
        promedio = 0
        if cantEspecialidadesAtendidas[i] != 0:
            promedio = sumEspecialidades[i]/cantEspecialidadesAtendidas[i]
        print("El tiempo promedio de espera para la especialidad {} es: {}".format(i+1,promedio))