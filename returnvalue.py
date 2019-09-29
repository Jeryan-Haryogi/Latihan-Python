# fungsi dengan return velue
def angka(arguments):
    total = arguments*4
    print('nilai yang dimasukan dalam arguments adalah', arguments, 'dikali dengan 4 hasilnya :', total)
    return total
a = angka(4)
print('hasil dari nilai a adalah', a)

# fungsi value return dan multiple arguments
def tambah(arguments1, arguments2) :
    total = arguments1 + arguments2
    print(arguments1,'+', arguments1,'adalah', total)
    return total
print(89*'<=>')
print('hasilnya adalah', tambah(5,5))