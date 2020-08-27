# 1: in cac dong so theo thu tu
print("1 2 3 4 5 6")
print("100 101 102 103 104 105")
print("9 8 7 6 5 4 3 2")

# 2: in cac so tu 0 den 20
for i in range(0, 21, 1):
    print(i)

# 3: in cac so tu 1 den n 
n = int(input("nhap 1 so bat ki: "))
for i in range(0, n + 1, 1):
    print(i)

# 4: in cac so tu 5 den 12
for i in range(5, 13, 1):
    print(i)

# 5: in cac so tu 5 den n
n = int(input("nhap 1 so bat ki: "))
for i in range(5, n + 1, 1):
    print(i)

# 6: in cac so tu 20 den 10
for i in range(20, 9, -1):
    print(i)

# 7: in cac so tu n den m voi dieu kien n lon hon m
n = int(input("nhap so n: "))
m = int(input("nhap so m: "))
if m < n:
    for i in range(n, m - 1, -1):
        print(i)

# 10: tinh tong cac so trong khoang tu 1 den N
N = int(input("nhap so N: "))
for i in range(1, N, 1):
    N = N + i
print(N)



