
##Juego de la Ruleta
from tabulate import tabulate
import random
#lISTA\DICT relación número-color
Numerosl = [[0.0,"verde"], [0," verde"], [1, "rojo"], [2, "negro"], [3, "rojo"], [4,"negro"], [5, "rojo"], [6, "negro"],
           [7, "rojo"], [8,"negro"], [9,"rojo"], [10,"negro"], [11,"negro"], [12,"rojo"], [13,"negro"], [14,"rojo"],
           [15,"negro"], [16,"rojo"], [17,"negro"], [18,"rojo"], [19,"rojo"], [20,"negro"], [21,"rojo"], [22,"negro"],
           [23,"rojo"], [24,"negro"], [25,"rojo"], [26,"negro"], [27,"rojo"], [28,"negro"], [29,"negro"], [30,"rojo"],
           [31,"negro"], [32,"rojo"], [33,"negro"], [34,"rojo"]]

Numeros = ({

    0.0: "verde", 0:" verde", 1: "rojo", 2: "negro", 3: "rojo", 4:"negro", 5: "rojo", 6: "negro", 7: "rojo", 8:"negro",
    9:"rojo", 10:"negro", 11:"negro", 12:"rojo", 13:"negro", 14:"rojo", 15:"negro", 16:"rojo", 17:"negro", 18:"rojo",
    19:"rojo", 20:"negro", 21:"rojo", 22:"negro", 23:"rojo", 24:"negro", 25:"rojo", 26:"negro", 27:"rojo", 28:"negro",
    29:"negro", 30:"rojo", 31:"negro", 32:"rojo", 33:"negro", 34:"rojo",
})

#BIENVENIDA DEL JUEGO
print("Bienvenido a LuckyLand Casino")
print("JUGUEMOS RULETA")
print("       ")
print("Para Jugar RULETA es necesario que haga mínimo 5 apuestas en los diferentes números")
print("       ")

print(tabulate(Numerosl))

apuesta = []

# APUESTA NUMEROS
NA = input("Apuestas por favor (separadas por espacio):")
NJ = NA.split()
apuesta.append(NJ)
while len(NJ) < 5:
    NA = input("Son mínimo 5 apuestas:")
    NJ = NA.split()

# APUESTA COLOR

CA = input("Apuestas a color (negro, rojo):")
while CA == "negro" or CA == "rojo":
    apuesta.append(CA)
    print("Hiciste", len(NJ), "apuestas")
    print("Tus Numeros", NJ)
    print("Tu apuesta es:", CA)
    print("VAMOS A JUGAR (TIRA LA BOLA")

    break
else:
    print("No hay apuesta, la RULETA sigue")
    print("Hiciste", len(NJ), "apuestas")
    print("Tus Numeros", NJ)
    print("VAMOS A JUGAR(TIRA LA BOLA)")


#RULETA
resultado=[]
key = random.choice(list(Numeros))
for i in Numeros:
  if i == key:
    print("La bola cayó:",i, Numeros[i])
    resultado.append(i)
    resultado.append(Numeros[i])
print(resultado)

#PAGO
while resultado in apuesta:
  print("GANA LA CASA!")
  break
else:
    print("GANAS!")

def JN ():
    print("Más apuestas?")
    return input("Apuestas por favor (separadas por espacio):")
    Na.append(JN)
