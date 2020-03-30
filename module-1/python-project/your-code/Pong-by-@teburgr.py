import turtle


print("BIENVENIDO AL JUEGO DE PING PONG DE @teburgr\nPor favor, sigue las instrucciones")
nombrej1 = input("Jugador 1, escribe tu nombre: ")
nombrej2 = input("Jugador 2, escribe tu nombre: ")

#Validación de número de juegos (que sea entero positivo)
def n_juegos():
    while True:
      try:
         n = int(input("¿Hasta cuántos turnos quieren jugar?: "))
         if n > 0:
             print("Perfecto, VAMOS!")
             return n
         else:
            print("Ingresa un entero POSITIVO DIJE")

      except ValueError:
         print("Ingresa un entero positivo")
         continue

#asignación de variable de número de juegos
n = n_juegos()


#Seteo Ventana
ventana = turtle.Screen()
ventana.title("@teburgr PingPong")
ventana.bgcolor("black")
ventana.setup(width=1000, height=700)
ventana.tracer(0) #hace que la ventana se deje de actualizar hasta que nosotros digamos


#Jugador 1 SetUp
jugador1 = turtle.Turtle()
jugador1.speed(0) #esto hace que la animación sea más rápida
jugador1.shape("square") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
jugador1.color("blue")
jugador1.shapesize(stretch_wid=5, stretch_len=1)
jugador1.penup()
jugador1.goto(-440,0)
puntos_jugador1 = 0

#Jugador 2 SetUp
jugador2 = turtle.Turtle()
jugador2.speed(0) #esto hace que la animación sea más rápida
jugador2.shape("square")
jugador2.color("red")
jugador2.shapesize(stretch_wid=5, stretch_len=1)
jugador2.penup()
jugador2.goto(440,0)
puntos_jugador2 = 0

#Bola SetUp
bola = turtle.Turtle()
bola.speed(0) #esto hace que la animación sea más rápida
bola.shape("circle")
bola.color("yellow")
bola.penup()
bola.goto(0,0)
bola.velx = 4 #avance en x
bola.vely = 2 #avance en y

#pizarron SetUp
pizarron = turtle.Turtle()
pizarron.speed(0)
pizarron.color("White")
pizarron.penup()
pizarron.hideturtle() #que pasa aca?
pizarron.goto(0,320)
pizarron.write("{} - 0 ----- 0 - {}".format(nombrej1,nombrej2) , align="center", font=("Courier", 24, "normal"))  # ACTUALIZAR CON NOMBRES


#Funciones para que suba y baje jugador 1 y 2
def jugador1_arriba():
    y = jugador1.ycor()
    y += 20 #agrega 20 pixeles a la coordenada y
    jugador1.sety(y) #actualizamos el valor de la coordenada y

def jugador1_abajo():
    y = jugador1.ycor()
    y -= 20
    jugador1.sety(y)

def jugador2_arriba():
    y = jugador2.ycor()
    y += 20
    jugador2.sety(y)

def jugador2_abajo():
    y = jugador2.ycor()
    y -= 20
    jugador2.sety(y)

def cerrar_juego():
    ventana.bye()


#configuración de teclas
ventana.listen() #le dice al programa que reciba información en la ventana principal
ventana.onkeypress(jugador1_arriba,"w") #cuando presionamos w, que haga la función jugador1_arriba
ventana.onkeypress(jugador1_abajo,"s")
ventana.onkeypress(jugador2_arriba,"Up")
ventana.onkeypress(jugador2_abajo,"Down")


contador=0
#Juego principal
while contador < n:
    ventana.update()
    #mueve la bola
    bola.setx(bola.xcor() + bola.velx) #setea la primera coordenada de x y que se vaya sumando según la variable X
    bola.sety(bola.ycor() + bola.vely)

    #rebote en Y positivo
    if bola.ycor() > 340:
        bola.sety(340)
        bola.vely = bola.vely * -1

    # rebote en Y negativo
    elif bola.ycor() < -340:
        bola.sety(-340)
        bola.vely = bola.vely * -1

    # rebote en x afuera del jugador 2
    if bola.xcor() > 490:
        bola.goto(0,0)
        bola.velx *= -1
        puntos_jugador1 += 1
        pizarron.clear()
        pizarron.write("{} {} ----- {} {}".format(nombrej1, puntos_jugador1, puntos_jugador2, nombrej2), align="center", font=("Courier", 24, "normal"))
        contador += 1

    # rebote en x afuera del jugador 1
    elif bola.xcor() < -490:
        bola.goto(0,0)
        bola.velx *= -1
        puntos_jugador2 += 1
        pizarron.clear()
        pizarron.write("{} {} ----- {} {}".format(nombrej1, puntos_jugador1, puntos_jugador2, nombrej2), align="center", font=("Courier", 24, "normal"))
        contador += 1

    #choque con jugadores
    if (bola.xcor() > 440 and bola.xcor() < 450 ) and (bola.ycor() < jugador2.ycor() + 50 and bola.ycor() > jugador2.ycor() - 50 ):
        bola.setx(440)
        bola.velx *= -1

    if (bola.xcor() < -440 and bola.xcor() > -450 ) and (bola.ycor() < jugador1.ycor() + 50 and bola.ycor() > jugador1.ycor() - 50 ):
        bola.setx(-440)
        bola.velx *= -1


#victoria SetUp
victoria = turtle.Turtle()
victoria.speed(0)
victoria.color("White")
victoria.penup()
victoria.hideturtle() #que pasa aca?
victoria.goto(0,0)

#mensaje de salida SetUp
salida = turtle.Turtle()
salida.speed(0)
salida.color("yellow")
salida.penup()
salida.hideturtle()
salida.goto(0,-100)

while True:
    ventana.update()
    if puntos_jugador1 > puntos_jugador2:
        victoria.write("{} gana con {} puntos".format(nombrej1,puntos_jugador1) , align="center", font=("Courier", 50, "normal"))
        bola.hideturtle()
        salida.write("Presiona esq para salir", align="center",font=("Courier", 20, "normal"))
        ventana.onkeypress(cerrar_juego, "Escape")

    elif puntos_jugador2 > puntos_jugador1:
        victoria.write("{} gana con {} puntos".format(nombrej2,puntos_jugador2) , align="center", font=("Courier", 50, "normal"))  # ACTUALIZAR CON NOMBRES
        bola.hideturtle()
        salida.write("Presiona esq para salir", align="center",font=("Courier", 20, "normal"))
        ventana.onkeypress(cerrar_juego, "Escape")

    else:
        victoria.write("ES UN EMPATE" , align="center", font=("Courier", 50, "normal"))
        bola.hideturtle()
        salida.write("Presiona esq para salir", align="center", font=("Courier", 20, "normal"))
        ventana.onkeypress(cerrar_juego, "Escape")