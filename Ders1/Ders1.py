print("Hello World")
print("Selenium")

# merhaba
"""
python
java
c
ruby
"""
print('Fatih "Türker"')  # Fatih "Türker"
#####
x = 5
print(x - 5)  # 0

y = "hello world"
print(y)  # hello world

z= 5.0
print(z)  # 5.0

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

sayi1= int(5)
sayi2= str("hello world")
sayi3= float(5.0)

sayi4 = str(5)
print(sayi4) # 5
print(type(sayi4)) # <class 'str'>

sayi5= int("5")
print(type(sayi5)) # <class 'int'>

sayi8 = 5
print(sayi8) # 5
sayi8 =10
print(sayi8) # 10

b=5
B="str"
print(b) # 5
print(B) # str

sayi9,sayi10,sayi11="Java","Python","C"
print(sayi9) # Java
print(sayi10) # Python
print(sayi11) # C

x=y=z= "hello"
print(x,y,z) # hello hello hello

print(f"{x} world {sayi9} merhaba") # hello world Java merhaba
print("{} world {} merhaba".format(x,sayi9)) # hello world Java merhaba

x= "python" # indeksler sıfırdan başlar
print(x[0]) # p
print(x[1]) # y
print(x[2]) # t
print(x[3]) # h
print(x[4]) # o
print(x[5]) # n

print(x[-1]) # n
print(len(x)) # 6 uzunluk birden başlar

x= "python hello world"
print("hello" in x) # True ==> hello kelimesi x in içinde var mı?

# String parcalama
print(x[2:5]) # tho ==> 2. indekse git ve 5. indekse kadar alıp yazdır
print(x[2:10:2]) # to e ==> 2. indekse git ve 10. indekse kadar 2 şer 2 şer arttırarak yazdır
print(x[::]) # python hello world ==> başlangıç ve sonu belirtmezsem hepsini yazdırır
print(x[:5:]) # pytho ==> başlangıç dan 5. indekse kadar git ve yazdır

print(x.upper()) # PYTHON HELLO WORLD bütün karakterleri büyük yapar
print(x.lower()) # python hello world bütün karakterleri küçük yapar
print(x.count("t",0,20)) # t harfi kaç kere var
print(x.capitalize()) # Python hello world ==> ilk harfi büyük yapar
print(x.title()) # Python Hello World
