from random import randint


jari = ['jempol', 'telunjuk', 'kelingking']
computer = {'telunjuk': ['jempol'], 'kelingking': [
    'telunjuk'], 'jempol': ['kelingking']}

print('Masukkan :q untuk keluar')
while True:
    pemain = input(', '.join([v.title() for v in jari]) + '? ')
    pemain = pemain.lower()
    if pemain in jari:
        # https://stackoverflow.com/questions/68783326/unpack-list-of-list-python
        komputer = [*computer[pemain], pemain][randint(0, 1)]
        # print('Menang atau seri :', [*computer[pemain], pemain])
        if pemain == komputer:
            print('Seri!')
        elif pemain == 'jempol':
            if komputer == 'telunjuk':
                print('Kamu menang')
            elif komputer == 'kelingking':
                print('Kamu kalah')
        elif pemain == 'telunjuk':
            if komputer == 'kelingking':
                print('Kamu menang!')
            elif komputer == 'jempol':
                print('Kamu kalah')
        elif pemain == 'kelingking':
            if komputer == 'jempol':
                print('Kamu menang!')
            elif komputer == 'telunjuk':
                print('Kamu kalah')

        print(f'{"":5} {pemain} vs {komputer}\n')

    else:
        if (pemain == ':q'):
            break
        print('Pilihan yang anda masukkan salah.')
