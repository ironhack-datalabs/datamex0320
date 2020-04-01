import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras = 'ironhack datos analisis informacion python estudiante desafio curso futuro'.split()

def RandomWord(lista):
    RandomWord=random.randint(0,len(lista))
    return lista[RandomWord]

def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print("")
    fin = " "
    print('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print(letra, fin)
    print("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): 
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: 
        print(letra, fin)
    print("")

def elijeLetra(algunaLetra):
    while True:
        print('Que letra deseas escoger?:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print('Hay que escribir usa sola letra XD') 
        elif letra in algunaLetra:
            print('Ya usaste esta letra, prueba otra  ;)')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Recuerda que solo puedes escribir una letra, numeros no :S')
        else:
            return letra

def empezar():
    print('\n')
    print('Te gustaria volver a jugar?  :D  (Si o No)')
    return input().lower().startswith('s')
print('\n        Juguemos...         ')
print('A * H * O * R * C * A * D * O')
print('   Tienes solo 6 intentos')
letraIncorrecta = ""
letraCorrecta = ""
palabraSecreta = RandomWord(palabras)
finJuego = False
while True:
    displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
    letra = elijeLetra(letraIncorrecta + letraCorrecta)
    if letra in palabraSecreta:
        letraCorrecta = letraCorrecta + letra
        letrasEncontradas = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letraCorrecta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print('\n\nExelente!!!!!! la palabra secreta era:  "' + palabraSecreta + '" Ganaste!!! Urraaaa!!!')
            finJuego = True
    else:
        letraIncorrecta = letraIncorrecta + letra
        if len(letraIncorrecta) == len(AHORCADO) - 1:
            displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
            print('Uy te quedaste sin intentos :( \nDespues de ' + str(len(letraIncorrecta)) + ' letras malas y ' + str(len(letraCorrecta)) + ' letras correctas \nla palabra que debias adivinar  era... "' + palabraSecreta + '"')
            print('\n')
            print('Has ahorcado a tu personaje XP')
            finJuego = True
    if finJuego:
        if empezar():
            letraIncorrecta = ""
            letraCorrecta = ""
            finJuego = False
            palabraSecreta = RandomWord(palabras)
        else:
            break