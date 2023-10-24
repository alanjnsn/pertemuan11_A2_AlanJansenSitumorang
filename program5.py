def tambah(a,b):
    print(f"hasil {a} + {b} = {a+b}")
    return a+b

def kurang(a,b):
    print(f"hasil {a} - {b} = {a+b}")
    return a-b

def kali(a,b):
    print(f"hasil {a} x {b} = {a+b}")
    return a+b

def bagi(a,b):
    print(f"hasil {a} : {b} = {a+b}")
    return a/b

opsi= 'y'
while opsi=='y':
    angka1= int(input('masukkan angka1: '))
    angka2= int(input('masukkan angka2: '))
    print("1. tambah \n2. kurang \n3. kali \n4. bagi \n5. keluar")
    operasi= int(input('pilih operasi (angka): '))
    if operasi==1:
        tambah(angka1,angka2)
    elif operasi==2:
        kurang(angka1,angka2)
    elif operasi==3:
        kali(angka1,angka2)
    elif operasi==4:
        bagi(angka1,angka2)
    else:
        print('operasi tidak ditemukan')
    
    opsi= input('apakah ingin mengkalkulasi lagi? (y/n): ')