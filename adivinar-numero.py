#Importación de dependencias
import numpy as np
import random

#Clase Numero
class Numero:

    def __init__(self):
        #self.numero = np.array(numero)
        self.numero = []
        self.cantCifras = 4
        self.error = ""
    
    def validarNumero(self,numeroi):
        ve = self.validacionEntero(numeroi)
        vc = self.validacionCantCifras(numeroi)
        vr = self.validacionCifrasRepetidas(numeroi)
        if ve == False:
            self.error="¡Ingresa un número!"
            return False
        if vc == False:
            self.error="¡Ingresa un número de {} cifras.!".format(self.cantCifras)
            return False
        if  vr == True:
            self.error="¡Las cifras no deben repetirse!. Intenta con otro número."
            return False
        return True

    def validacionEntero(self,numero):
        if numero.isdigit():
            return True
        else:
            return False

    def validacionCantCifras(self,numero):
        if len(numero) != self.cantCifras:
            return False
        else:
            return True

    def validacionCifrasRepetidas(self,numero):
        arr = list(numero)
        contador = 0
        for cifra in arr:
            if arr.count(cifra)>1:
                contador +=1
                
        if contador > 1:
            return True
        else:
            return False
#Clase Juego
class Juego:
    obj_numero = Numero()
    #obj_random = Numero()

    def __init__(self):
        self.valido = False
        self.countCorrectas = 0
        self.countRegulares = 0
        #self.nr = self.generarAleatorio()
        #self.objrandom = Numero(self.nr)
        #self.obj_numero = Numero(numeroi)
    
    def iniciar_juego(self):

        while self.valido == False:
            numeroi = input('Estoy pensando en un número. ¿Puedes adivinar cuál es?: ')
            self.valido = self.obj_numero.validarNumero(numeroi)
            if self.valido == False:
                print("Error: {}".format(self.obj_numero.error))
            else: 
                print("Puedes jugar!")

#Bloque principal
obj_juego = Juego()
obj_juego.iniciar_juego()
