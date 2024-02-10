import random
import time
import turtle

delay = 0.1

# Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Wall
wall = turtle.Turtle()
wall.hideturtle()
wall.speed(0)
wall.color("white")
wall.penup()
wall.goto(-310, 310)
wall.pendown()

for _ in range(4):
    wall.forward(620)
    wall.right(90)

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score
score = 0
scoreGui = turtle.Turtle()
scoreGui.speed(0)
scoreGui.color("white")
scoreGui.penup()
scoreGui.hideturtle()
scoreGui.goto(0, 260)
scoreGui.write("Score: {}".format(score), align="center",
               font=("Courier", 24, "normal"))

# Start Button
start = turtle.Turtle()
start.speed(0)
start.shape("square")
start.color("blue")
start.penup()
start.goto(0, -260)
start.write("Click On the Screen to Start",
            align="center", font=("Courier", 24, "normal"))

# Functions


def startGame(x, y):
    start.hideturtle()
    start.clear()
    moveSnake()


def goRight():
    if snake.direction != "left":
        snake.direction = "right"


def goLeft():
    if snake.direction != "right":
        snake.direction = "left"


def goUp():
    if snake.direction != "down":
        snake.direction = "up"


def goDown():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


currentDelay = 100


def moveSnake():
    global score, currentDelay
    wn.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"

        for seg in segments:
            seg.goto(1000, 1000)

        segments.clear()

        food.goto(0, 100)

        currentDelay = 100

        score = 0
        scoreGui.clear()
        scoreGui.write("Score: {}".format(score), align="center",
                       font=("Courier", 24, "normal"))

        start.showturtle()
        start.write("Click On the Screen to Start", align="center",
                    font=("Courier", 24, "normal"))
    else:
        if snake.distance(food) < 20:
            # Teleport food to a new location
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)

            while any(seg.distance(x, y) < 20 for seg in segments):
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)

            food.goto(x, y)

            # Speed by score
            if score % 50 == 0 and score > 0 and currentDelay >= 70:
                currentDelay -= 1

            # Create a new segment
            newSegment = turtle.Turtle()
            newSegment.speed(0)
            newSegment.shape("square")
            newSegment.color("black")  # Kenar rengi olarak siyah
            newSegment.fillcolor("grey")
            newSegment.penup()
            segments.append(newSegment)

            # Adding score
            score += 10
            scoreGui.clear()
            scoreGui.write("Score: {}".format(score), align="center",
                           font=("Courier", 24, "normal"))

        for i in range(len(segments)-1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y)

        move()

        for segment in segments:
            if segment.distance(snake) < 20:
                time.sleep(1)
                snake.goto(0, 0)
                snake.direction = "Stop"

                for seg in segments:
                    seg.goto(1000, 1000)

                segments.clear()

                food.goto(0, 100)

                currentDelay = 100

                score = 0
                scoreGui.clear()
                scoreGui.write("Score: {}".format(score), align="center",
                               font=("Courier", 24, "normal"))

                start.showturtle()
                start.write("Click On the Screen to Start", align="center",
                            font=("Courier", 24, "normal"))
                return

        wn.ontimer(moveSnake, currentDelay)


wn.onscreenclick(startGame)

# Keys
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goLeft, "a")
wn.onkeypress(goRight, "d")

wn.mainloop()
