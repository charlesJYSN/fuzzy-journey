temp = eval(input(" Temperature outside?"))

if temp <= 0:
	print("Freezing temperature")

elif temp >=1 and temp <=20:
	print("Extremely cold")

elif temp >=21 and temp <=30:
	print("Moderately cold")

elif temp >=31 and temp <=37:
	print("Lukewarm")

elif temp >=38 and temp <=45:
	print("Hot")

elif temp >=46 and temp <=50:
	print("Boiling hot")

elif temp >= 51:
	print("Dangerous Temperature")
else:
	print("Invalid temperature")