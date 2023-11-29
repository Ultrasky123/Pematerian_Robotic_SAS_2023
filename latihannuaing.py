import fungsilatihannuaing

while True:
    print("Kalkulator Sederhana")
    awal = int(input("Masukan Nilai Awal = "))
    akhir = int(input("Masukan Nilai Akhir = "))

    print( "Nilai Awal", awal)
    print("Nilai Akhir", akhir)
    print("Beberapa Pilihan Operasi")
    print("1. penambahan")
    print("2. pengkurangan")
    print("3. pengkalian")
    print("4. pembagian")

    pilihan = int(input("Input Operasi = "))

    if pilihan == 1:
        print ("Hasil dari Penambahan = ", fungsilatihannuaing.penambahan(awal,akhir))
    elif pilihan == 2:
        print ("Hasil dari Pengurangan = ", fungsilatihannuaing.pengkurangan(awal,akhir))
    elif pilihan == 3:
        print ("Hasil dari Pengalian = " ,fungsilatihannuaing.pengkalian(awal,akhir))
    elif pilihan == 4:
        if akhir == 0:
            print("Tidak bisa dipembagian 0")
        else:
            print ("Hasil dari Pembagian = ",fungsilatihannuaing.pembagian(awal,akhir))
    else:
        print ("Masukan pilihan operasi yang benar")

    kelanjutan = input("Apakah anda ingin menlanjutkan program? (y/n)")
    if kelanjutan.lower() =='n':
        print("Program selesai")
        break