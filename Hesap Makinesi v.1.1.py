print("""
---Hoşgeldiniz---
====================================
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Üs Alma
6-Kök Alma
====================================
""")

while True:
    sayı=input("Lütfen Yapmak İstediğiniz İşlemi Giriniz   :  (Çıkış İçin 'q' Tuşuna Basınız)   :")

    if sayı=="q":
        print("Sistemden Çıkılıyor...")
        break


    elif sayı=="1":
        sayı1=int(input("Lütfen Birinci Sayıyı Giriniz  :"))
        sayı2=int(input("Lütfen İkinci Sayıyı Giriniz :"))
        sayı3=int(input("Lütfen Üçüncü Sayıyı Giriniz :"))
        print(sayı1,"+",sayı2,"+",sayı3,"=",sayı1+sayı2+sayı3)

    elif sayı=="2":
        sayı1=int(input("Lütfen Birinci Sayıyı Giriniz  :"))
        sayı2=int(input("Lütfen İkinci Sayıyı Giriniz :"))
        print(sayı1,"-",sayı2,"=",sayı1-sayı2)

    elif sayı=="3":
        sayı1=int(input("Lütfen Birinci Sayıyı Giriniz  :"))
        sayı2=int(input("Lütfen İkinci Sayıyı Giriniz :"))
        sayı3=int(input("Lütfen Üçüncü Sayıyı Giriniz :"))

        print(sayı1,"x",sayı2,"x",sayı3,"=",sayı1*sayı2*sayı3)

    elif sayı=="4":
        sayı1=int(input("Lütfen Birinci Sayıyı Giriniz  :"))
        sayı2=int(input("Lütfen İkinci Sayıyı Giriniz :"))

        print(sayı1,"/",sayı2,"=",sayı1/sayı2)

    elif sayı=="5":
        sayı1=int(input("Lütfen Birinci Sayıyı Giriniz  :"))
        sayı2=int(input("Lütfen İkinci Sayıyı Giriniz :"))
        print(sayı1,"^",sayı2,"=",sayı1**sayı2)

    elif sayı=="6":
        sayı1=int(input("Lütfen Sayıyı Giriniz  :"))

        print(sayı1,"√2","=",sayı1**0.5)

    else:
        print("Hatalı İşlem Yaptınız Tekrar Deneyiniz.")