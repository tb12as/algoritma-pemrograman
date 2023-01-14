# 1 Format Specifiers
template = 'Halo, saya %s dari %s'
print(template % ('Syafiq Afifuddin', 'Indonesia'))

# 2 format() function
template = 'Halo, saya {nama} dari {asal}'
template_2 = 'Saya suka makan {} dan minum {}'
print(template.format(nama='Syfiq Afifuddin', asal='Indonesia'))
print(template_2.format('Nasi Goreng', 'air putih'))

# 3 f-strings
nama = 'Syafiq Afifuddin'
asal = 'Indonesia'
print(f'Perkenalkan saya {nama} dari {asal} 😎')
