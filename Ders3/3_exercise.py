# KARAR YAPILARI
# Programlama da önemli yapılardan biri de karar yapılarıdır. Bu yapılar bir yazılımda belirli bir şarta göre
# ilerlememizi sağlar. Bu yapılar sayesinde biz belirli kurallara göre programımızı yönlendirebiliriz.

# Örnek1 : Kullanıcıdan yaşını isteyip bunu yaş değişkenine atadık.
# input() fonksiyonu gelen tüm değerleri string olarak kabul ediyor
# Bu nedenle direkt yaş değişkenine atama yapmadan önce int türüne dönüştürme işlemi yapıyoruz.

# yas = int(input("Lütfen yaşınızı giriniz : "))
# # Eğer yaşı 18 e eşit yada büyük ise ekranda True sonucu çıkacaktır
# if yas >= 18:
#     print("Ehliyet alabilirsiniz!")
# else:
#     print("Yaşınız 18 den küçük olduğundan ehliyet alamazsınız...")

# Örnek2 : Kullanıcıdan bir sayı isteyip bunu sayi değişkenine atadık.
# input() fonksiyonu gelen tüm değerleri string olarak kabul ediyor
# Bu nedenle direkt sayi değişkenine atama yapmadan önce  int türüne dönüştürme işlemi yapıyoruz.
# sayi=int(input("Lütfen bir sayi giriniz... : "))
# if sayi>5:
#     print("Girdiğiniz sayi 5 den büyüktür")
# elif sayi ==5:
#     print("Girdiğiniz sayi 5 e eşittir")
# else:
#     print("Girdiğiniz sayi 5 den küçüktür")

# Örnek3 : Bir öğrencinin vize ve final notu alınacaktır. Bu öğrencinin girilen vize notunun %40 'ı ve girilen final
# notunun ise %60'ı alınarak yıl sonu not ortalaması hesaplanacaktır. Bu not ortalaması eğer
# 85 ve üzeri ise AA
# 75 -85 arasında ise BA
# 70 - 75 arasında ise BB
# 65 -70 arasında ise CB
# 60 - 65 arasında ise CC
# 55 -60 arasında ise DC
# 50 55 arasında ise DD olarak hesaplanacaktır.
# Bu öğrencinin yıl sonu toplam notu 50'nin altında ise firekt FF ile kalacaktır.

# Kullanıcıdan vize ve final notunu istiyoruz
# Bu notların ortalamaları küsüratlı olabileceği için float veri tipine çeviriyoruz.

vizeNotu = float(input("Lütfen vize notunuzu giriniz : "))
finalNotu = float(input("Lütfen final notunuzu giriniz : "))

ortalama = (0.4 * vizeNotu) + (0.6 * finalNotu)

# kullanıcının hesaplanan notunu ekrana yazdırıyoruz.
print("Yıl sonu not ortalaması : " , ortalama)

# Kullanıcının final notu eğer 50 den büyükse not yazdıracak
# Eğer final notu 50 den küçükse öğrenci direk kalacak
# 50 den düşük olduğunda program en alttaki else deyiminden devam edecek
# final notu 50 ve üzeri ise ilk if deyiminin içerisine girecek ve diğer deyimler kontrol edilecektir.

if finalNotu>=50:
    if (ortalama>=85 and finalNotu>=50):
        print("AA")
    elif (ortalama>=75 and ortalama<85):
        print("BA")
    elif (ortalama>=70 and ortalama<75):
        print("BB")
    elif (ortalama>=65 and ortalama<70):
        print("CB")
    elif (ortalama>=60 and ortalama<65):
        print("CC")
    elif (ortalama>=55 and ortalama<60):
        print("DC")
    elif (ortalama>=50 and ortalama<55):
        print("DD")
    else:
        print("FF notu aldınızi kaldınız")
else:
    print("Finalden FF ile kaldınız")