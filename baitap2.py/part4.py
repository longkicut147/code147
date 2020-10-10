#4.1
number = [1, 5, 6, 12, 27, 56]
for item in number:
    if item %2 == 0:
        print(item)

#4.2
usernumber = input("Enter list number separate by ,: ")
listnumber = usernumber.split(',')
for item in listnumber:
    if item %2 == 0:
        print(item)
