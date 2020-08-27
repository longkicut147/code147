#day la 1 game giai toan chon dung sai

from random import randrange, choice
while True:
    a = randrange(10)
    b = randrange(10)
    
    correct = a + b
    wrongnumber = choice([0,-3, 0, -2, 3, 1, 2, -1, 0])
    incorrect = correct + wrongnumber
    print(a, "+", b, "=", incorrect)

    userInput = input("T or F: ")

    if incorrect != correct:
        if userInput.lower() == "t":
            print("lose")
            break
        elif userInput.lower() == "f":
            print(" ")
    else:
        if userInput.lower() == "t":
            print(" ")
        elif userInput.lower() == "f":
            print("lose")
            break


    

    


