#6.1
quan = ["ST_", "BĐ_", "BTL_", "CG_", "ĐĐ_", "HBT_"]
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150.300, 247.100, 333.300, 266.800, 420.900, 318.000]

dientich.sort(reverse=True)
print(dientich)

a = 150.300 / 117.43 
b = 247.100 / 9.224
c = 333.300 / 43.35
d = 266.800 / 12.04
e = 420.900 / 9.96
f = 318.000 / 10.09
matdo = [a, b, c, d, e, f]
matdo.sort(reverse=True)
print("Mật độ dân cư là: ", matdo)

#6.2
x = sum(matdo)
matdotrungbinh = x / 6
print("Mật độ trung bình là: ", matdotrungbinh)

