import turtle

t = turtle.Turtle()

def close_on_esc():
    """
        close when esc key is pressed
    """
    turtle.bye()

t.color("blue")
t.begin_fill()

for _ in range(4):
    t.fillcolor("#35b96a")
    t.forward(100)
    t.right(90)

t.end_fill()
    
turtle.listen()
turtle.onkeypress(close_on_esc,"Escape")
turtle.mainloop()

    
