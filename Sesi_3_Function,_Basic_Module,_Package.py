#!/usr/bin/env python
# coding: utf-8

# In[4]:


def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)
    
my_function(2,4)
    


# In[5]:


def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# In[9]:


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)


# In[13]:


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = "BFI")


# In[14]:


# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=4, name="Irma" )


# In[17]:


# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="Irma" )
printinfo( name="Andini" )


# In[18]:


def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


# In[19]:


def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(vartuple) # Menghitung ada berapa data after Argument 1 (70), jika contoh dibawah habis 70 = 60,50,"a" maka akan ke print 3
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )


# In[28]:


# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

def sum(arg1, arg2):
    return arg1 + arg2 #Dari contoh hanya tambahkan return saja
    
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))


# In[50]:


def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)


# In[51]:


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahHewan()
jumlahKelinci()


# In[36]:


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahKelinci()
jumlahHewan()


# In[37]:


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

print(jumlahKelinci(),jumlahHewan())


# In[38]:


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

print(jumlahKelinci(),jumlahHewan(), jumlahKelinci()+jumlahHewan())


# In[52]:


total = 0; 

def sum( arg1, arg2 ):

   total = arg1 + arg2; 
   print("Inside the function local total : ", total)
   return total;

def min():
    
    sum( 10, 20 );
print("Outside the function global total : ", total)


# In[53]:


s = "Hacktiv8-PTP Python For Data Science"
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

print(s)
print(a)
foo('quux')
x = Foo()
print(x)


# In[56]:


a = [100, 200, 300]
print('a =', a)

