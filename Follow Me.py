"""
We've initialized a blue ball for you, and started you off with the mouse tracking code from 
lecture. Make the blue ball follow the mouse position so that the mouse is at the center of 
the blue ball as it moves!
Click the image to make it pause!
Recall that the graphics library has a moveto function
canvas.moveto(object, new_x, new_y)
"""

from graphics import Canvas
import time

CANVAS_SIZE = 400
BALL_DIAMETER = 50
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    ball = canvas.create_oval(
        0, 0,
        BALL_DIAMETER, 
        BALL_DIAMETER,
        'blue'
    )

    # Wait until mouse is on the canvas
    while canvas.get_mouse_x() is None or canvas.get_mouse_y() is None :
        canvas.update()
        time.sleep(0.01)
    
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # Instructs the ball to follow the position of the user's mouse
        if mouse_x is not None and mouse_y is not None :
            canvas.moveto(ball, mouse_x, mouse_y)
        
        canvas.update()
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

        # Keep the window open to see the output
        
        


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()