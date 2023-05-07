class viajerofrecuente:
    __nro_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, nro, doc, nomb, ape, mill):      #CONTRUCTOR
        self.__nro_viajero = nro
        self.__dni = doc
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas_acum = mill
    def __str__(self):
        return("{} {} - {}| Nro: {} - Millas Acumuladas: {}".format(self.__apellido, self.__nombre, self.__dni, self.__nro_viajero, self.__millas_acum))
    def numviajero(self):
        return self.__nro_viajero
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    def acumularMillas(self, c):
        tot = self.__millas_acum + c
        self.__millas_acum = tot
    def canjearMillas(self, c):
        if (c <= self.__millas_acum):
            self.__millas_acum = self.__millas_acum - c
            print("¡Millas canjeadas! - Te quedan {} millas".format(self.__millas_acum))
        else:
            print("ERROR AL CANJEAR (Millas insuficientes)")