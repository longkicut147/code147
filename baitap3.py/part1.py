#1.1
computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
print(computer)

#1.2
print("So luong macbook co trong kho la: ", computer["MACBOOK"])

#1.3
a = input("nhap hang may tinh: ")
userInput = a.upper()
if userInput in computer:
    print("So luong may trong kho la: ", computer[userInput])
else: 
    print("deo co")

