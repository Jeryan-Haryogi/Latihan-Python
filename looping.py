Buah = [
    'semangka', 'Jeruk', 'Apel', 'Stobery', 'Anggur', 'Rambutan'
     ]
Benda = ('Tv', 'Kipas', 'Lemari', 'Kasur', 'Bantal', 'Sajadah', 'Galon')
# looping list enumerat


for index,benda in zip(Buah,Benda):
    print(index, 'Telah terjual', benda)
print(100*'=')
i = 1
for i,list in enumerate(Buah):
    print('No', i, 'Lagi Memanen Buah', list)
    i += 1
# Membuat looping menggunakan Tuple enumarate
i = 0
print(100*'=')
for i,Benda in enumerate(Benda):
    print('Benda Yang Bernomerkan', i, 'Adalah', Benda,'Telah Terjual')
    i += 1
print(100*'=')
print('Megabungkan ISi semua dalam looping')
# menggunakan teknik looping pada set himpunan
print(100*'=')
print('Himpunan')
Makanan = {'Bakso', 'Sate', 'Ketoprak', 'Pecel', 'Soto', 'Sop'}
for index in sorted(Makanan):
    print(index)
Lagu = {'Payung teduh':'Akad', 'fourtwnty':'Zona Nyaman', 'Dilog dini Haro':'Rumahku'}
for i,v in Lagu.items():
    print(i, 'Lagunya', v)



