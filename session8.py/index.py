
# mylist = ["mom", "me", "dad"]

# def reverselist():
#     print("Hello")
#     print("My family", mylist)


# def checkAge(age):
#     if (0 < age <= 6):
#         return("baby")
#     elif (7 <= age <= 12):
#         return("Child")
#     elif(13 <= age <= 16 ):
#         return("Teenager")
#     else:
#         return("adult")

# yourAge = int(input("Your age: "))
# result = checkAge(yourAge)
# print(result)


#1
# x = int(input("Số thứ nhất: "))
# y = int(input("Số thứ hai: "))

# def sosanh():
#     if x > y:
#         print("Số thứ nhất lớn hơn số thứ hai")
#     elif x < y:
#         print("Số thứ nhất bé hơn số thứ hai")
#     else:
#         print("Bằng nhau")

# sosanh()


#2
# a = int(input("Viết 1 số: "))

# def chanHayle():
#     if a %2 == 0:
#         print("Đây là số chẵn")
#     else:
#         print("Đây là số lẻ")

# chanHayle()


#3
# b = int(input("Năm: "))

# def kiemtraNamnhuan():
#     if b %4 == 0:
#         print("Đây là năm nhuận")

# kiemtraNamnhuan()


#4
# def Tongdayso():
#     day = [1, 2, 3, 4, 5, "ngu", True]
#     tong = 0
#     for item in day:
#         if type(item) is int:
#             tong = tong + item
#     print(tong)

# Tongdayso()


#5
def convertStringToList(text):
    result = text.split(", ")
    result.sort()
    return result

userinput = input("Enter: ")

lastResult = convertStringToList(userinput)
print(lastResult)
