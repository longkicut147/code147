#3.1
computer = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
for key, value in computer.items():
    print(key,":", value)

#3.2
print(sum(computer.values()))

#3.3
computer.update({"FUJITSU": 15})
computer.update({"ALIENWARE": 5})
print(computer)

#3.4
print(sum(computer.values()))
