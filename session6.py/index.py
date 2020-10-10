# list_mon_an = ["thit cho", "thit meo"]
# list_mon_an.append("thit ga") #thêm thit ga (CREAT)

# # mon_an_moi = input()
# # list_mon_an.append(mon_an_moi)

# # length = len(list_mon_an) 
# # for i in range(length):
# #     print(list_mon_an[i])

# # for index, item in enumerate(list_mon_an):
# #     print(index, item)  

# # list_mon_an[0] = "chó thịt" #thay thit cho bằng chó thịt
# # list_mon_an.remove("chó thịt") #xóa chó thịt (UPDATE)
# # list_mon_an.pop(0) #xóa theo thứ tự

# for item in list_mon_an:
#     print(item)


# C.R.U.D
# Create
favorite = ["esport", "soccer", "pes", "motor"]
#Read
print(favorite)
# Update
favorite[0] = "sport"        # thay esport thành sport
favorite.append("badminton") # thêm badminton
print(favorite)
# Delete
favorite.pop()   # xóa phần tử theo thứ tự trong ()
print(favorite)

# for i in favorite:
#     if i == "soccer":
#         print(i)
#     else:
#         break

# kiểm tra phần tử tồn tại trong 1 list
# if "soccer" in favorite:
#     print("hello")
# else:
#     print("not found")

# tính tổng các phần tử trong list
# myNunmber = [1, 3, 7, 9, 10, 23]
# result = 0
# for item in myNunmber:
#     result += item
# print(result)

# hoặc
# print(sum(myNumber))

# userInput = input("Enter list item and split by ',': ")
# print(userInput.split(','))



#2.1
sheep_size = [5, 7, 300, 90, 24,  50, 75]
print(sheep_size)

#2.2
# the_biggest_sheep = max(sheep_size)
# print("the biggest sheep is", the_biggest_sheep)

# #2.3
# sheep_size.index(the_biggest_sheep)




#sheep.py
#chữa
for month in range(4):
    max_size = 0
    for size in sheep_size:
        if size > max_size:   #cách tính max theo thuật toán tự chế
            max_size = size
    print(max_size)

    max_size_index = sheep_size.index(max_size)
    sheep_size[max_size_index] = 8
    print(sheep_size)

    for index, item in enumerate(sheep_size):
        # sheep_size[index] = item + 50
        sheep_size[index] += 50
    print(sheep_size)

# total = sum(sheep_size)
# print(total)
total = 0
for item in sheep_size:
    total += item
    print(total)



#freakingmath.py

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