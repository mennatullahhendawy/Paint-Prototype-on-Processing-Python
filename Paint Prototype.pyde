def setup():
    size(400,400) #width, #height
    background(255,0,0) # r, g, b
    noStroke() #no stroke on the background
   

def draw(): #function to draw
    fill(255,255,255) #colorfill for quad to be drawn below
    stroke(0,255,0) #stroke the quad with a specefic color (G)
    quad(38, 31, 86, 20, 69, 63, 30, 76) #shape as a quad in this position
  
    fill(0, 0, 255) #colorfill the triangle to be drawn below
    stroke(200,150,20) #stroke triangle with this color
    triangle(130, 175, 158, 120, 186, 175) #draw triangle
 
    
    stroke(200,150,20) #stroke rectangle
    fill(0, 0, 0) #colorfill the triangle to be drawn below
    rect(0, 40, 30, 20) #draw rectangle

    
