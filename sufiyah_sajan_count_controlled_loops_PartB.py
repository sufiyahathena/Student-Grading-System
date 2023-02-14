#sufiyah sajan
#count controlled loops
#part B

import random
import math

no_throws = int(input("Number of throws: "))
while float(no_throws) < 0:
    no_throws = input("Please enter a positive number of throws: ")

red_square = 0
blue_rect = 0
orange_circle = 0
grey_circle = 0
yellow_circle = 0
black_overlap = 0

def distance(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2) + ((y1-y2)**2))


def darts(x,y):
    global red_square
    global blue_rect
    global orange_circle
    global grey_circle
    global yellow_circle
    global black_overlap
    #reddist = distance(x,y,125,125)
    #bluedist = distance(x,y,350,250)
    orangedist = distance(x,y,650,150)
    greydist = distance(x,y,650,350)
    yellowdist = distance(x,y,650,350)
    bcirc1dist = distance(x,y,350,150)
    bcirc2dist = distance(x,y,350,250)
    bcirc3dist = distance(x,y,350,350)
    #blackdist = distance(x,y, 650, 225)

    if (orangedist <= 100):
        if ((x >= 575 and x<= 725) and (y >= 200 and y <= 250)):
            black_overlap = black_overlap + 1
            return
        orange_circle = orange_circle + 1
        return
    if ((x >= 50 and x<= 200) and (y >= 50 and y <= 200)):
        red_square = red_square + 1
        return
    if ((x >= 250 and x <= 450) and (y >= 50 and y<= 750)):
        if (bcirc1dist <= 50):
            return
        if (bcirc2dist <= 50):
            return
        if (bcirc3dist <= 50):
            return
        blue_rect = blue_rect + 1
    if (greydist <= 150):
        if (yellowdist <= 50):
            yellow_circle = yellow_circle + 1
            return
        if ((x >= 575 and x<= 725) and (y >= 200 and y <= 250)):
            black_overlap = black_overlap + 1
            return
        grey_circle = grey_circle + 1
        return

for i in range(int(no_throws)):
    x_cord = random.randint(0,800)
    y_cord = random.randint(0,800)
    darts(x_cord, y_cord)

hit = (red_square + blue_rect + orange_circle + yellow_circle + grey_circle + black_overlap)
misses = int(no_throws) - hit

redperc = format((red_square*100/no_throws), '.2f')
blueperc = format((blue_rect*100/no_throws), '.2f')
orangeperc = format((orange_circle*100/no_throws), '.2f')
yellowperc = format((yellow_circle*100/no_throws), '.2f')
greyperc = format((grey_circle*100/no_throws), '.2f')
blackperc = format((black_overlap*100/no_throws), '.2f')
missesperc = format((misses*100/no_throws), '.2f')

print("Red:             ", red_square, " (", redperc, "%)")
print("Blue:            ", blue_rect, " (", blueperc, "%)")
print("Orange:          ", orange_circle, " (", orangeperc, "%)")
print("Yellow:          ", yellow_circle, " (", yellowperc, "%)")
print("Grey:            ", grey_circle, " (", greyperc, "%)")
print("Black:           ", black_overlap, " (", blackperc, "%)")
print("Misses:          ", misses, " (", missesperc, "%)")


# Extra Credit

import turtle
print()
draw = input("Would you like to visualize the results? (yes/no): ")
while draw != 'yes':
    draw = input("Would you like to visualize the results? (yes/no): ")
turtle.tracer(0)
while draw == 'yes':
    turtle.reset()
    turtle.setworldcoordinates(0, 500, 800, 0)
    turtle.screensize(800,500)
    turtle.setup(800, 500)
    turtle.pensize(1)
    turtle.pencolor('red')
    turtle.fillcolor('red')
    turtle.penup()
    turtle.setposition(50,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(200,50)
    turtle.goto(200, 200)
    turtle.goto(50, 200)
    turtle.goto(50, 50)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('blue')
    turtle.fillcolor('blue')
    turtle.setposition(250,50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(450,50)
    turtle.goto(450, 450)
    turtle.goto(250, 450)
    turtle.goto(250, 50)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.setposition(350,150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(350,250)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(350,350)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('orange')
    turtle.fillcolor('orange')
    turtle.penup()
    turtle.setposition(650,150)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('grey')
    turtle.fillcolor('grey')
    turtle.penup()
    turtle.setposition(650,350)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.penup()
    turtle.setposition(650,350)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.pencolor('yellow')
    turtle.fillcolor('yellow')
    turtle.penup()
    turtle.setposition(650,350)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    break
turtle.update()
    
