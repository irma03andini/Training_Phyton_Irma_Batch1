# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:59:50 2022

@author: 072457
"""

#Latihan 2
print('Latihan 2')
Absen = int(input("Masukkan Absensi"))
print(Absen)

Tugas = int(input("Masukkan Nilai Tugas"))
print(Tugas)

UTS = int(input("Masukan Nilai UTS"))
print(UTS)

UAS = int(input("Masukkan Nilai UAS"))
print(UAS)
print()

NilaiAbsen = (Absen * 0.1)
NilaiTugas = (Tugas * 0.2)
NilaiUTS = (UTS * 0.3)
NilaiUAS = (UAS * 0.4)

print("Nilai Akhir")
NilaiAkhir = (NilaiAbsen + NilaiTugas + NilaiUTS + NilaiUAS)
print(NilaiAkhir)
print()

if NilaiAkhir > 80 < 100:
    print("A")
elif NilaiAkhir > 70 < 79:
    print("B")
elif NilaiAkhir > 60 < 69:
    print("C")
elif NilaiAkhir > 50 < 59:
    print("D")
else :
    print("E")