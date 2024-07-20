# Bir sayının değerini 5 azaltmak
# Sonucu tekrar o sayıya atamak
a = 10
a -= 5
print(a)  # 5

# bir sayının değerini 2 ile çarpmak
# Sonucu tekrar o sayıya atamak
b = 10
b *= 2
print(b)  # 20

# bir sayının değerini 4'e bölmek
# Sonucu tekrar o sayıya atamak
c = 10
c /= 4
print(c)  # 2.5

# bir sayının 2 kuvvetini almak
# sonucu tekrar o sayıya atamak
d = 10
d **= 2
print(d)  # 100

# Liste Veri Tipi
# List Tipi: sıralanabilen, değiştirilebilen ve yinelenen üyelere izin veren koleksiyon tipinde bir veri tipidir.
# Köşeli parantez "[]" ile oluşturulur.
# BOŞ BİR LİSTE OLUŞTURMAK
liste = []
print(type(liste))  # <class 'list'>

# LİSTE OLUŞTURMAK
meyveler = ["Elma", "Armut", "Kivi", "Çilek"]

# BİR LİSTE'NİN ELEMAN SAYISINI BULMAK
print(len(meyveler))  # 4

# BİR LİSTENİN ELEMANLARINA ULAŞMAK
print(meyveler[0])  # Elma
print(meyveler[1])  # Armut
# Burada dikkat etmemiz gereken ilk nokta listenin eleman sayısı ile indis numaralarının farklı olmasıdır.
# Bunun sebebi indis numaralandırılırken 0'dan başladığı içindir. Listenin 1. elemanı "Elma" iken; "Elma" elemanının
# indisi 0'dır. Buna özellikle dikkat etmeliyiz. Bir listede olmayan indis değerine erişmeye çalışırsak program
# hata verecektir.
# print(meyveler[5]) # hata verir

# BİR LİSTENİN ELEMANINI DEĞİŞTİRMEK
meyveler[0] = "Muz"
print(meyveler)  # ['Muz', 'Armut', 'Kivi', 'Çilek']

# FARKLI TÜRLERE SAHİP LİSTE OLUŞTURMAK
farkli = ["Bir değer", 5, False, True, 2.2]
print(farkli[0]) # Bir değer
print(len(farkli)) # 5

# LİSTEYE APPEND() FONKSİYONU İLE ELEMAN EKLEMEK
meyveler.append("Portakal")
print(meyveler)  # ['Muz', 'Armut', 'Kivi', 'Çilek', 'Portakal']

# LİSTEYE INSERT() FONKSİYONU İLE ELEMAN EKLEMEK
# append() fonksiyonu daima listenin sonuna değer eklemesi yapıyordu.
# Fakat biz istediğimiz bir indise veri eklemek istersek ne yapacağız? Bunun için insert() fonksiyonu kullanacağız.
# Bu fonksiyonun ilk parametresi veriyi eklemek istediğimiz indis numarasını belirtmemize yararken,
# ikinci parametresi ise eklemek istediğimiz veriyi yazmamızı bekler.
meyveler.insert(2, "Erik")
print(meyveler)  # ['Muz', 'Armut', 'Erik', 'Kivi', 'Çilek', 'Portakal']

# LİSTEDEN REMOVE() FONKSİYONU İLE ELEMAN ÇIKARMAK
meyveler.remove("Kivi")
print(meyveler)  # ['Muz', 'Armut', 'Erik', 'Çilek', 'Portakal']

# LİSTEYE POP() FONKSİYONU İLE ELEMAN ÇIKARMAK
# Bu fonksiyon ile listeden belirli bir indeksdeki veriyi çıkartabiliriz. Silmek istediğimiz elemanın indis numarasını
# vererek bu elemanı listeden çıkartabiliriz. Eğer pop() fonksiyonuna parametre vermezsek son elemanı silecektir.
print(meyveler.pop()) # Portakal
print(meyveler.pop(1)) # Armut

# LİSTE ELEMANLARINI REVERSE() FONKSİYONU İLE TERSİNE ÇEVİRMEK
print(meyveler) # ['Muz', 'Erik', 'Çilek']
meyveler.reverse()
print(meyveler)  # ['Çilek', 'Erik', 'Muz']

# LİSTENİN EN KÜÇÜK VE EN BÜYÜK ELEMANLARINI BULMAK
sayilar=[4,10,2,1,78,12,3]
print(min(sayilar)) # 1
print(max(sayilar)) # 78
# Bu fonksiyonları kullanabilmek için listenin tüm elemanlarının aynı türde olması gerekmektedir.

# TUPLE (DEMET) VERİ TİPİ
# Bu veri tipi diğer programlama dillerindeki dizi veri tiplerine benzemektedir. "()" sembolleri ile gösterilir.
# Demetler sıralanabilen ancak listelerin aksine değiştirilemeyen koleksiyon türüdür.
# BOŞ BİR TUPLE OLUŞTURMAK
demet=()
print(demet) # ()
print(type(demet))  # <class 'tuple'>

# TUPLE OLUŞTURMAK
sayilar=(1,3,5,7,9,2)

# BİR DEMETİN ELEMAN SAYISINI BULMAK
print(len(sayilar)) # 6

# TEK ÖĞELİ DEMET OLUŞTURMAK
demet=("örnek")
print(demet) # ('örnek')
print(type(demet))  # <class 'str'>
# bir tuple oluşturmak istersek ilk elemanın yanına virgül koymamız gerekir.
# Aksi halde python dili bu ifadeyi string olarak algılayacaktır.
demet=("örnek", )
print(type(demet)) # <class 'tuple'>

# BİR DEMETİN ELEMANLARINA ULAŞMAK
sayilar=(1,5,7,9,2)
print(sayilar[0]) # 1
# Demetlerden elemanlara -aynı listelerde olduğu gibi- köşeli "[ ]" içerisine elemanın indis değerini yazarak
# bu işlemi gerçekleştirebiliriz.

# BİR DEMETİN ELEMANINI DEĞİŞTİRMEK
# Demetler, listeler gibi değiştirilebilen veri tipleri değildir.
# Bir demetin elemanlarını değiştiremezsiniz.

# NOT: Tuple veri tipi immutable (değiştirilemez) türünde olduğu için listelerde yaptığımız eleman ekleme
# çıkarma işlemlerini yapamayız. Bir tuple tanımlandıktan sonra değiştirilemez.

# SET (KÜME) VERİ TİPİ
# BOŞ KÜME OLUŞTURMAK
kume=set()
print(kume) # set()
print(type(kume))  # <class 'set'>
# Henüz değer ataması yapılmadan boş bir küme oluşturmak için set() fonksiyonu kullanılır.

# KÜME OLUŞTURMAK
kume=set("a")
print(kume) # {'a'}

liste=["Elma","Armut","Kivi","Çilek"]
kume=set(liste)

demet=("Elma","Armut","Kivi","Çilek")
kume=set(demet)
# bir listeyi ve demeti kümeye eleman olarak verebiliyoruz.
# bir sayı ile küme oluşturamıyoruz.
sayi=1
# kume=set(sayi) # TypeError: 'int' object is not iterable

# DİCTİONARY (SÖZLÜK) VERİ TİPİ
# Sözlükler, yani ingilizce adı ile Dictionary, Python dilinde elemanları sırasız bir şekilde tutan ve
# elemanları arasında "anahtar - değer" ilişkisi bulunan, indis değeri tutan "koleksiyon" türünde bir yapıdır.
# Sözlük tanımlanırken "{}" süslü parantez sembolü kullanılır. Her bir değerin tutulduğu ve değere karşılık gelen
# anahtar diye tanımlayacağımız yapı bulunur.

# BOŞ SÖZLÜK OLUŞTURMAK
sozluk={}
print(sozluk) # {}
print(type(sozluk))  # <class 'dict'>

# SÖZLÜK OLUŞTURMAK
sozluk={"Elma":100,"Armut":50,"Kivi":200,"Çilek":75}

# BİR SÖZLÜĞÜ EKRANA YAZDIRMAK
print(sozluk) # {'Elma': 100, 'Armut': 50, 'Kivi': 200, 'Çilek': 75}

# BİR SÖZLÜKTEKİ ELEMANLARINA ERİŞMEK
sozluk={"Elma":100,"Armut":50,"Kivi":200,"Çilek":75}
print(sozluk["Elma"]) # 100

# SÖZLÜĞE ELEMAN EKLEMEK
sozluk["Portakal"]=350
print(sozluk) # {'Elma': 100, 'Armut': 50, 'Kivi': 200, 'Çilek': 75, 'Portakal': 350}