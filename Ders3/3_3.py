# While Döngüsü
"""
Bu döngü yapısı bir koşula bağlı olarak çalışır. Eğer koşul doğru ise döngünün içerisinde bulunan
yani döngünün kapsadığı alandaki kodlar çalışır.
Döngülerin farkı koşul doğru olduğu sürece tekrar etmesidir. Yani bir döngüye girdiğinizde koşul doğru olduğu sürece
sonsuza kadar tekrar eder.

while <koşul> :
    kodlar...
    kodlar...
döngünün dışında kalan kısım

Bir döngü yapısı yukarıdaki gibidir. Koşul doğru olduğu sürece döngünün içerisinde bulunan kodlar sonsuza kadar
tekrar eder. Koşul yanlış olduğunda döngüden çıkar ve program döngüden sonraki satırlardan devam eder.
"""
# while 1==1:
#     print("Merhaba")
# print("döngünün dışı")

# sayi =0
# while sayi <= 10:
#     print(sayi)
#     sayi += 1
# print("Döngü dışı")
# While döngüsünü sonlandırmak için mutlaka koşulu geçersiz kılacak bir ifadenin döngü içerisine
# yazılması gerektiğini unutmayın.

# Örneğin bu değerleri alt alta çalıştırmak yerine yan yana yazdırmak isteseydik ne yapacaktık?
# Bunun için print() fonksiyonunun parametrelerini kullanmamız gerekiyordu. Bu fonksiyonun parametrelerinde
# varsayılan olarak bir alt satıra inme komutu bulunmaktadır. Bu komut "\n" komutudur. Komutu ise print() fonksiyonunun
# parametresi olan end parametresi ile gerçekleştiriyoruz.

sayi =0
while sayi <= 10:
    print(sayi, end=" ")  # 0 1 2 3 4 5 6 7 8 9 10 Döngü dışı
    sayi += 1
print("\nDöngü dışı") # Döngü dışı