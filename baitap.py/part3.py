#3.1
number = [1, 5, 6, 9, 12]
userinput = int(input("Enter a number: "))
if userinput in number:
    print("found")
else:
    print("not found")

#3.2
print(sum(number))

total = 0
for item in number:
    total += item
print(total)

#3.3
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
d = int(input("Enter your number: "))
e = int(input("Enter your number: "))
listNumber = [a, b, c, d, e]
print(sum(listNumber))
