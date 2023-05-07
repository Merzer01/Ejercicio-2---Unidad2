from classManejador import Manejador
from classViajeroFrecuente import viajerofrecuente


#AGREGAR EL INGRESO DE UN DATO INT(NUMERO DE VIAJERO) Y LLAMAR A pos=m.buscar(el dato)

def menu(m, p):
        print("-----MENU DE OPCIONES-----")
        print("1- Consultar cantidad de millas")
        print("2- Acumular millas")
        print("3- Canjear Millas")
        print("0- Salir")
        print("\n")
        m.options(p)


if __name__ == '__main__':
    m = Manejador()
    m.readArchivo()
    m.mostrar()
    dato = int(input("Ingrese numero de viajero: "))
    pos = m.buscar(dato)
    menu(m, pos)