
import random
n = random.randint(1, 99)
guess = int(raw_input(“Ingrese un entero entre el 1 al 99: "))
while n != "guess":
    print
    if guess < n:
        print "guess queda subestimando“
        guess = int(raw_input("Ingrese un entero entre el 1 al 99: "))
    elif guess > n:
        print "guess queda sobreestimando“
        guess = int(raw_input("Ingrese un entero entre el 1 al 99: "))
    else:
        print “¡Adivinaste!”
        break
    print

#ahora uno de adivinar entre 1 y 36 con 5 preguntas:

n2=random.randint(1, 36)

guess2= int(raw_input(“Ingrese un entero entre el 1 al 36: ”))

while n2 != "guess":
    print
    if guess2 < n2:
        print "guess2 queda subestimando“
        guess2 = int(raw_input("Ingrese un entero entre el 1 al 36: "))
    elif guess2 > n2:
        print "guess2 queda sobreestimando“
        guess2 = int(raw_input("Ingrese un entero entre el 1 al 36: "))
    else:
        print “¡Adivinaste!”
        break
    print
