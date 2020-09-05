#2.1
sheep_size = [5, 7, 300, 90, 24,  50, 75]
print(sheep_size)

#2.2
# the_biggest_sheep = max(sheep_size)
# print("the biggest sheep is", the_biggest_sheep)

# #2.3
# sheep_size.index(the_biggest_sheep)





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

