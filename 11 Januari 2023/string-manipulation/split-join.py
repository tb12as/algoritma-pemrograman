alamat = 'Surabaya, Jawa Timur, Indonesia'
print(alamat.split())  # ['Surabaya,', 'Jawa', 'Timur,', 'Indonesia']
print(alamat.split(','))  # ['Surabaya', ' Jawa Timur', ' Indonesia']
print(alamat.split(', '))  # ['Surabaya', 'Jawa Timur', 'Indonesia']
print('❤️'.join(['aku', 'suka', 'python']))  # aku❤️suka❤️python
print('❤️'.join(alamat.split(', ')))  # Surabaya❤️Jawa Timur❤️Indonesia
