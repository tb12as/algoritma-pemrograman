import helper
from operator import itemgetter


counter = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
}

names = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
}

data = helper.createList('data', to_dict=True)
for i in range(0, len(data)):
    # calculate nilai akhir
    val = data[i]
    aktivitas = float(val['AKT']) * (10 / 100)
    tugas = float(val['TGS']) * (20 / 100)
    uts = float(val['UTS']) * (30 / 100)
    uas = float(val['UAS']) * (40 / 100)

    final = aktivitas + tugas + uts + uas
    val['N.AKHIR'] = final

    # generate nilai huruf
    if final >= 80.51:
        nHuruf = 'A'
    elif final >= 65.61:
        nHuruf = 'B'
    elif final >= 50.51:
        nHuruf = 'C'
    elif final >= 34.41:
        nHuruf = 'D'
    else:
        nHuruf = 'E'

    val['N.HURUF'] = nHuruf
    counter[nHuruf.lower()] = counter[nHuruf.lower()] + 1
    names[nHuruf.lower()].append(val['Nama'])


# Sort the data (ref : https://stackoverflow.com/a/73050)
print("Mahasiswa berdasarkan nilai akhir")
sorted_data = sorted(data, key=itemgetter('N.AKHIR'), reverse=True)
print(f'{"No":>3}. {"Nama":40} {"AKT":5} {"TGS":5} {"UTS":5} {"UAS":5} {"N.AKHIR":5} {"N.HURUF":10}')
for i in range(0, len(sorted_data)):
    val = sorted_data[i]
    print(f'{(i+1):>3}. {val["Nama"]:40} {val["AKT"]:5} {val["TGS"]:5} {val["UTS"]:5} {val["UAS"]:5} {(round(val["N.AKHIR"], 2)):5} {val["N.HURUF"]:^10}')


# print reports
print('')
print("Laporan")
for x in counter:
    i = 1
    print(f'\nMahasiswa dengan nilai {x.upper()} : ({counter[x]}) orang', )
    for name in names[x]:
        print(f'{i:>3}. {name:40}')
        i += 1
