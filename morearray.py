Buah = ['Semangka', 'Jeruk', 'Apel', 'Mangga', 'Anggur', 'Rambutan', 'Pear']
print('Ini Adalah Hasi Dari Data Awal', Buah)
# beberapa method yang bisa digunakan untuk memanipulasi sebuah array / list
# menambahkan isi sebuah data pada array
Buah.append('Blimbing')
print(Buah)
print('Data Yang Nambah Pada array Adalah', Buah[7])
print('Data Menggunakan Method Extends')
Buah.extend('sawo')
print(Buah)
print('Data Yang Ditambahkan menggunakan Method Insert')
Buah.insert(5, 'Durian')
Buah.insert(4, 'Rambutan')
print(Buah)
# Menghitung ada berapa banyak data yang sama pada isi array
Jumlahisiyangsama = Buah.count('Rambutan')
print(Jumlahisiyangsama)
print(100*']=[')
print('Menghapus Data Pada Isi Array')
# memghapus data pada method list
Buah.remove('Apel')
print(Buah)
# mengcopy isi dalam Buah
Buahan = Buah.copy()
Buahan.remove('Rambutan')
print(Buahan)