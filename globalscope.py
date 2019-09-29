# membuat variabel scope dengan merubah nilai / variabel
Pacar = 'Sabina'
Mantan = 'Alfita Najma'
def Saya(saya, pacarbaru) :
    global  Pacar
    Pacar = pacarbaru
    print('pacarnya si', saya, 'pacar barunya adalah', Pacar)
Saya(saya='jeryan', pacarbaru='robiatuladawiyah')
print(60*':=:')
def Baru(saya, mantan):
    global Pacar, Mantan
    Pacar = saya
    Mantan = mantan
    print('mantanku yang dulu adalah', Pacar, 'pacar baru', Mantan)
Baru(saya='Adaw', mantan='Aflta')