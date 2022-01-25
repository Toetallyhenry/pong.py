#created using a tutorial
#original code by @TokyoEdTech
#simple pong game written by Henry using a tutorial

import turtle
    
window = turtle.Screen()
window.title("pong by Henry")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# score
score_A = 0
score_B = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball_a = turtle.Turtle()
ball_a.speed(0)
ball_a.shape("square")
ball_a.color("white")
ball_a.penup()
ball_a.goto(0, 0)
ball_a.dx = 1
ball_a.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
#keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    window.update()
    
    #move the ball
    ball_a.setx(ball_a.xcor() + ball_a.dx)
    ball_a.sety(ball_a.ycor() + ball_a.dy)
    
    #border checking
    if ball_a.ycor() > 290:
        ball_a.sety(290)
        ball_a.dy *= -1
     
    if ball_a.ycor() < -290:
        ball_a.sety(-290)
        ball_a.dy *= -1
     
    if ball_a.xcor() > 390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))
    
    if ball_a.xcor() < -390:
        ball_a.goto(0, 0)
        ball_a.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))
    # paddle ball collision
    
    if ball_a.xcor() > 340 and ball_a.xcor() < 350 and (ball_a.ycor() < paddle_b.ycor() + 50 and ball_a.ycor() > paddle_b.ycor() -50):
        ball_a.setx(340)
        ball_a.dx *= -1
    
    if ball_a.xcor() < -340 and ball_a.xcor() > -350 and (ball_a.ycor() < paddle_a.ycor() + 50 and ball_a.ycor() > paddle_a.ycor() -50):
        ball_a.setx(-340)
        ball_a.dx *= -1  