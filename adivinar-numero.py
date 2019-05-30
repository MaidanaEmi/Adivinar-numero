#Importación de dependencias
import random
import unittest

#Clase Numero
class Numero:

    def __init__(self, numero):
        self.numero = numero    
    
#Clase Juego
class Juego:

    def __init__(self):
        self.cantCifras = 4
        self.error = ""
        self.coinciden = False
    
    def iniciar_adivinar_numero(self):
        correcto_ingresado = False
        random_generado = self.generarRandom() #[1,2,3,4]
        self.obj_random = Numero(random_generado)

        while correcto_ingresado == False:
            numero_ingresado = input('Ingresa un número de 4 cifras que no se repitan: ')
            valido_ingresado = obj_validacion.validarNumero(numero_ingresado)
            
            if valido_ingresado == False:
                print("Error:", obj_validacion.error)
            else: 
                ingresado_lista = [int(digit) for digit in numero_ingresado]
                self.obj_ingresado = Numero(ingresado_lista)
                resultado = self.calcularCoincidencias(self.obj_ingresado.numero,self.obj_random.numero)
                if self.coinciden == True:
                    numero_int = self.convertirNumero(ingresado_lista)
                    print("¡Adivinaste!. El número es: ", numero_int)
                    correcto_ingresado = True
                    break
                else:
                    print("Cantidad de cifras correctas: ", resultado[0])
                    print("Cantidad de cifras regulares: ", resultado[1])
                    print("¡Intenta con otro número!")
    
    def Rand(self):
        num = 4
        start = 0
        end = 9
        random_lista = [] 
        for j in range(num): 
            random_lista.append(random.randint(start, end)) 
        return random_lista

    
    def generarRandom(self):
        valido = False        
        while valido == False:
            random_lista = self.Rand() #Se crea el aleatorio como una lista
            validacion = obj_validacion.validacionCifrasRepetidas(random_lista)
            if validacion == False:
                valido = True            
        return random_lista

    def calcularCoincidencias(self,n1,n2):
        correctas = 0
        regulares = 0
        if n1==n2:
            self.coinciden = True
        else:
            self.coinciden = False
            for i in n1:
                for j in n2:
                    if i == j:
                        if n1.index(i)== n2.index(j):
                            correctas += 1
                        else:
                            regulares +=1

        return (correctas,regulares)
    
    def convertirNumero(self,numero_lista):
        numero_str = [str(i) for i in numero_lista]
        numero_int = int("".join(numero_str))
        return numero_int

# Clase Validacion
class Validacion:

    def __init__(self):
        self.cantCifras = 4
        self.error = ""
        
    def validarNumero(self,numero_ingresado):
       
        ve = self.validacionEntero(numero_ingresado)
        vc = self.validacionCantCifras(numero_ingresado)
        vr = self.validacionCifrasRepetidas(numero_ingresado)
        if ve == False:
            self.error="¡Ingresa un número!"
            return False
        if vc == False:
            self.error="¡Ingresa un número de {} cifras! ".format(self.cantCifras)
            return False
        if  vr == True:
            self.error="¡Las cifras no deben repetirse!. Intenta con otro número."
            return False
        return True

    def validacionEntero(self,numero):
        numero_str = str(numero) 
        if numero_str.isdigit():
            return True
        else:
            return False

    def validacionCantCifras(self,numero):
        if len(numero) != self.cantCifras:
            return False
        else:
            return True

    def validacionCifrasRepetidas(self,numero):
        contador = 0
        for cifra in numero:
            if numero.count(cifra)>1:
                contador +=1                
        if contador > 1:
            return True
        else:
            return False

#Bloque principal
obj_validacion = Validacion()
print("Ingresa 1 si quieres ser el adivinador ")
print("Ingresa 2 si quieres ser el pensador ")
opcion = int(input("Opción: "))

if opcion == 1:
    obj_juego = Juego()
    obj_juego.iniciar_adivinar_numero()

# UnitTest

class PruebaJuego(unittest.TestCase):
    def test_calcularCoincidencias(self):
        self.assertEqual(obj_juego.calcularCoincidencias([1,2,3,4],[1,9,6,8]),(1,0))
        self.assertEqual(obj_juego.calcularCoincidencias([1,2,3,4],[4,3,2,1]),(0,4))
        self.assertEqual(obj_juego.calcularCoincidencias([1,2,3,4],[5,6,7,8]),(0,0))
        self.assertEqual(obj_juego.calcularCoincidencias([1,2,3,4],[4,2,3,1]),(2,2))
    
    def test_convertirNumero(self):
        self.assertEqual(obj_juego.convertirNumero([1,2,3,4]),1234)
    
class PruebaValidacion(unittest.TestCase):
    def test_validarNumero(self):
        self.assertEqual(obj_validacion.validarNumero([9,9,1,4]),False)
        self.assertEqual(obj_validacion.validarNumero([1,2,3,4]),True)
    
    def test_validarEntero(self):
        self.assertEqual(obj_validacion.validacionEntero(['a','d','f','r']),False)

    def test_validarCantCifras(self):
        self.assertEqual(obj_validacion.validarNumero([1,2,3]),False)

    def test_validarCifrasRepetidas(self):
        self.assertEqual(obj_validacion.validacionCifrasRepetidas([1,2,3,1]),True)

if __name__ == "__main__":
    unittest.main()
