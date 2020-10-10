#5.1
quan = ["ST_", "BĐ_", "BTL_", "CG_", "ĐĐ_", "HBT_"]
dientich = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
danso = [150.300, 247.100, 333.300, 266.800, 420.900, 318.000]
print(quan)
print(dientich)
print(danso)

#5.2
maxdan = max(danso)
chisomaxdan = danso.index(maxdan)
print("Chỉ số của quận đông dân nhất là:", chisomaxdan)

mindan = min(danso)
chisomindan = danso.index(mindan)
print("Chỉ số của quận ít dân nhất là:", chisomindan)

#5.3
print("quận đông dân nhất là:", quan[ chisomaxdan])
print("quận đông dân nhất là:", quan[chisomindan])

