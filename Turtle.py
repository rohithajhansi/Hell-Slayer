import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 500)

# Create the turtle to draw the path
path_drawer = turtle.Turtle()
path_drawer.hideturtle()
path_drawer.pencolor("green")
path_drawer.pensize(3)

# Draw the green path
path_drawer.penup()
path_drawer.goto(-200, -50)  # Starting point
path_drawer.pendown()
path_drawer.goto(200, -50)  # Ending point

# Create the turtle (representing a stick figure)
human_drawer = turtle.Turtle()
human_drawer.speed(3)
human_drawer.hideturtle()

# Function to draw a stick figure at a given position
def draw_human(x, y):
    human_drawer.penup()
    human_drawer.pensize(5)
    human_drawer.goto(x, y + 50)  # Draw the head
    human_drawer.pendown()
    human_drawer.circle(10)  # Radius of the head

    human_drawer.penup()
    human_drawer.pensize(5)
    human_drawer.goto(x, y + 20)  # Draw the body
    human_drawer.pendown()
    human_drawer.goto(x, y + 50)

    human_drawer.penup()
    human_drawer.goto(x, y + 35)  # Draw the left arm
    human_drawer.pendown()
    human_drawer.goto(x - 15, y + 45)

    human_drawer.penup()
    human_drawer.pensize(5)
    human_drawer.goto(x, y +35)  # Draw the right arm
    human_drawer.pendown()
    human_drawer.goto(x + 15, y + 45)

    human_drawer.penup()
    human_drawer.pensize(5)
    human_drawer.goto(x, y +20)  # Draw the left leg
    human_drawer.pendown()
    human_drawer.goto(x - 15, y +0)

    human_drawer.penup()
    human_drawer.pensize(5)
    human_drawer.goto(x, y +20)  # Draw the right leg
    human_drawer.pendown()
    human_drawer.goto(x + 15, y + 0)
    human_drawer.write("Walking here!", align="center", font=("Arial", 12, "normal"))


# Animate the human moving along the path
for position in range(-200, 200, 50):  # Move from left to right
    human_drawer.clear()  # Clear the previous figure
    draw_human(position, -50)  # Stick figure moves along the green path
    time.sleep(0.2)  # Pause to create the animation effect

# Finish
screen.mainloop()
