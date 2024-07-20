a = int(input("a sayısını giriniz : "))
b = int(input("b sayısını giriniz : "))
c = int(input("c sayısını giriniz : "))

if b > a:
    print("b a dan büyüktür")
elif b < a:
    print("a b den büyüktür")
elif c > a and c > b:
    print("c hepsinden büyüktür")
else:
    print("a ve b eşittir")
