#4.1
price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000
}
# print(price)

#4.2
# print(price["ASUS"])

#4.3
computerInput = input("computer: ")
print("The price of that computer is: ", price[computerInput])