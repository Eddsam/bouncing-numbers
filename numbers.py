print("incresar porcentaje como entero (99)")
porc = int(input()) # porcentaje
bun = 0

# increasing number
def increasing_number(num):
	listnumber = [int(x) for x in str(num)] 
	for j in range(len(listnumber) - 1):
		if (listnumber[j] > listnumber[j + 1]):
			return 0

	return 1

# decreasing number
def decreasing_number(num):
	listnumber = [int(x) for x in str(num)] 
	for j in range(len(listnumber) - 1):
		if (listnumber[j] < listnumber[j + 1]):
			return 0

	return 1

n = 0
while True:
	n = n + 1
	if (increasing_number(n) == 0 and decreasing_number(n) == 0):
		bun = bun + 1

	if (((bun) * 100 / n) >= porc):
		break

print("El numero ", n, " es tal que la proporcion llega hasta el ", porc, "%")
