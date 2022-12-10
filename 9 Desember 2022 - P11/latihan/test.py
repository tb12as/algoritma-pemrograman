import caesar 

string = input('Encrypt string : ')
shift = int(input('Masukkan shift : '))

print('Encrypted :', caesar.caesar(string, shift))
print('Decrypted :', caesar.decrypt(string, shift))


