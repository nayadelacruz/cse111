# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_starts(canvas, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_trees(canvas, scene_width, scene_height)
    

    #call stars


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height, scene_width, 200, width=0, fill="black")
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0,0,scene_width,200, width=0, fill="tan1")
def draw_clouds(canvas, scene_width, scene_height):
    draw_oval(canvas, 50, 450, 250, 350, width=0,fill="gray")
    draw_oval(canvas, 150, 420, 350, 300, width=0,fill="gray")
    draw_oval(canvas, 400, 475, 700, 300, width=0,fill="gray")
    draw_oval(canvas, 600, 400, 700, 300, width=0,fill="gray")  


#draw stars that creates many starts with just one function, 
def draw_starts(canvas, scene_height):
    #necesito una variable que me guarde el estado de la posicion horizontal
    #necesito una variable que guarde el estado de la posicion vertical
    for row in range(1, 6):
        for col in range(1, 16):
            x1 = col * 50
            y1 = scene_height - (row * 50)
            x2 = x1 + 1
            y2 = y1 + 1
            draw_oval(canvas, x1, y1, x2, y2, width=0, fill="yellow")

       #quiero un loop que avance 50px en cada iteration, y quiero que corra 15 veces
       #necesito un loop que actualize la posicion vertical 
       # necesito un loop que cree las rows tres veces  
       # para tener los 4 valores que necesito para el ovalo necesito para el ovalo el primero lo quiero en la coordenada 50, 470 y la siguiente coordenada 52, 472 
       #necesito que el primer row inicie 
def draw_trees(canvas, scene_width, scene_height):           
    #I want to draw 3 trees and for drawing one circle  and one vertical rectangle 
    # I need a loop that goes 3 times
    
    for tree in range (0,7):
        x1tree = (tree * 100) + 50
        x2tree = x1tree + 50
        x1oval = tree * 100
        x2oval = x1oval + 150
        draw_rectangle(canvas, x1tree, 0, x2tree, 150, width=0, fill="tan4")
        draw_oval(canvas, x1oval, 140, x2oval, 290, width=0, fill="green")
          
       
        
        




# Call the main function so that
# this program will start executing.
main()