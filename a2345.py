# importing  hte libray 
import turtle

# cretaing canvas 
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(800,600)

# turtle object creation  
board = turtle.Turtle()
board.speed("slowest")


for i in range(4):
    board.forward(100)
    board.left(90)


turtle.done()
