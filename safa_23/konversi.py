def konversi():
    berat = int(input("masukan berat : "))
    type = input("masukan tipe : ")

    kg = berat * 0.4
    lbs = berat * 2.2

    if type == "k":
        print(f"hasilnya adalah {lbs} L ")
    elif type == "l":
        print(f"hasilnya adalah {kg} kg")


konversi()