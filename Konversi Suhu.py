# Program Konversi Suhu
print("""
             =================================
             |                               |
             |         Konversi Suhu         |
             |        ===============        |    
             |                               |
             =================================
""")
x = 1

while x > 0 :
    pilihan = (input("> F (Farenheit) \n> K (Kelvin)\n> R (Reamur)\n  Pilih salah satu Suhu yang ingin di ubah ke C  =  "))
    print("="*56)
    if pilihan == "F" or pilihan == "f":
        f = float(input("  Suhu F = "))
        c = (f-32)*5/9
        print("|------------------Mengkonversi F ke C-----------------|")
        print("  C =",c,"°C")
        print("="*56)
        ulang = input("Konversi lagi ? y/t = ")
        print("="*56)
        if ulang == "y" or ulang == "Y" :
            continue
        else :
            print("Program Berhenti")
            print("="*56)
            break

    elif pilihan == "K" or pilihan == "k":
        k = float(input("  Suhu K = "))
        c = k-273.15
        print("|------------------Mengkonversi K ke C-----------------|")
        print("  C =",c,"°C")
        print("="*56)
        ulang = input("Konversi lagi ? y/t = ")
        print("="*56)
        if ulang == "y" or ulang == "Y" :
            continue
        else :
            print("Program Berhenti")
            print("="*56)
            break
        
    elif pilihan == "R" or pilihan == "r":
        r = float(input("  Suhu R = "))
        c = r/0.8
        print("|------------------Mengkonversi R ke C-----------------|")
        print("  C =",c,"°C")
        print("="*56)
        ulang = input("Konversi lagi ? y/t = ")
        print("="*56)
        if ulang == "y" or ulang == "Y" :
            continue
        else :
            print("Program Berhenti")
            print("="*56)
            break

    else: 
        print("Inputan tidak diketahui")
        print("="*56)
        ulang = input("Konversi lagi ? y/t = ")
        print("="*56)
        if ulang == "y" or ulang == "Y" :
            continue
        else :
            print("Program Berhenti")
            print("="*56)
            break