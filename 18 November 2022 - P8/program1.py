def isInt(num):
	try:
		int(num);
		return True;
	except Exception:
		return False

def intInput(message):
	number = input(message)
	if (isInt(number)):
		return int(number)
	else:
		print('Input harus berupa angka')
		return intInput(message)


angka = intInput("Masukkan angka : ")
if (angka >= 0):
	print(f'Angka {angka} adalah angka positif')
else:
	print(f'Angka {angka} adalah angka negatif')

