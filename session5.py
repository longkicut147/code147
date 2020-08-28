
# UserInput = input("write something: ")
# print(UserInput.upper())


# ho = input("Họ_Của_Bạn: ")
# ten = input("Tên_Của_Bạn: ")
# print("Hi", a, b)


# a = int(input("Viết một số bất kì: "))
# b = a**2
# print("Bình phương của", a, "là", b)

# for i in range(3, 13):
#     print(i)

# n = int(input("Viết 1 số bất kì: "))
# if n > 0:
#     for i in range(0, n+1):
#         print(i)
# else:
#     print("số lớn hơn 0 pls")

# n = int(input("Viết 1 số bất kì: "))
# a = n %2==0
# if a == 0:
#     for i in range(n, 0, -2):
#         print(i)
# elif a == 1:
#     for i in range(n-1, 0, -2):
#         print(i)


# a = int(input("Viết 1 số bất kì: "))
# if a > 13:
#     print(a, "lớn hơn 13")
# elif a < 13:
#     print(a, "bé hơn 13")
# else:
#     print(a, "là 13 :D")


# n = int(input("Viết 1 số bất kì: "))
# a = n %2==0
# if a == 1:
#     print(n, "là số chẵn")
# elif a == 0:
#     print(n, "không phải số chẵn")


# a = [1, 3, 5, 7, 8 ,10, 12]
# b = [4, 6, 9, 11]
# UserInput = int(input("Tháng: "))
# if UserInput in a:
#     print("Tháng", UserInput, "có 31 ngày")
# elif UserInput in b:
#     print("Tháng", UserInput, "có 30 ngày")
# elif UserInput == 2:
#     print("Tháng 2 có 28 ngày hoặc 29 ngày nếu vào năm nhuận")
# else:
#     print("Không có tháng", UserInput)

# bán_kính = int(input("vẽ hình tròn có bán kính: "))
# circle(bán_kính)
# mainloop()

# from turtle import *
# a = int(input("số cạnh đa giác: "))
# for i in range(0, a+1):
#     forward(100)
#     left(120)
# mainloop()

while True:
    email = input("Enter your email: ")
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    password2 = input("Enter your password again: ")
    i = range(0, 10)
    if "@gmail" and "i" in email:
        if len(email) >= 8:
            if password2 == password:
                print("OK")
                break
            else:
                print("wrong password")
        else:
            print("invalid email, not long enough")
    else:
        print("invalid email")