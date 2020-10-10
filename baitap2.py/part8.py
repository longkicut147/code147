#8.1 + 8.2
listnumber = [45, 67, 56, 78]
listnumber.sort(reverse=True)
for item in range(len((listnumber))):
    print(item+1, ".", listnumber[item])

while True:
    newscore = int(input("new score: "))
    if newscore not in listnumber:
        listnumber.append(newscore)
        listnumber.sort(reverse=True)
        for item in range(len((listnumber))):
            print(item+1, ".", listnumber[item])
