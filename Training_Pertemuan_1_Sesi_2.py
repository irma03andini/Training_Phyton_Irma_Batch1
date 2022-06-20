# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:15:51 2022

@author: 072457
"""

#Introduction to the if Statement
print('Introduction to the if Statement')
print('Contoh 1')
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')
if x:                                # Falsy
    print('yes')
if y:                                # Truthy
    print('yes')
if 'aul' in 'grault':                # Truthy
    print('yes')
if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')
print()

#Contoh 2
print('contoh 2')
if 'foo' in ['bar', 'baz', 'qux']: #Jika Foo tidak ada di dalam [] maka akan mengambil Print terakhir
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')
print()

#Contoh 3
print('Contoh 3')
if 'foo' in ['bar', 'baz', 'qux','foo']: #Jika Foo ada di dalam [] maka akan mengambil All prrnt
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')
print()

#Contoh 4
print('Contoh 4')
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print()

#Contoh 5
print('Contoh 5')
x = 120

if x < 120:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print()

#Contoh 6
print('Contoh 6')
x = 120

if x < 120:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')
print()

#Contoh 7
print('Contoh 7')
hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")
print()

#Contoh 8
print('Contoh 8')
if 'f' in 'foo': print('1'); print('2'); print('3')
print()

#Looping
print("Contoh 1 Looping")
n = 5
while n > 0:
    n -= 1
    print(n)
    print()
    
print("Contoh 2")
i = 1
while i < 6:
  print(i)
  i += 1
  print()
  
print("Contoh 3")
#Dikarenakan ada fungsi Break sehingga hasilnya hanya sampai 3 dan 2 tidak tercetak
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

print("Contoh 4")
