"""
Students in Code in Place are from 150 different countries! Wow. Let's celebrate our 
international class by drawing flags. To start out, one of the most straightforward flags 
to draw using Python graphics is the flag of Indonesia:

The dimensions of your flag should be based off the provided constants:

# The width of the canvas
CANVAS_WIDTH = 450
# The height of the canvas
CANVAS_HEIGHT = 300

To draw the Indonesian flag all you need to do is to draw a single red rectangle which covers 
the top half of the graphics canvas. You don't need to draw the white stripe, the canvas is 
white by default.

Recall the graphics method for drawing a colored rectangle:

# Draws a rectangle with specified color
rect = canvas.create_rectangle(
    left_x, 
    top_y, 
    right_x, 
    bottom_y,
    color
)

Once you have drawn the Indonesian flag, push the "check correct" button underneath the canvas 
to get it graded.

After that, feel free to get creative. Consider making up your own flag! Can you think of a 
design that would represent your friends, family, or a group that doesn't have a flag?
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    # This function creates a flag, in this case, Indonesia's.
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0,0, CANVAS_WIDTH, CANVAS_HEIGHT/2, "red")
    
    # Keep the window open to see the output
    canvas.mainloop()
    

if __name__ == '__main__':
    main()