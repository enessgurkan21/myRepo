print("Hesap Makinesine Hoşgeldiniz :")

giriş="""
(1) Topla
(2) Çıkar
(3) Çarp 
(4) Böl
(5) Karesini hesapla
(6) Kökünü hesapla
"""
print(giriş)

soru=input("Yapmak İstediğiniz İşlemin Numarasını Giriniz :")

if soru=="1":
    sayı1=int(input("Lütfen Toplamak İstediğiniz Birinci Sayıyı Giriniz :"))
    sayı2 = int(input("Lütfen Toplamak İstediğiniz İkinci Sayıyı Giriniz :"))
    sayı3 = int(input("Lütfen Toplamak İstediğiniz Üçüncü Sayıyı Giriniz :"))

    print(sayı1 ,"+", sayı2,"+",sayı3,"=",sayı1+sayı2+sayı3)


elif soru=="2":
    sayı1=int(input("Lütfen Çıkarmak İstediğiniz Birinci Sayıyı Giriniz :"))
    sayı2 = int(input("Lütfen Çıkarmak İstediğiniz İkinci Sayıyı Giriniz :"))
    sayı3 = int(input("Lütfen Çıkarmak İstediğiniz Üçüncü Sayıyı Giriniz :"))

    print(sayı1 ,"-", sayı2,"-",sayı3,"=",sayı1-sayı2-sayı3)

elif soru=="3":
    sayı1=int(input("Lütfen Çarpmak İstediğiniz Birinci Sayıyı Giriniz :"))
    sayı2 = int(input("Lütfen Çarpmak İstediğiniz İkinci Sayıyı Giriniz :"))
    sayı3 = int(input("Lütfen Çarpmak İstediğiniz Üçüncü Sayıyı Giriniz :"))

    print(sayı1 ,"x", sayı2,"x",sayı3,"=",sayı1*sayı2*sayı3)

elif soru=="4":
    sayı1=int(input("Lütfen Bölmek İstediğiniz Birinci Sayıyı Giriniz :"))
    sayı2 = int(input("Lütfen Bölmek İstediğiniz İkinci Sayıyı Giriniz :"))
    sayı3 = int(input("Lütfen Bölmek İstediğiniz Üçüncü Sayıyı Giriniz :"))

    print(sayı1 ,"/", sayı2,"/",sayı3,"=",sayı1/sayı2/sayı3)

elif soru=="5":
    sayı1=int(input("Lütfen Üs Almak İstediğiniz Sayıyı Giriniz :"))
    sayı2 = int(input("Lütfen Kuvveti Giriniz :"))

    print(sayı1 ,"^", sayı2,"=",sayı1**sayı2)

elif soru=="6":
    sayı1=int(input("Lütfen Kök Almak İstediğiniz Sayıyı Giriniz :"))

    print("Belirlediğiniz Sayının Kökü" ,sayı1**0.5,"dir." )

else:
    print("Hatalı Bir Giriş Yaptınız !!!,\nLütfen Tekrar Deneyiniz...",giriş)
    