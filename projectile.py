# Barret Fisher
# CS115 Section 5
# 10-3-12
# Program 2 with design
# Purpose: To output range, maximum height of projectile on three different
#       planets and plot parabola curve of each
# Input: User inputs velocity, angle of projectile
# Preconditions: None
# Postconditions: Range, max height on three planets and graph


# import turtle, math libraries
from math import *
from turtle import *


###########################
# Function name: total_distance
# Purpose: To determine distance traveled by projectile on one planet
# Preconditions: Velocity (initial velocity of projectile), angle
#       (initial angle of projectile), gravity (force felt on planet)
# Postconditions: Total distance traveled by projectile
# 1. Define range function with parameters velocity, angle, gravity
# 2. First part is distance traveled equals velocity squared times
#       sine of two times the angle
# 3. Second part is first part divided by gravity
###########################
def total_distance(v,a,g): #(velocity, angle, gravity)
    length = (v**2) * sin(2*a)
    length = length / g
    return(length)


###########################
# Function name: maxHeight
# Purpose: To determine the maximum height of projectile on one planet
# Preconditions: Velocity (initial velocity of projectile), angle
#       (initial angle of projectile), gravity (force felt on planet)
# Postconditions: Maximum height of projectile
# 1. Define maxHeight function with parameters velocity, angle, gravity
# 2. First part is velocity squared times sine of angle squared
# 3. Second part is first part divided by two times gravity
###########################
def maxHeight(v,a,g): #(velocity, angle, gravity)
    highest = (v**2) * sin(a)**2
    highest = highest / (2*g)
    return(highest)


###########################
# Function name: height
# Purpose: To determine the height of projectile after it's traveled
#       a certain distance
# Preconditions: Velocity (initial velocity of projectile), angle (initial
#       angle of projectile), gravity (force felt on planet), distance
#       (x-value of turtle in graph)
# Postconditions: Height of projectile after a certain distance (y-value)
# 1. Define height function with parameters velocity, angle, gravity, distance
# 2. First part is distance times tangent of angle
# 3. Second part is gravity times distance squared
# 4. Third part is two times velocity squared times cosine of angle squared
# 5. Fourth part is second part divided by third part
# 6. Fifth part is first part minus fourth part
###########################
def height(v,a,g,x): #(velocity, angle, gravity, distance)
    y_one = x * tan(a)
    y_two = g * (x**2)
    y_three = 2 * (v**2) * (cos(a))**2
    y_four = y_two / y_three
    y = y_one - y_four
    return(y)


###########################
# Function name: graph
# Purpose: To plot projectile on a planet as parabola curve
# Preconditions:  Velocity (initial velocity of projectile), angle (initial
#       angle of projectile), gravity (force felt on planet), length (distance
#       traveled by projectile), turtle (name of turtle drawing)
# Postconditions: 
# 1. Define graph function with parameters velocity, angle, gravity, length,
#       turtle
# 2. Increment equals range divided by fifteen
# 3. x is 0, y is 0
# 4. Use for loop to plot 15 points on graph connected by line
#       4a. Plot x,y with turtle (in loop)
#       4b. x is x plus increment (in loop)
#       4c. Call height function for y using velocity, angle, gravity, x
#           (in loop)
###########################
def graph(v,a,g,le,t): #(velocity, angle, gravity, length, turtle)
    increment = le/14
    x = 0
    y = 0
    t.ht()
    t.speed(0)
    t.pd()
    for i in range(15):
        t.goto(x,y)
        t.dot(1)
        x = x + increment
        y = height(v,a,g,x)



# Define main function
def main():

    # Greet the user with title of program
    print()
    print("Trajectories on Planets")

    # Get angle of launch in degrees and initial velocity from user
    angle = eval(input("Enter the angle of launch (degrees): "))
    velocity = eval(input("Enter the initial velocity (meters per second): "))
    print()

    # graph window (added after design)
    wn = Screen()
    wn.setup(800,600)
    wn.setworldcoordinates(-10,-20,790,580)
    wn.bgcolor("White")
    wn.title("Motion of Projectile")

    # graph axes, labels (added after design)
    line = Turtle()
    line.ht()
    line.color("black")
    line.width(2)
    line.speed(0)
    line.up()
    line.goto(0,580)
    line.pd()
    line.goto(0,0)
    line.goto(790,0)
    line.up()
    line.goto(0,-20)
    line.color("blue")
    line.write("Earth = blue,", True, align="left", font=("Arial",8,"normal"))
    line.fd(8)
    line.color("red")
    line.write("Mars = red,", True, align="left", font=("Arial",8,"normal"))
    line.fd(8)
    line.color("black")
    line.write("Mercury = black", True, align="left", font=("Arial",8,"normal"))
    line.goto(10,565)
    line.write("Height (m)", True, align="left", font=("Arial",8,"normal"))
    line.goto(720,-20)
    line.write("Distance (m)", True, align="left", font=("Arial",8,"normal"))

    # Convert degrees to radians
    angle = angle * (pi/180)
    
    # Earth calculation/output using functions
    gravity = 9.81
    length = total_distance(velocity,angle,gravity)
    highest = maxHeight(velocity,angle,gravity)
    length = round(length,2)
    highest = round(highest,2)
    print("Distance traveled on Earth =",length,"m, max height =",highest,"m")
    earth = Turtle()
    earth.color("blue")
    graph(velocity,angle,gravity,length,earth)

    # Mars calculation/output using functions
    gravity = 3.77
    length = total_distance(velocity,angle,gravity)
    highest = maxHeight(velocity,angle,gravity)
    length = round(length,2)
    highest = round(highest,2)
    print("Distance traveled on Mars =",length,"m, max height =",highest,"m")
    mars = Turtle()
    mars.color("red")
    graph(velocity,angle,gravity,length,mars)

    # Mercury calculation/output using functions
    gravity = 3.59
    length = total_distance(velocity,angle,gravity)
    highest = maxHeight(velocity,angle,gravity)
    length = round(length,2)
    highest = round(highest,2)
    print("Distance traveled on Mercury =",length,"m, max height =",highest,"m")
    mercury = Turtle()
    mercury.color("black")
    graph(velocity,angle,gravity,length,mercury)

    # allows program to end w/o crashing...
    wn.exitonclick()
main()
