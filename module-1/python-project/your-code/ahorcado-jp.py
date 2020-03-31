# Importa random para escoger una palabra al aleatorea.
import random
import sys
import pykakasi
# Mis graficos mejorados de ASCII a Emoji porque pues millenial.
# Los apostrofes son para imprimir la etapa del juego.
AHORCADOEMOJI = ['''

  ➕➖➖➖➖➕
  🔽       🏿🏿
           🏾🏾
           🏿🏿
           🏾🏾
           🏿🏿
👼🟫👼🟫👼🟫👼''', '''

  ➕➖➖➖➖➕
  🔽       🏿🏿
  😓       🏾🏾
           🏿🏿
           🏾🏾
           🏿🏿
🟫👽🟫👽🟫👽🟫''', '''

  ➕➖➖➖➖➕
  🔽       🏿🏿
  😰       🏾🏾
  🟡       🏿🏿
           🏾🏾
           🏿🏿
👹🟫👹🟫👹🟫👹''', '''

  ➕➖➖➖➖➕
  🔽       🏿🏿
  😭       🏾🏾
🤚🟡       🏿🏿
           🏾🏾
           🏿🏿
🟫👻🟫👻🟫👻🟫''', '''

  ➕➖➖➖➖➕
  🔽       🏿🏿
  😰       🏾🏾
🤚🟡🤚     🏿🏿
           🏾🏾
           🏿🏿
🟫😈🟫😈🟫😈🟫''', '''

  ➕➖➖➖➖➕
  🔽       🏿🏿
  😬       🏾🏾
🤚🟡🤚     🏿🏿
🦶         🏾🏾
           🏿🏿
🧨🧨🧨🧨🧨🟫🟫''', '''

  ➕➖➖➖➖➕
  🔽       🏾💀
  🔽       💀🏿
  💀       🏾💀
           💀🏿
           🏾💀
🔥🔥🔥🔥🔥💀🏿''']
# diccionario con 4 catergorias. Me gustaría cambiarlo por algo mas interesante
palabras = {'動物・どうぶつ':'あり さる アナグマ コウモリ クマ ビーバー\
                     ねこ　へび とら しか いぬ\
                     アヒル きつね かえる\
                     ライオン トカゲ ねずみ カワウソ'.split(),
         '形・かたち':'しかく さんかく まる'.split(),
         '果物・くだもの':'りんご オレンジ ライム レモン なし スイカ ぶどう グレープフルーツ\
                   さくらんぼ バナナ マンゴ いちご'.split(),
         '色・いろ':'あか オレンジ きいろ みどり あおい むらさき しろ\
                   くろ ちゃいろ'.split()}
# Esta función genera una palabra aleatorea del diccionario: palabraKey
# despues obtiene el index de la palabra seleccionada
# regresa tanto la palabra como su index
def palabraAletorea(DictPalabras):
    palabraKey = random.choice(list(DictPalabras.keys()))
    palabraIndex = random.randint(0, len(DictPalabras[palabraKey]) - 1)
    return [DictPalabras[palabraKey][palabraIndex], palabraKey]

# Visualización del tablero del juego, donde imprime tanto los graficos de Emoji
# y el estado del juego segun las letras equivocadas, correctas, y por adivinar
def tablero(AHORCADOEMOJI, letrasequivocadas, letrascorrectas, palabrasecreta):
    print(AHORCADOEMOJI[len(letrasequivocadas)])
    print()

    print('Equivocaciones:', end=' ')
    for palabra in letrasequivocadas:
        print(palabra, end=' ')
    print()

    vacios = '_' * len(palabrasecreta)

    for i in range(len(palabrasecreta)):
        if palabrasecreta[i] in letrascorrectas:
            vacios = vacios[:i] + palabrasecreta[i] + vacios[i+1:]

    for palabra in vacios:
        print(palabra, end=' ')
    print()

# Esta función funciona como input del juego. Toma una palabra y la convierte
# en minusculas y comprueba que solo sea una letra. También comprueba que
# si la letra ya fue usada o no. También comprueba que esa letra esta en el
# abecedario y que no sea un número.
def adivina(adivinadas):
    while True:
        print('Venga, adivina una letra, sin miedo:👾👾👾')
        adivinar = str(input())
        adivinar = adivinar.lower()

        if len(adivinar) != 1:
            print('Vamos alegre, te dije solo UNA letra...UNA, ONE, HITOTSU, Uma')
        elif adivinar in adivinadas:
            print('Perooo que pashaaaa!!何それ〜〜!!, esa letra ya la escogiste.🈳')
        elif adivinar not in 'abcdefghijklmnñopqrstuvwxyzあいうえおかきくけこ\
                              さしすせそたちつてとなにぬねのはひふへほまみむめもやゆよ\
                              んらりるれろがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ\
                              アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフ\
                              ヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾ\
                              ダヂヅデドバビブベボパピプペポー':
            print('Vamos alegre, que te digo una LETRA, 🈳')
        else:
            return adivinar

# Esta función es para darle continuidad al juego, que realmente con cualquier
# letra que no sea s el programa termina.
def playAgain():
    print('¿Te gustaría jugar nuevamente? (si[S] or no[N])')
    return input().lower().startswith('s')

# Mi super banner con ASCII art pense hacer las graficas con la misma tematica
# para las etapas del horcado pero escogí Emoji. Para la version 2.0
print("""
╔═══╦╗░░░░░░░░░░░░░░╔╗░░░
║╔═╗║║░░░░░░░░░░░░░░║║░░░
║║░║║╚═╦══╦═╦══╦══╦═╝╠══╗
║╚═╝║╔╗║╔╗║╔╣╔═╣╔╗║╔╗║╔╗║
║╔═╗║║║║╚╝║║║╚═╣╔╗║╚╝║╚╝║
╚╝░╚╩╝╚╩══╩╝╚══╩╝╚╩══╩══╝

\n
╔╦╗▒▒╔╗▒▒▒╔╗▒▒▒▒▒▒▒▒▒▒▒▒▒╔╗╔╦╗▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
║╔╬═╗║╚╦═╗║╠╦═╗╔═╦╦═╗▒╔╦╗║╚╝╠╬╦╦═╗╔═╦═╗╔═╦╦═╗▒
║╚╣╬╚╣╔╣╬╚╣═╣╬╚╣║║║╬╚╗║║║║╔╗║║╔╣╬╚╣╬║╬╚╣║║║╬╚╗
╚╩╩══╩═╩══╩╩╩══╩╩═╩══╝╠╗║╚╝╚╩╩╝╚══╬╗╠══╩╩═╩══╝
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╚═╝▒▒▒▒▒▒▒▒▒╚═╝▒▒▒▒▒▒▒▒▒

\n
╔╗▒▒▒▒╔═╗▒▒╔╦╗▒▒▒▒▒╔══╗▒▒▒▒▒▒▒╔╗▒
║╚╦╦╦╗║╔╬═╦╝╠╬═╦╦═╗║═╦╬═╦╦╦╦╦═╣╚╗
║╬║║╠╣║╚╣╬║╬║║║║║╬║║╔╝║╩╣╔╣╔╣╩╣╔╣
╚═╬╗╠╝╚═╩═╩═╩╩╩═╬╗║╚╝▒╚═╩╝╚╝╚═╩═╝
▒▒╚═╝▒▒▒▒▒▒▒▒▒▒▒╚═╝▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\n
Tu aventura aprendiendo Japonés comienza aprendiendo los dos alfabetos básicos:\n
Hiragana (ひらがな) y Katakana (カタカナ)\
Para perfeccionar tu lectura y rápidez usaremos el viejo juego del horcado.\n
Venga, que con un par de juegos por día veráz resultados muy buenos. \


""")

# reset para cuando el juego comienza nuevamente
letrasequivocadas = ''
letrascorrectas = ''
palabrasecreta, secretoKey = palabraAletorea(palabras)
finJuego = False

# Mientras el juego esta activo: Imprime la categoria del diccionario así como
# la funcion del tablero que hace la Visualización del estado del juego. Llama
# a la función que controla el input del jugador junto con sus comprobaciones.
# Con esto actualiza las letras correctas y vuelve a llamar la función.
# Tiene una variable para controlar si hayo todas las letras y finaliza el juego
# sino actualiza las letras equivocadas. Si el numero de letras equivocadas es
# igual a la longitud del emoji imprime el tablero eso quiero decir que fallo
# 6 veces y termina el juego con un status de los aciertos y equivocaciones
# y le muestra al jugador la palabra correcta.
# En este punto se llama a la funcion del fin del juego y se hace reset a todas
# las variables para el siguiente juego.

#TL;DR Basicamente el curpo y cerebro del juego.
while True:
    print('La categoria es: ' + secretoKey)
    print('La palabra es: ' + palabrasecreta)
    tablero(AHORCADOEMOJI, letrasequivocadas, letrascorrectas, palabrasecreta)
    adivinar = adivina(letrasequivocadas + letrascorrectas)

    if adivinar in palabrasecreta:
        letrascorrectas = letrascorrectas + adivinar
        encontroTodasLetras = True
        for i in range(len(palabrasecreta)):
            if palabrasecreta[i] not in letrascorrectas:
                encontroTodasLetras = False
                break
        if encontroTodasLetras:
            print('Siiiii! La palabra secreta es: "' + palabrasecreta + '"! Haz ganado!')
            finJuego = True
    else:
        letrasequivocadas = letrasequivocadas + adivinar
        if len(letrasequivocadas) == len(AHORCADOEMOJI) - 1:
            tablero(AHORCADOEMOJI, letrasequivocadas, letrascorrectas, palabrasecreta)
            print('Se te han acabado las oportunidades para adivinar!\nDespues de ' + str(len(letrasequivocadas)) + ' equivocacione(s) y ' + str(len(letrascorrectas)) + ' intentos correctos, la palabra era: "' + palabrasecreta + '"')
            finJuego = True

    if finJuego:
        if playAgain():
            letrasequivocadas = ''
            letrascorrectas = ''
            finJuego = False
            palabrasecreta, secretoKey = palabraAletorea(palabras)
        else:
            break
