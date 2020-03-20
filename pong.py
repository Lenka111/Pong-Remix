# Elena Voinu
import turtle
import time

start_time = time.time()



turtle.register_shape("pong.gif")

wn = turtle.Screen()
wn.title("Pong Game by Elena Voinu")
# Changed the background color Elena Voinu
wn.bgcolor("dark green")
# Changed the screen size to accommodate the border drawing Elena Voinu
wn.setup(width=800, height=700)
wn.tracer(0)

# set up the border 
# added the lines 17 through 26, they weren't here initially
border = turtle.Turtle(visible=False)
border.color('white')
border.pensize(3)
border.penup()
border.setposition(-300, -300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.left(90)


# Score
score_a = 0
score_b = 0

''' Added a timer to the game that counts the seconds passed while the game is ruinning: lines 40 - 46
    Elena Voinu
'''
seconds = 0
# Draw timer
time_pen = turtle.Turtle(visible=False)
time_pen.color("white")
time_pen.penup()
time_pen.setposition(-55, -340)
time_pen.write("Time  {} ".format(time.time()), False, align="center", font=("Courier", 24, "normal"))


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# added gif instead of shape for the paddle 
paddle_a.shape("pong.gif")
#paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(0.5, 3)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.showturtle()
paddleaspeed = 10

# Paddle B computer player
paddle_b = turtle.Turtle()
paddle_b.speed(0)
# added gif instead of shape for the paddle
paddle_b.shape("pong.gif")
#paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(0.5, 3)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.showturtle()

# Added the speed of the computer paddle 
paddlebspeed = 15

# Ball
ball = turtle.Turtle()
ball.speed(0)
# Changed the shape of the ball
ball.shape("circle")
# Added the size of the ball
ball.shapesize(1, 1)
ball.color("white")
ball.penup()
ball.showturtle()
ball.goto(0, 0)
# added the speed of the ball 
ballspeed = 15
ball.dx = 5
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

'''Changed the position of the player A and B score, because the border 
   is now visible and the text looks better when it's above it
'''
pen.goto(-20, 310)
#pen.goto(0, 260) original position
# Rearranged how the scores are displayed on the screen 
pen.write("PlayerA: 0 \t\t Sharapova: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    wn.update()


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    wn.update()


'''Commented out the up and down movement for paddle b
   since it's the computer playing now
'''
#def paddle_b_up():
   # y = paddle_b.ycor()
   # y += 20
   # paddle_b.sety(y)
 #   wn.update()


#def paddle_b_down():
   # y = paddle_b.ycor()
   # y -= 20
   # paddle_b.sety(y)


# Keyboard bindings
wn.listen()
# Changed the keys to move up and down for paddle A Elena Voinu
# If run from Mac's terminal use onkey(), if run from windows change to
#on keypress() for a smooth up and down movement
wn.onkey(paddle_a_up, "Up")
wn.onkey(paddle_a_down, "Down")


# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom

    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1

    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        # rearranged how the scores are displayed on the screen
        pen.write("PlayerA: {} \t\t Sharapova: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        # rearranged how the scores are displayed on the screen Elena Voinu
        pen.write("PlayerA: {} \t\t Sharapova: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # move the computer player(paddle_b) 
    y = paddle_b.ycor()
    y += paddlebspeed
    paddle_b.sety(y)
    if paddle_b.ycor() > 250:
        paddlebspeed *= -1
    if paddle_b.ycor() < -250:
        paddlebspeed *= -1

    # Paddle and ball collisions

    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    # Ball and player collision
    # Simplified the comparison
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    # display timer
    time_pen.undo()
    time_pen.write("Time: {}".format(round(time.time()- start_time)), False, align="Left", font=("Courier", 24, "normal"))


    wn.update()

