from turtle import *

#2.1
color = ["blue", "red", "green"]
# userinput = int(input("Enter position: "))
# position = color[userinput]
# print(position)

#2.2
# userinput = int(input("delete: "))
# color.pop(userinput)
# userinput = input("delete: ")
# color.remove(userinput)
# print(color)

#2.3
for i in range(color):
    pencolor(i)
    forward(100)