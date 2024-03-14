import turtle
import time
import random

delay = 100  # Delay espresso in millisecondi invece di secondi

# Impostazioni dello schermo
win = turtle.Screen()
win.title("Snake Retro Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Testa del serpente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Cibo per il serpente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Testo punteggio
score = 0
high_score = 0
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Punteggio: 0  Record: 0", align="center", font=("Courier", 24, "normal"))

# Funzioni
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Tastiera
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_left, "a")
win.onkeypress(go_right, "d")

# Funzione per gestire il movimento del serpente
def move_snake():
    if head.direction != "stop":
        move()

        # Controlla collisioni con il bordo dello schermo
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            reset_game()

        # Controlla collisione con il cibo
        if head.distance(food) < 20:
            move_food()
            add_segment()
            update_score(10)

        # Controlla collisioni con il corpo del serpente
        for segment in segments:
            if segment.distance(head) < 20:
                reset_game()

    win.update()
    turtle.ontimer(move_snake, delay)

# Funzione per muovere il cibo
def move_food():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

# Funzione per aggiungere un segmento al serpente
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

# Funzione per aggiornare il punteggio
def update_score(points):
    global score, high_score
    score += points
    if score > high_score:
        high_score = score
    text.clear()
    text.write("Punteggio: {}  Record: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Funzione per riavviare il gioco
def reset_game():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    update_score(-score)

# Avvia il gioco
move_snake()

# Avvia la finestra principale di Turtle
win.mainloop()
