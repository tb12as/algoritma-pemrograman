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


angka1 = intInput("Masukkan angka 1 : ")
angka2 = intInput("Masukkan angka 2 : ")
if (angka1 > angka2):
	print(f'{angka1} lebih besar dari {angka2}')
elif (angka1 == angka2):
	print(f'{angka1} sama dengan {angka2}')
else:
	print(f'{angka1} lebih kecil dari {angka2}')

