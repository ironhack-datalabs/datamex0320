#from time import *
import time                                         # Importe tiempo para darle delay al snake
import turtle                                       # Importe Turtle para usar sus métodos
import random                                       # importe ramndom para crear los puntos alatoriamente

delay = 0.14                                      # Indico que el programa tenda un delay de una decima de segundo
score = 0
hight_score = 0

print('\nListo para jugar?, Utiliza las flechas de dirección y control de tu teclado para desplazarte')
print('Recuerda que no puedes chocar con el muro y tampoco puedes chocar con el cuerpo de la Snake')
print('                             de lo contrario perderas!!!!\n')
input("Presiona Enter para empezar")

mensaje = turtle.Turtle()
mensaje.color('white')
mensaje.penup()
mensaje.hideturtle()
mensaje.goto(0,325)
mensaje.write('Este es el juego de la Snake', align= 'center', font = ('Arial',18,'normal'))

# Set Window
ventana = turtle.Screen()                           # Se crea la ventana objeto de Turtle
ventana.bgcolor('black')                             # Le configuro color a la ventana
ventana.title('Snake')                              # Le agrego título
ventana.setup(width = 700 , height = 700)            # Configuro tamaño de ventana
ventana.tracer(0)                                   # Se inicia la animación de turtle

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color('white')
marcador.penup()
marcador.hideturtle()
marcador.goto(0,302)
marcador.write('Score:       Hight Score: ', align= 'center', font = ('Arial',20,'normal'))


# Head
head = turtle.Turtle()                              # Se crea Head objeto de turtle
head.speed(0)                                       # La velocidad inicial del head
head.shape('circle')                                # Forma de cabeza snake
head.penup()                                        # Con esta instruccion no se deja rastro al desplazarse la snake
head.goto(0,0)                                      # Posición inicial de head
head.direction = 'stop'                             # Para que no se mueva la snake al empezar el juego
head.color('green')                                 # Color de la cabeza

# Body Snake
body = []                                           # Se crea lista para appendear el cuerpo que se crea en el ciclo while > if


# Points (cuerpo)

puntos = turtle.Turtle()                            # Se crea 'Puntos' objeto de turtle
puntos.speed(0)                                     # Para que aparezcan los puntos en pantalla
puntos.shape('circle')                              # Forma de los puntos (cuerpo)
puntos.penup()                                      # Con esta instruccion no se deja rastro al desplazarse la snake
puntos.goto(-200,0)                                 # Posicion inicial de los puntos
puntos.color('yellow')


# Funciones
def hacia_arriba():                                 # Para indicar que el 'head' debera tomar una dirección una vez llamado el método
    head.direction = 'up'

def hacia_abajo():                                  
    head.direction = 'down'

def hacia_la_derecha():                             
    head.direction = 'right'

def hacia_la_izquierda():                           
    head.direction = 'left'


def movimiento():                                   # Definimos método para el movimiento del Snake
    if head.direction =='up':                         
        ejey = head.ycor()
        head.sety(ejey + 20)
    
    if head.direction =='down':
        ejey = head.ycor()
        head.sety(ejey - 20)

    if head.direction =='right':
        ejex = head.xcor()
        head.setx(ejex + 20)

    if head.direction =='left':
        ejex = head.xcor()
        head.setx(ejex - 20)

ventana.listen()                                    # Aqui la ventana está pendiente de lo que presionemos en el teclado
ventana.onkeypress(hacia_arriba,'Up')               # Mandamos llamar alguna funcion para modificar dirección del 'Head'
ventana.onkeypress(hacia_abajo,'Down')
ventana.onkeypress(hacia_la_derecha,'Right')
ventana.onkeypress(hacia_la_izquierda,'Left') 

while True:                                         # Mientras la condición se cumpla
    
    ventana.update()                                # Se actualizará la ventana y el movimiento
    


    # Delimitando área ed juego

    if head.xcor() > 350 or head.xcor() < -350 or head.ycor() > 350 or head.ycor() < -350:
        time.sleep(1)
        #print('Has perdido, presiona enter para intentarlo de nuevo: ')
        #input("Presiona Enter para empezar")
        head.goto(0,0)
        head.direction = 'stop'

        for i in body:
            i.goto(2000,2000)

        body.clear()

        score = 0
        marcador.clear()
        marcador.write('Score: {}       Hight Score: {}'.format(score,hight_score), align= 'center', font = ('Arial',20,'normal'))


    # Comiendo :P

    if head.distance(puntos)<20:                    # Si la posición del 'head' es menor que 20 el cual esta entre los rangos de X y Y, se actualizará
        x = random.randint(-345,345)                # la posición del punto (puntos.goto)
        y = random.randint(-345,299)
        puntos.goto(x,y)

        add_body = turtle.Turtle()                  # Si se cumple la condición anterior se creará un nuevo objeto turtle
        add_body.speed(0)                           # Con forma,color y se posiciona en pantalla con speed(0)
        add_body.shape('circle')        
        add_body.color('green')
        add_body.penup()
        body.append(add_body)                       # Cumplido lo anterior se appendea la lista body para la longitud del snake

        score += 1


        if score > hight_score:
            hight_score = score
        marcador.clear()
        marcador.write('Score: {}       Hight Score: {}'.format(score,hight_score), align= 'center', font = ('Arial',20,'normal'))



    # Movimiento de cuerpo

    body_total = len(body)                          # Se declara que el cuerpo total es igual al número de elementos de la lista 'body'
    for i in range(body_total -1,0,-1):             # Se crea bucle para indicar que cada elemento de 'body_total' asignará diferentes cordenadas
        x = body[i -1].xcor()                       # en 'body con respecto al numero de elemetos de 'body' menos 1.
        y = body[i -1].ycor()
        body[i].goto(x,y)

    if body_total > 0:                              # Modificamos las cordenadas del 'head' tanto en X como en Y
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)                           # indicamos que para el primer elemento de 'body' las cordenadas serán las ultimas del 'head'



    movimiento()


    for b in body :
        if b.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for b in body:
                b.goto(2000,2000)
            body.clear()

            score = 0
            marcador.clear()
            marcador.write('Score: {}       Hight Score: {}'.format(score,hight_score), align= 'center', font = ('Arial',20,'normal'))




    time.sleep(delay)


# Esperar para cierre de ventana
#sleep(30)