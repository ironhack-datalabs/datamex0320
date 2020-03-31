
import random

Rick = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

words = "rick morty meeseeks beth jerry jessica summer snuffles poopybutthole birdperson abradolf unity icet armaghedon annie goldenfold tammy gearhead joyce leonard".split()

def palabra(lista):
    palabra1 = random.randint(0, len(lista)-1)
    return lista[palabra1]

def ahorcado(Rick, letras_erroneas, letras_correctas, secreto):
    print(Rick[len(letras_erroneas)])
    print()

    print("Morty Ayuuuuu (eructo) daaaaa!: ", end = " ")
    for l in letras_erroneas:
        print(l, end = ' ')
    print()

    blanks = "_"*len(secreto)

    for i in range(len(secreto)): 
        if secreto[i] in letras_correctas:
            blanks = blanks[:i] + secreto[i] + blanks[i+1:]

    for l in blanks: 
        print(l, end = " ")
    print()

def adivina(x):
    
    while True:
        print("Show me what you got!")
        adv = input()
        adv = adv.lower()
        if len(adv) != 1:
            print("Morty deja de ser tan estupido como tu padre, solo puedes poner una letra")
        elif adv in x:
            print("Escucha, Morty, odio decirte esto pero eso que la gente llama 'amor' es sólo una reacción química que obliga a los animales a reproducirse. Enfocate en la Ciencia. Esa letra ya la usaste")
        elif adv not in "abcdefghijklmnopqrstuvwxyz":
            print("Estás creciendo, Morty. Creciendo como una enorme espina dentro de mi trasero. Solo usa letras")
        else:
            return adv

def otravez():
    print("Wubba Lubba Dub Dub, Morty quieres ir a otra aventura? (oh geez(si)esto parece esclavitud con etapas extra(no))")
    return input().lower().startswith("s")


print("Oh geeez! Rick fue colgado por un personaje de la serie de Rick y Morty. Tienes que salvarlo!")
print("Adivina quien fue el personaje que colgo a Rick")
print("Rick")
letras_erroneas = ''
letras_correctas = ''
secreto = palabra(words)
d = False


while True:
    ahorcado(Rick, letras_erroneas, letras_correctas, secreto)
    adv = adivina(letras_erroneas + letras_correctas)

    if adv in secreto:
        letras_correctas = letras_correctas + adv

        
        win = True
        for i in range(len(secreto)):
            if secreto[i] not in letras_correctas:
                win = False
                break
        if win:
            print("Wubba luba dub dub! Me salvaste Morty, la palabra secreta es", secreto)
            d = True
    else:
        letras_erroneas = letras_erroneas + adv

        
        if len(letras_erroneas) == len(Rick)-1:
            ahorcado(Rick, letras_erroneas, letras_correctas, secreto)
            print("El universo es basicamente un animal, crea una infinidad de idiotas solo para comerselos.\nMorty no me pudiste salvar despues de: ",str(len(letras_erroneas)),"intentos, ", "Morty solo tenias que typear esto!!","'", secreto,"'")
            d = True

        
        if d:
            if otravez():
                letras_erroneas = ''
                letras_correctas = ''
                d = False
                secreto = palabra(words)
            else:
                break