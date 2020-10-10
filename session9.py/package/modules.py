# 1
# x = int(input("Số thứ nhất: "))
# y = int(input("Số thứ hai: "))

def sosanh(number1, number2):
    if number1 > number2:
        print("Số thứ nhất lớn hơn số thứ hai")
    elif number1 < number2:
        print("Số thứ nhất bé hơn số thứ hai")
    else:
        print("Bằng nhau")



#2
# a = int(input("Viết 1 số: "))

def chanHayle(number):
    if number %2 == 0:
        print("Đây là số chẵn")
    else:
        print("Đây là số lẻ")

#3
# b = int(input("Năm: "))

def kiemtraNamnhuan(nam):
    if nam %4 == 0:
        print("Đây là năm nhuận")

#4
def Tongdayso():
    day = [1, 2, 3, 4, 5, "ngu", True]
    tong = 0
    for item in day:
        if type(item) is int:
            tong = tong + item
    print(tong)

#5
def convertStringToList(text):
    result = text.split(", ")
    result.sort()
    return result

    userinput = input("Enter: ")

    lastResult = convertStringToList(userinput)
    print(lastResult)

if __name__ == "__main__":
    sosanh()
    convertStringToList()
    chanHayle()
    Tongdayso()