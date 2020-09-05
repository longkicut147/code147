
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
