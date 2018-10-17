from turtle import *

def star(n):
    for i in range(n):
        forward(100)
        right(180-(360/(2*n)))

def spiral_star():     
    for i in range(50):
        forward(5*i)
        left(180-36)

def flower(n):
    for j in range(n-1):
        for i in range(n):
            forward(50)
            left(360/n)
        forward(50)
        right(360/(n-1))

def spirala(n,k):
    forward(n)
    left(90)
    for i in range(k):
        for j in range(2):
            forward(n-i*10)
            left(90)

def diamant():
    for i in range(10):
        forward(100)
        left(36)
    for i in range(10):
        left(36)
        forward(100)
        left(72)
        forward(100)   
        left(108)
        forward(100)
        left(72)
        forward(100)
        left(72)
        forward(100)
        left(36)

        
def spiral6():     
    j = 0
    for i in range(80):
        forward(10 + j)
        right(62)
        j = j + 2
        
def spiral8():
    j = 10
    for i in range(40):
        forward(j)
        left(360/8)
        j *= 1.1
        

def diamant12():
    for i in range(12):
        for i in range(12):
            forward(40)
            left(360/12)
        left(360/12)

def polypolygon(inner_n,outer_n):
    for i in range(inner_n):
        forward(50)
        left(360/inner_n)
    for i in range(inner_n):
        for j in range(outer_n):
            forward(50)
            right(360/outer_n)
        forward(50)
        left(360/inner_n)

 

   



