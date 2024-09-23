# Paint Prototype on Processing Python
 
Paint Prototype

Acknowledgments
Acknowledgments: This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy and Mohamed-Ali-77. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Project overview
This repository contains a simple Paint Program created as part of the Game Development 1 for Beginners course using Processing Python mode.

Installation
1.	Download and install Processing.
2.	Make sure to enable Python Mode in Processing:
o	Open Processing.
o	Go to the "Mode" drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the paint_prototype.pde file in Processing.

Usage
1.	Launch Processing.
2.	Open the paint_prototype.pde file from this repository.
3.	Click the "Run" button in Processing to start the paint program.
4.	You can now draw on the canvas using multiple shapes (quad, triangle, and rectangle) with different colors.

Code Functionality
The paint program fulfills the following grading rubric:
•	Brush Shape: Different shapes like quads, triangles, and rectangles are used as brushes.
•	More than Two Colors: The program includes more than two colors for the shapes.

Example Code Snippet
def setup():
    size(400, 400)  # Set the canvas size
    background(255, 0, 0)  # Set the background color to red
    noStroke()  # No stroke for the background

def draw():
    fill(255, 255, 255)  # White fill for the quad
    stroke(0, 255, 0)  # Green stroke for the quad
    quad(38, 31, 86, 20, 69, 63, 30, 76)  # Draw a quad

    fill(0, 0, 255)  # Blue fill for the triangle
    stroke(200, 150, 20)  # Custom stroke for the triangle
    triangle(130, 175, 158, 120, 186, 175)  # Draw a triangle

    fill(0, 0, 0)  # Black fill for the rectangle
    stroke(200, 150, 20)  # Custom stroke for the rectangle
    rect(0, 40, 30, 20)  # Draw a rectangle

