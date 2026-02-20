# Función para mostrar la palabra con espacios y guiones bajos
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

#Definimos el termino "palabra_aleatoria" para usarlo mas adelante
import random
#Damos valor al conjunto "palabras"
def palabra_aleatoria():
    palabras=["araña","casa","carro","programa","codigo","pasarela","carpeta", "archivo", "camara", "reloj" , "monitor", "computadora","teclado","cargador"]
    return random.choice(palabras)
#Mensaje de bienvenida
print("¡¡Bienvenido!!") 
while True:
#Opción para empezar el juego
  respuesta=input("¿Deseas jugar? (si/no): ").lower()
  if respuesta=="si" :
    print("¡Excelente! El juego comienza...")
    palabra = palabra_aleatoria()
    print("Tu palabra secreta tiene", len(palabra), "letras.")
    break
  elif respuesta=="no" :
    print("Ok,ya será otro día¡¡")
    
  else:
    print("Esa no es una opción valida, escribe 'si' o 'no'")
#Si se acepta se muestra la condición
print("tienes 5 intentos, introduce una letra")   
intentos = 5
letras_adivinadas = []
while intentos > 0:
  letra = input("Introduce una letra: ").lower()
  if letra in palabra:
     print("¡Bien! La letra está en la palabra.")
     letras_adivinadas.append(letra)
     
  else:
        intentos -= 1
        print("Fallaste. Te quedan", intentos, "intentos.")
  print(mostrar_palabra(palabra, letras_adivinadas))
# Condición de victoria
      
  if all(letra in letras_adivinadas for letra in palabra):
        print("¡Felicidades! Has adivinado la palabra:", palabra)
        break
# Condición de derrota
if intentos == 0:
    print("Lo siento, te has quedado sin intentos. La palabra era:", palabra)

print("deseas volver a jugar",)







