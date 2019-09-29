Data = ['Jeryan Haryogi', 'Sabina', 'Sfiva Salwa', 'yuni', 'Adaw', 'putri cahyani']
# mengakses lis pada variabel data
programmer = Data[0]
print('Programmer Di SMK Muhammadiyah 9 adalah', programmer)
# memotong isi array pada variabel data
Kekasih = Data[1:6]
print('Istri dari programmer jeryan adalah', Kekasih)
# menambah Data array pada variabel data
Data2 = ['Vina Nisrina', 'Maulidia Rahma', 'Alfita Najma', 'Jihan Salsabilla']
Subdata = Data + Data2
print('Hasil Dari full data', Subdata)
# eksekusi array di dalam array
dataArray = [Data + Data2]
a = dataArray[0][0]
print(dataArray)
print('Semua Perempuan Yang Ada Di Data Adalah milik', a)
# method objek pada array/list
Data.append('Fadiyah Maisahrani')
b = Data[6]
print('penambahan istri dari jeryan adalah bernama', b)
# function pada array list
panjang_array = len(Data)
print(panjang_array)