#luas persegi
s = int(input("Masukkan Sisi = "))
luas_persegi = s*s
kp= 4 *s
print("Luas Persegi = ",luas_persegi,"\nKeliling Persegi = ",kp)

#luas Persegi Panjang
p = int(input("\nMasukkan Panjang = "))
l = int(input("Masukkan Lebar = "))

luas_persegi_pnjng = p*l
kpp = 2*(p+l)
print("Luas Persegi Panjang = ",luas_persegi_pnjng,"\nKeliling Persegi Panjang = ",kpp)

#Luas Lingkaran
jari2= int(input("\nMasukkan jari-jari ="))
luas = 3.14 * jari2 * jari2
keliling = 2* 3.14 * jari2
kursus  ="Pemrograman Python Fundamental"
lembaga = 'Nurul Fikri Computer'
title = kursus + lembaga

print(title,"\nLuas lingkaran dengan jari-jari ",jari2,"adalah",luas,
"\ndan Kelilingnya adalah",keliling)