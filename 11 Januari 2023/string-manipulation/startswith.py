phone1 = '0871122334455'
phone2 = '6288776655300'
phone3 = '+6233003300330'
country_code = '+62'

print(phone1.startswith(country_code))  # False
print(phone2.startswith(country_code))  # False
print(phone3.startswith(country_code))  # True
