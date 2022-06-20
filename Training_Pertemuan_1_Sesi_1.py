# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Untuk Phyton ini sangat sensitif, terutama untuk String

#Print : Untuk cek hasilnya dari yang dibuat
print() 


#Integer
print(123123+1) 
print(10)
print(type(10)) #Print type ini khusus untuk cek type data yang digunakan
print()

#Floating : Nilai float ditentukan dengan titik desimal
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)
print()

#String : data karakter
#Untuk String diwajibkan menggunakan Kutip
print("BFI")
print(type("BFI"))
print()

#Boolean :Objek tipe Boolean mungkin memiliki salah satu dari dua nilai, True atau False
#Untuk True/False : tidak perlu menggunakan "" dikarenakan type data ini untuk Boolean bukan String
print(True)
print(False)
print()

#Variable Assignment
#n = variable (bebas)
n=300
print(n)
print()

#Latihan 1
a=10
t=20
n=(a*t)/2
print(n)
print()

#Python juga memungkinkan chained assignment, yang memungkinkan untuk menetapkan nilai yang sama ke beberapa variabel secara bersamaan
a=b=c=300
print(a,b,c)
print()

#Variable Types in Python
#var = variable (bebas mau diganti apapun)
var = 23.5
print(var)
print()

var = "Now I'm a string"
print(var)
print()

#Variable Names : bisa terdiri dari huruf besar dan huruf kecil (A-Z, a-z), digit (0-9), dan karakter garis bawah (_)
#Nama variabel tidak boleh dimulai dengan angka contoh : 9_kepala_naga = True
name = "Irma"
Age = 28
has_laptops = True #Type data bersifat Boolean
print(name,Age,has_laptops)
print()

#Huruf kecil dan huruf besar tidak sama. Penggunaan karakter garis bawah juga penting.
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
print()

#Contoh 2
age = 1
Age = 2
aGe = 3
AGE = 4
AGE = 9 #yang dipanggil hanya nilai yang terbaru saja
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

print(age, Age, aGe, AGE, AGE,a_g_e, _age, age_, _AGE_)
print()

#Operators and Expressions in Python : 
a=10
b=20
print(a+b)
#jika mau ditambahkan variable kembali bisa, misal
a=10
b=20
c=a+b
print(c)
print()

#contoh 2
a=10
b=20
a+b-5
print(a+b-5)
#Jika perkalian
a=10
b=20
a+b*5
print(a+b*5)
print()

#Arithmetic Operators
a = 4
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) #Fungsi Mode/Modulus
print(a ** b) #Fungsi kuadrat Contoh 4 pangkat 3 = 4 * 4 * 4 = 64
print()

#Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
print()
#Contoh 2
a = 30
b = 30
print(a == b)
print(a <= b)
print(a >= b)
print()

#String Manipulation
s = 'foo'
t = 'bar'
u = 'baz'
print(s + t)
print(s + t + u)
print('BFI ' + 'FINANCE')






