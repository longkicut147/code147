a = 20
b = int(input("nhap 1 so bat ki: "))
if b > a:
    print("b lon hon a")
else:
    print("b be hon a")


tuoi = int(input("nhap so tuoi: "))
if tuoi <= 6:
    print("baby")
elif 7 <= tuoi <= 12:
    print("kids")
elif 13 <= tuoi <= 17:
    print("teen")
elif tuoi >= 100:
    print("died")
else:
    print("adult")


#day la 1 doan code nhan biet loai tam giac va tinh dien tich theo 3 canh
a = int(input("canh ben thu nhat: "))
b = int(input("canh ben thu hai: "))
c = int(input("canh day: "))
p = (a + b + c) / 2

if a == b and a == c:
    print("tam giac deu")
    S1 = (p * (p-a) * (p-b) * (p-c)) **1/2
    print(S1)

elif a == b or a == c or b == c:
    print("tam giac can")
    S2 = (p * (p-a) * (p-b) * (p-c)) **1/2
    print(S2)

elif a**2 + b**2 == c**2:
    print("tam giac vuong")
    S3 = (p * (p-a) * (p-b) * (p-c)) **1/2
    print(S3)

else:
    print("tam giac binh thuong")
    S4 = (p * (p-a) * (p-b) * (p-c)) **1/2
    print(S4)


books = ["Harry Potter", "su tich cay khe", "Thach Sanh"] 
while True:
    userinput = input("enter here: ")
    if userinput in books:
        index = books.index(userinput)
        print(books[index])
        break   

# for i in [1, 0]:
#     print(i + 1)