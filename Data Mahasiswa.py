# 2 . Program sederhana data Mahasiswa 
print("""
            =================================
            |                               |
            |        Data Mahasiswa         |
            |       ================        |    
            |                               |
            =================================
""")

x = 1
DataMahasiswa = {}
while x > 0 :
    pilihan = input("> Ingin Memasukkan Data ? y/t = ")
    print("="*56)

    if pilihan == "Y" or pilihan == "y":
        nama = str(input("> Nama = ")) 
        nim = int(input("> NIM = "))
        umur = int(input("> Umur = "))
        tinggi = float(input("> Tinggi dalam Meter = "))
        bb = float(input("> Berat Badan dalam Kg = "))

        DataMahasiswa["Nama"] = nama
        DataMahasiswa["NIM"] = nim
        DataMahasiswa["Umur"] = umur
        DataMahasiswa["Tinggi Badan"] = str(tinggi)+" m"
        DataMahasiswa["Berat Badan"] = str(bb)+" Kg"

        print("="*145)
        print("  Data Mahasiswa = ",DataMahasiswa)
        print("="*145)

    else :
        print("Program Berhenti")
        print("="*56)
        break