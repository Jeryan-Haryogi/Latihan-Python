# ini merupakan function biasa
def Coba():
    print('Hallo Word')
# yang diisikan dengan argumnents
def Coba2(nama,jual,harga) :
    harga = harga
    print('Si',nama,'Menjual', jual,'dengan harga', harga)
def latihan1(nama, kelas, sekolah):
    print('Siswa ini bernama', nama)
    print('dia kelas', kelas)
    print('sekolah di', sekolah)
Coba()
print(6*'=')
Coba2('Jeryan', 'kopi', 20000)
# cara lain dengan keywords arguments
Coba2(nama='Sabina',jual='brwonies',harga=20000)
print(6*'=')
latihan1(nama='jeryan',kelas=21,sekolah='smk')