# While döngüsü ile karar yapılarını birleştiren örnekler yapalım.
# Örneğin basit bir hesap makinesi yapalım. Girilen iki sayıyı kullanıcının seçeceği işleme göre sonucu ekrana yazdıralım.

# menümüzü oluşturuyoruz
menu = """
###########################################
##              Hesap Makinesi           ##
##                                       ##
##      Toplama İşlemi için    (1)       ##
##      Çıkarma İşlemi için    (2)       ##
##      Çarpma İşlemi için     (3)       ##
##      Bölme İşlemi için      (4)       ##
##      Programdan Çıkmak için (5)       ##
##                                       ##
########################################### 
"""
# Başlangıçta çıkış değerini belirliyoruz
cikis = 1
# cikis degiskeni 1 olduğu sürece döngü çalışacak

while cikis == 1:
    # menümüzü çağırıyoruz
    print(menu)

    # Kullanıcıdan ilk sayi isteniyor
    sayi1 = int(input("Lütfen 1. sayiyi giriniz : "))
    # Kullanicidan ikinci sayi isteniyor
    sayi2 = int(input("Lütfen 2. sayiyi giriniz : "))

    # Kullanıcıdan işlem seçeneği isteniyor
    islem = int(input("Lütfen yapmak istediğiniz işlemi numarası giriniz : "))

    # Karar yapısına göre işlem yapılıyor
    if islem == 1:
        sonuc = sayi1 + sayi2
        print(f"{sayi1} + {sayi2} = {sonuc}")
    elif islem == 2:
        sonuc = sayi1 - sayi2
        print(f"{sayi1} - {sayi2} = {sonuc}")
    elif islem == 3:
        sonuc = sayi1 * sayi2
        print(f"{sayi1} * {sayi2} = {sonuc}")
    elif islem == 4:
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
            print(f"{sayi1} / {sayi2} = {sonuc}")
        else:
            print("Bölme işlemi sıfıra eşit olamaz!")
    elif islem == 5:
        print("Programdan çıkılıyor...")
        cikis = 0
    else:
        print("Hatalı işlem...")
