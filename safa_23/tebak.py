def tebak():
    secret_num = 10
    guess_max = 3
    guess = 0

    while guess < guess_max:
        user = int(input("masukan angka tebakan anda : "))
        if user == secret_num:
            print("selamat anda benar")
            break
        else:
            print("SALAH!")
            guess += 1
    else:
        print(f"anda gagal menebak, angka rahasianya adalah {secret_num}")

tebak()