from Imagenes import FIGURAS                                                                   #Importa las figuras de aorcado del documento Imagenes 
from bullet import Password  # muy importante -pip3 install bullet

def mostrar_pantalla (palabra_oculta, intentos):                                               #Imprime la figura del ahorcado por intento
    print(chr(27)+'[0;46m'+'{}\n\n{}'.format(FIGURAS[intentos], palabra_oculta))
    print('___-___-___-___-___-___-___-___-___')

def run():
    print(input('El tema a tratar es: \t '))
    cli = Password('Escribe la palabra: ')                                                     #Introducir la palabra a adivinar sin que el otro man la vea
    palabra = cli.launch().lower()
    palabra_oculta = ['-'] * len(palabra)                                                      #lista con los mismos espacios vacios que los caracteres de la palabra
    intentos = 0                                                                               #inicializa variable intentos en 0

    while True:                                                                                #bucle del juego
        mostrar_pantalla (palabra_oculta, intentos)
        letra_actual = str (input ('Escribe una letra: ')).lower()                             #pide la entrada de un caracter
        indices_letra = [idx for idx in range (len (palabra)) if palabra[idx] == letra_actual] #revisa si la letra introducida esta 
        #                                                                                       en alguno de los indices de la palabra
        if len(indices_letra) == 0:                                                            #si ningun caracter coincide agrega un intento 
            intentos += 1                                                                      #contador de intentos

            if intentos == 7:                                                                  #limita los intentos a 7
                mostrar_pantalla (palabra_oculta, intentos)                                    #pasa las variables actuales a la funcion para mostrar pantalla
                print('\n¡Es una pena! Perdiste. \nLa palabra correcta era: {}'.format(palabra))     #mensaje si un usuario pierde
                break
        else:
            for idx in indices_letra:                                                          #sustituye el espacio vacio en palabra oculta por la letra acual
                palabra_oculta[idx] = letra_actual

        if ('-') not in palabra_oculta:
            print('\n¡Felicidades! Ganaste. \nLa palabra es: {}'.format(palabra))              #comprueba si ya no hay indices vacios
            break

if __name__ == '__main__':
    print(chr(27)+'[0;46m'+'\tJ U E G O    A H O R C A D O S')                                 #Titulo del juego, (chr(27)+'[0;46m'+) comando anterior de (código ascii 27) cambia color de fondo
    run()      