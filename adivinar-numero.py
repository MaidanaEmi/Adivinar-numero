#Importación de dependencias
import random

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
        self.respuestas = []
    
    def iniciar_adivinar_numero(self):
        correcto_ingresado = False
        random_generado = self.generarRandom()
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
    
    def iniciar_pensar_numero(self):
        print("Juego 2 iniciado!")
        random_generado = self.generarRandom()
        ingresado_dic = {'numero': random_generado, 'correctas': 0, 'regulares': 0}
        self.obj_random = Numero(random_generado)
        correcto = False
        while correcto == False:
            print("¿El número que pensaste es? ", self.obj_random.numero )
            adivina = input("¿Es el número?. s/n: ")
            if adivina == "s":
                    correcto = True
                    print("¡Juego terminado!")
            else:
                ingresado_dic = {'numero': self.obj_random.numero, 'correctas': 0, 'regulares': 0}   
                # Agregar validaciones de las respuestas ingresadas!
                correc=int(input("Ingrese la cantidad de cifras correctas: "))
                reg=int(input("Ingrese la cantidad de cifras regulares: "))
                ingresado_dic['correctas'] = correc
                ingresado_dic['regulares'] = reg
                self.respuestas.append(ingresado_dic)
                self.obj_random.numero = self.adivinarNumero(ingresado_dic)    
    
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

    # def validarAleatorio(self, numero):
    #     numero_int = self.convertirNumero(numero)
    #     #numero_str = ""
    #     #Validacion si no es 9999
    #     numero_limite = str(numero_int)
    #     if numero_limite == "9999":
    #         numero_str = "0123"
    #     else:
    #         valido = False
    #         while valido == False:
    #             numero_int += 1
    #             numero_str = str(numero_int)
    #             if len(numero_str) == 3:
    #                   numero_str ='0'+ numero_str
    #             if numero_str == '9999': 
    #                   numero_int = 123
    #                   numero_str = "0123"
    #             v = obj_validacion.validacionCifrasRepetidas(numero_str)
    #             if v == False:
    #                   valido = True
        
    #     numero_lista=[int(digit) for digit in numero_str]
    #     return numero_lista
                 
        

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
    
    def adivinarNumero(self, dic):
        #self.respuestas.append(dic)
        numero_int = self.convertirNumero(dic['numero'])
        coincide = False
        while coincide == False:
            ####
            valid = False
            while valid == False:
                numero_int += 1
                numero_str = str(numero_int)
                if len(numero_str) == 3:
                      numero_str ='0'+ numero_str
                if numero_str == '9999': 
                      numero_int = 123
                      numero_str = "0123"
                v = obj_validacion.validacionCifrasRepetidas(numero_str)
                if v == False:
                      valid = True
            ####
            
            count = 0
            for d in self.respuestas:
                random_valido =[int(digit) for digit in numero_str]
                res = self.calcularCoincidencias(d['numero'],random_valido)
                if res[0] == d['correctas'] and res[1] == d['regulares']:
                    count +=1
                if count == len(self.respuestas):
                    coincide = True
                    return random_valido
        return numero_str

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
            return True #return (True,contador)
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
if opcion == 2:
    obj_juego = Juego()
    obj_juego.iniciar_pensar_numero()
