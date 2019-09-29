import  sys
# list
Data = ['Jeryan Haryogi', 'Sabina', 'Putri Cahyani', 'RobiatulAdawiyah']
# tuple
Data2 = ('Jeryan Haryogi', 'Sabina', 'Putri Cahyani', 'RobiatulAdawiyah')
# besarnya data
besar_Data = sys.getsizeof(Data)
besar_Data2 = sys.getsizeof(Data2)
Data.append('Fadiyah Maisahrani')
coba = Data2.count('Jeryan Haryogi')
print(Data)
print(dir(Data2))
print(90*'=')
print(besar_Data)
print(besar_Data2)
