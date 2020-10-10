from turtle import *

# userinput = int(input("Nhap so vong tron: "))
# speed(-1)

# def drawTimesCircle(times):
#     for i in range(times):
#         circle(100)
#         left(i*13)

# drawTimesCircle(userinput)

#ve hinh va so luong hinh nguoi dung muon:
userinput = input("Vẽ hình: ")
userinput2 = int(input("Số lượng hình: "))

speed(-1)

if userinput == "tron":
    userinput3 = int(input("Bán kính: "))
    for i in range(userinput2):
        circle(userinput3)
        left(27)
elif userinput == "vuong":
    for i in range(userinput2):
        for x in range(4):
            forward(100)
            left(90)
        left(35)

mainloop()




