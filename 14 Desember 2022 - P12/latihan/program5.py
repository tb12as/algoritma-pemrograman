def reverse_word(string):
    str_list = string.split(' ')
    str_list.reverse()
    return ' '.join(str_list)


print(reverse_word('Aku ganteng banget'))
print(reverse_word('Emang bener!'))
print(reverse_word('Saya sudah bisa membuat fungsi dengan python'))
