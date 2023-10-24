def total_tertentu(daftar_angka,pemisah):
    for angka in daftar_angka:
        print(angka,pemisah, sep=",", end=",")
    print()
    total=0
    for angka in daftar_angka:
        if angka%pemisah==0:
            total+=angka
        else:
            continue

    print(f"total angka yang habis dibagi {pemisah} = {total}")



total_tertentu([3,5,6,4],2)
print()
total_tertentu([4,6,9,7,6],3)