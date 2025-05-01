import math #Berfungsi untuk mengimpor modul math
from functools import reduce #Berfungsi untuk melakukan pelipatan 

print("Selamat Datang Di Program Kalkulator Sederhana") #Menampilkan Teks Selamat Datang
print("==============================================")
print("")

print("Pilih Salah Satu Opsi :") #Menampilkan Opsi Yang Bisa Dipilih
print("1. Menghitung Rata-rata")
print("2. kalkulator")

opsi = (int(input("Masukkan Pilihan Anda [1 / 2] : "))) 
#Perintah Input Untuk Menentukan Pilihan dengan tipe data Integer

print("")
print("==============================================")

#Membuat Percabangan dari bagian input opsi di line-13
if opsi == 1:
    rata2 = int(input("Masukkan jumlah Bilangan : ")) #Membuat Input dengan Tipe Data Integer

    bil = [] #Membuat Variable / Storage Untuk Menyimpan Angka Yang Akan Dihitung

    for i in range(rata2): 
        #Membuat Perulangan Dengan For dan akan mengulang sebanyak angka yang dimasukkan di variabel "rata2"
        
        bil.append(int(input(f"Masukkan Angka Ke - {i+1} : ")))
        ''' Membuat input dan angka yang dimasukkan akan disimpan didalam storage "bil" dan diulang sesuai dengan
        jumlah yang di input pada input "rata2" '''

    total = sum(bil) #Membuat Variable "total" dengan menjumlahkan seluruh angka didalam variable bil/storage

    rata_rata = float(total / rata2) #Mencari rata-rata dengan membagi variable "total" dengan "rata2"
    print(f"Hasilnya Yaitu : {rata_rata}")#Menampilkan hasil dari perhitungan rata_rata diatas

elif opsi == 2: #Membuat Opsi kedua dari percabangan di line-13
    
    print("Pilih Menu Aritmatika : ") #Menampilkan opsi pada pilihan bagian kalkulator
    print("1. Perkalian ") 
    print("2. Pembagian ")
    print("3. Penjumlahan")
    print("4. Pengurangan ")
    print("5. Perpangkatan (Kuadrat) ")
    kode = int(input("Masukkan Kode Angka [1 - 5] : ")) 
    #Membuat input dengan variable "kode" dengan tipe data Integer untuk menentukan pilihan menu

    kal = int(input("Masukkan Jumlah Bilangan Yang Ingin Dihitung : "))
    #Membuat input variable dengan nama "kal" yang memiliki tipe data integer

    kal2 = [float(input(f"Masukkan bilangan ke-{i + 1}: ")) for i in range(kal)]
    #Membuat perulangan looping dengan nama variable kal2 yang memiliki tipe data float
    #dan angka yang dimasukkan di input akan disimpan pada variable "kal2"

    if kode == 1: #Membuat Percabangan dari varible "kode"
        hasil = math.prod(kal2)#Mengalikan seluruh bilangan yang tersimpan pada variable "kal2"

    elif kode == 2: #Membuat opsi kedua dari variable "kode"
        try:#program akan menjalankan perintah dibawah jika tidak terjadi kesalahan  
            hasil = reduce(lambda x,y : x / y, kal2)

        except:#jika terjadi kesalahan, maka program akan menampilkan teks dibawah
            hasil = "Error: Pembagian Dengan Nol"

    elif kode == 3: #Membuat Percabangan opsi ketiga dari variable "kode"
         hasil = sum(kal2)#Menjumlahkan seluruh angka yang tersimpan pada variable "kal2"
    
    elif kode == 4: #Membuat percabangan opsi keempat dari variable "kode"
        hasil = kal2[0] - sum(kal2[1:])
        #Menjumlahkan seluruh angka pada variable "kal2" lalu dikurangi dengan indeks ke-0

    elif kode == 5: #Membuat Percabangan opsi kelima dari variable "kode"
        if len(kal2) == 2:
        #Membuat percabangan, dimana jika variable "kal2" bernilai 2 
        #Maka bilangan pertama akan dipangkatkan dengan bilangan
            hasil = kal2[0] ** kal2[1]
        
        else:#Jika nilai variable kal2 selain dari angka 2
             #maka program akan berjalan namun akan deiakhiri dengan hasil "Error"
            hasil = "Error"
        

    print(f"Hasilnya Yaitu : {hasil}") #Menampilkan hasil dari operasi hitung yang dipilih