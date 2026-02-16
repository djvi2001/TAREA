#Definimos el termino "palabra_aleatoria" para usarlo mas adelante
import random
#Damos valor al conjunto "palabras"
def palabra_aleatoria():
    palabras=["araña","casa","carro","programa","codigo","computadora","teclado","cargador"]
    return random.choice(palabras)
print("¡¡Bienvenido!!") 
while True:
  respuesta=input("¿Deseas jugar? (si/no): ").lower()
  if respuesta=="si" :
    print("¡Excelente! El juego comienza...")
    palabra = palabra_aleatoria()
    print("Tu palabra secreta tiene", len(palabra), "letras.")
    break
  elif respuesta=="no" :
    print("Ok,ya será otro día¡¡")
    break
  else:
    print("Esa no es una opción valida, escribe 'si' o 'no'")
print("tienes 5 intentos, introduce una letra")   
intentos = 5
letras_adivinadas = []
while intentos > 0:
  letra = input("Introduce una letra: ").lower()
  if letra in palabra:
     print("¡Bien! La letra está en la palabra.")
     letras_adivinadas.append
  else:
        intentos -= 1
        print("Fallaste. Te quedan", intentos, "intentos.")

progreso = ""
for l in palabra:
  if l in letras_adivinadas:
    progreso += l + " "
  else:
     progreso += "_ "
print("Progreso:", progreso)






