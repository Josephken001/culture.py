
cultures=[
	("Ngas", "Ngas", "Bwan", "Puusdung", ("Funkaya", "Yala")),
	("Berom", "Berom", "Gwote", "Nzem Berom",("Ashui", "shou")),
	("Afizere", "Izere", "Tuwon Mazara", "Izere Day", ("Angrari"))
]

print("1.", cultures[1][4][1])
print("2. The", cultures[0][0], "people wear", cultures[0][4][0], "and eat", cultures[0][2] )
tribe, language, food, festival, cloth_greetings = cultures[2]
print("3.", festival, "is celebrated by the", tribe, "and they eat", food)

