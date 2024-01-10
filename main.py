def perhitungan():
    while True:
        angka1 = int(input("masukan angka : "))
        angka2 = int(input("masukan angka : "))
        operator = input("ingin perhitungan apa ( +, -, *, / ) ?  ")

        tambah = angka1 + angka2
        kali = angka1 * angka2
        kurang = angka1 - angka2
        bagi = angka1 / angka2

        if ( operator == "+" ):
            print(f"hasil dari penambahan {angka1} dan {angka2} adalah {tambah}")
        elif ( operator == "-" ):
            print(f"hasil dari pengurangan {angka1} dan {angka2} adalah {kurang}")
        elif ( operator == "*" ):
            print(f"hasil dari perkalian {angka1} dan {angka2} adalah {kali}")
        elif ( operator == "/" ):
            print(f"hasil dari pembagian {angka1} dan {angka2} adalah {bagi}")
        print("")
        lagi = input("Ingin menghitung lagi (y/n)? ")
        if lagi == "n":
            print("Terima kasih")
            break



perhitungan()