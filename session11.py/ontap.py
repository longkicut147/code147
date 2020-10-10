listQuan = [
    {
    "name": "DongDa",
    "square": 9.96,
    "people": 420.900
    },
    {
    "name": "BaDinh",
    "square": 9.224,
    "people": 247.100
    },
    {
    "name": "BacTuLiem",
    "square": 43.35,
    "people": 333.300
    }
]
listpeople = []
result = 0
for item in listQuan:
    listpeople.append(item["people"])
    result = max(listpeople)

QuanMax = {}
for items in listQuan:
    if items["people"] == result:
        QuanMax = items
print(QuanMax)