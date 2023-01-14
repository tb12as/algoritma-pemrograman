# This shit doesnt work
def quick_sort(list, awal, akhir):
    if awal < akhir:
        pindex = partisi(list, awal, akhir)
        quick_sort(list, awal, pindex - 1)
        quick_sort(list, pindex + 1, akhir)
    return list


def partisi(list, awal, akhir):
    tengah = int(akhir / 2)
    pivot = list[tengah]
    pindex = awal
    for i in range(awal, tengah):
        if list[i] >= pivot:
            list[i], list[pindex] = list[pindex], list[i]
            pindex = pindex + 1

    list[pindex], list[tengah] = list[tengah], list[pindex]
    print(list)
    return pindex


list = [67, 91, 87, 33, 49, 10, 16, 43, 65, 3]
print('hasil ', quick_sort(list, 0, len(list) - 1))
