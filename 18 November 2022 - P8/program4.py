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
		print('Input harus berupa angka!')
		return intInput(message)

# Jumlah sudut segitiga jika ditambah harus 180deg, but who cares anyway?
a = intInput("Masukkan besar sudut A : ")
b = intInput("Masukkan besar sudut B : ")
c = intInput("Masukkan besar sudut C : ")

if (a == c):
	
