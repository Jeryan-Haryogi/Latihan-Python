from collections import  deque
antrian = deque([1,2,3,4,5,6,7,8,9])
print('Data Saat Ini Adalah', antrian)
# menambahkan lagi data
antrian.append(11)
print('Data Yang Masuk Adalah', 11)
print(antrian)
# menghapus bagian kirim data
keluarData = antrian.popleft()
print('Data Yang Keluar adalah', keluarData)
print(antrian)

keluarData = antrian.popleft()
print('Data Yang Keluar adalah', keluarData)
print(antrian)
antrian.append(12)
print(antrian)