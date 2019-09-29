nama = 'Jeryan Haryogi'
nama2 = 'Sabina'
if nama is not nama2 :
    print("anda Tidak cocok berhubungan dengan dia")
elif nama is nama2 :
    print('Anda Cocok Sekali Dengan Si ', nama2)
else:
    print("anda Cocok Dengan", nama2)
print(50*'=')
# logika pengkondisian
makanan = ['Nasi Goreng', 'Nasi Uduk', 'Nasi Pecel', 'Gorengan', 'ketoprak', 'Soto Betawi']
sarapan = 'Nasi Uduk'
if sarapan in makanan:
    print('Sarapan Pagi Saya Adalah', sarapan,'Bude mie')
elif not sarapan in makanan :
    print("saya leper ingin sarapan pagi")
else:
    print("Saya Tidak makan Seharian")

