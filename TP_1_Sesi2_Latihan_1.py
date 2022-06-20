# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:43:32 2022

@author: 072457
"""
#Latihan 1
print('Latihan 1')
HargaBuku = int(input("Berapa Harga Bukunya ?"))
print(HargaBuku)

JumlahBeli = int(input("Berapa yang mau dibeli ?"))
print(JumlahBeli)

TotalBelanja = (HargaBuku*JumlahBeli)
print(TotalBelanja)

Uang = int(input("Input Uangnya"))
print(Uang)

if(Uang > TotalBelanja):
    print("Uang Cukup")
elif(Uang > HargaBuku):
    print("Bisa kebeli barangnya")
else :
    print("Tidak Cukup Ya Uangnya")
print()