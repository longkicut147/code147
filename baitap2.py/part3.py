#3.1
number = [1, 5, 6, 9, 12]
userinput = int(input("Enter a number: "))
if userinput in number:
    print("found")
else:
    print("not found")

#3.2
print(sum(number))

#3.3
number = input("Enter numbers separate by ,: ")
listnumber = number.split(',')
print(sum(listnumber))
