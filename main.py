import random

uzunluk = int(input("Şifre Uzunluğu Kaç Karakter Olacak?: "))
bharf = input("Büyük Harf İçermeli Mi?: ")
kharf = input("Küçük Harf İçermeli Mi?: ")
rakam = input("Rakam İçermeli Mi?: ")
sembol = input("Sembol İçermeli Mi?: ")

bharf_liste = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
kharf_liste = list("abcdefghijklmnopqrstuvwxyz")
rakam_liste = list("0123456789")
sembol_liste = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~*")

karakter_havuzu = []

if bharf.lower() == "evet":
    karakter_havuzu.extend(bharf_liste)

if kharf.lower() == "evet":
    karakter_havuzu.extend(kharf_liste)

if rakam.lower() == "evet":
    karakter_havuzu.extend(rakam_liste)

if sembol.lower() == "evet":
    karakter_havuzu.extend(sembol_liste)

if not karakter_havuzu:
    print("Hata: En az bir karakter türü seçmelisiniz!")
else:
    sifre = "".join(random.choices(karakter_havuzu, k=uzunluk))
    print("Oluşturulan Şifre: ",sifre)
