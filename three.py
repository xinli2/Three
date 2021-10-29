###
### Author: Xin Li
### Description:  In this programming assignment,
### you should create a program that behaves
### similarly to the gif shown in this spec.
### Name of this program is: three.py
### The frame rate should be no less than 30 and
### no more than 100.
### The canvas should draw a rectangle, circle,
### and triangle. Requirements for the shapes
### include:
### Each of these shapes should be a different color.
### They should move across the screen at about the
### same rate as the example shows.
### They should be aligned in a column.
### They should wrap around the screen. They should
### begin off-canvas to the left, and go off-canvas
### to the right, and then wrap around.
### The y position should be set randomly for each
### shape each time the shapes wrap. The random
### position should not cause the shape to go
### off-canvas on the top or bottom.
###
from graphics import graphics
import random
def main():
    gui = graphics(500, 500, 'Graphics')
    x_coord = 0
    y_rectangle_coord = random.randint(50, 450)
    y_ellipse_coord = random.randint(50, 450)
    y_triangle_coord = random.randint(0, 450)
    while True:
        gui.clear()
        gui.rectangle(x_coord-25, y_rectangle_coord, 50, 50, 'green')
        gui.ellipse(x_coord, y_ellipse_coord, 50, 50, 'orange')
        gui.triangle(x_coord, y_triangle_coord, x_coord-25, y_triangle_coord+50, x_coord+25, y_triangle_coord+50,'blue')
        gui.update_frame(30)
        x_coord += 10
        if x_coord > 550:
            x_coord = 0
            y_rectangle_coord = random.randint(50, 450)
            y_ellipse_coord = random.randint(50, 450)
            y_triangle_coord = random.randint(0, 450)

main()
