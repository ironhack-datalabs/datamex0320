jugador = []
casino = []
while len(casino) !=2:
    casino.append(random.randin(1,11))
    if len(casino)== 2:
        print ("Casino tiene X", casino)
while len(jugador) !=2:
    jugador,append(random.randin(1,11))
    if len(jugador)==2:
        print ("Tienes", jugador)
        
if sum(casino)==21:
    print("Casino tiene 21!")
elif sum(casino) > 21:
    print("Casino se paso de 21!")
    
while sum(jugador)< 21:
    jugador_1 = str(input("¿Quieres otra carta Si/s o No?"))
    if jugador_1 == (s):
        jugador.append(random.randin(1,11))
        print("Tienes un total " + str(sum(jugador))+ jugador)
    else:
        print("El casino tiene un total de" + str(sum(casino)) + casino)
        print("tienes un total de " + str(sum(jugador))+ jugador)
        if sum(casino > sum(jugador)):
            print(" ¡Casino GANA!")
        else:
            print("¡HAS GANADO!")
            break
if sum(jugador) > 21:
    print("Te has pasado, casino gana")
elif sum(jugador)==21:
    print("¡BLACKJACK!")