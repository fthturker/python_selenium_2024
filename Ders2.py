# Aritmatik operatörler
"""
+   ==> toplama
-   ==> çıkarma
/   ==> bölme
*   ==> çarpma
%   ==> mod
**  ==> üs alma
//  ==> tam bölüm
"""
print("hello" + " world")  # hello world
print("hello" * 3)  # hellohellohello
print(5 % 2)  # 1
print(2 ** 3)  # 8
print(15 / 4)  # 3.75
print(int(15 / 4))  # 3
print(15 // 4)  # 3

# Atama Operatörleri
x = 5
print(x)  # 5
x = x + 3
# x += 3
print(x)  # 8

# Karşılaştırma operatörleri
x = 5
y = 3
print(x == y)  # False
print(x != y)  # True
print(x > y)  # True
print(x < y)  # False
print(x >= y)  # False
print(x <= y)  # True

# Mantıksal Operatörler
print(4 == 4 and 5 == 5)  # True
print(4 > 3 and 5 > 3)  # False

print(4 == 4 or 5 == 5)  # True
print(4 > 3 or 5 > 3)  # True

print(3 < 1 and 4 > 5 or 2 < 4)  # True

diller = "python java c ruby"
print("c#" in diller)  # False

mylist = ["merhaba", 1, 5.0, True]
print(type(mylist))  # <class 'list'>
print(mylist)  # ['merhaba', 1, 5.0, True]
print(mylist[0])  # merhaba

# merhaba yazısını elemanını "hello" olarak değiştirmek istiyorum
mylist[0] = "hello"
print(mylist)  # ['hello', 1, 5.0, True]

mylist.insert(2, "py")
print(mylist)  # ['hello', 1, 'py', 5.0, True]

myTuple = ('merhaba', 1, 5.0, True)
print(type(myTuple))  # <class 'tuple'>
print(myTuple)  # ('merhaba', 1, 5.0, True)

a = list(myTuple)
print(type(a))  # <class 'list'>
a[0]="Hello"
myTuple= tuple(a)
print(type(myTuple)) # <class 'tuple'>
print(a) # ['Hello', 1, 5.0, True]
