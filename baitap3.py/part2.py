#2.1
computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
computer.update({"TOSHIBA": 10})
print(computer)

#2.2
# computerInput = input("them loai may: ")
# numberComInput = int(input("so luong: "))
# computer.update({computerInput: numberComInput})
# print(computer)

#2.3
computer["DELL"] += 10
print(computer)

computer["MACBOOK"] = 2
print(computer)



