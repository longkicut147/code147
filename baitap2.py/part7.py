#7.1
listnumber = [45, 67, 56, 78]

#7.2
for item in range(len((listnumber))):
    print(item+1, ".", listnumber[item])

#7.3
newscore = int(input("new score: "))
listnumber.append(newscore)
for item in range(len((listnumber))):
    print(item+1, ".", listnumber[item])

