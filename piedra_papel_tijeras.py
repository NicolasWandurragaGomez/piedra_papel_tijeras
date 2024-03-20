from random import *


# input

print("------¡BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERA------")


eleccion_usuario = input("ingrese su desicion: ")

# processing


def piedra_papel_tijera():
 opciones = ["piedra", "papel", "tijera"]
 return random.choice(opciones)



 if eleccion_usuario == "piedra":
      
    if eleccion_computadora == "piedra":
            print(" ¡EMPATE! ")

    elif eleccion_computadora == "papel":
            print(" ¡PERDISTE! ")


    elif eleccion_computadora == "tijera":
       print(" ¡GANASTE! ")



 if eleccion_usuario == "papel":
      
       if eleccion_computadora == "papel":
            print(" ¡EMPATE! ")

       elif eleccion_computadora == "piedra":
            print(" ¡GANASTE! ")


       elif eleccion_computadora == "tijera":
            
        print(" ¡PERDISTE! ")


 if eleccion_usuario == "tijera":
       
   if eleccion_computadora == "tijera":
            print(" ¡EMPATE! ")

   elif eleccion_computadora == "papel":
            print(" ¡GANASTE! ")


   elif eleccion_computadora == "piedra":
       
       print(" ¡PERDISTE! ")
    
  


 

       


                   


        
        
        