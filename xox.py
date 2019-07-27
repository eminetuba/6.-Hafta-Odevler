# XOX Oyunu
#		Kitapta yer alan XOX oyunu iki kisinin karsilikli oynayabilecegi sekilde duzenlenmis. Sizden bu oyunu
#		kullanicinin bilgisayara karsi oynayabilecegi versiyonunu yapmanizi istiyoruz. Ayrica gelistireceginiz
#		algoritma sayesinde bilgisayarin tamamen rastgele hamleler yapmasindan ziyade mantikli hamleler yapmasini
#		saglamanizi istiyoruz. Ornegin bilgisayarin "O" hamlesini yaptigini varsayalim:
#					X O _
#					_ X _
#					_ _ _
#
#		seklinde olusan bir durumda hamle sirasi bilgisayarda ve bilgisayar kaybetmemek icin sag-alt koseye "O"
#		koymalidir.
#
#
#		Farkli bir ihtimal:
#					O X X
#					O _ X
#					_ _ _
#
#		boyle bir durumda da hamle sirasi bilgisayarda ve bilgisayar kazanma hamlesi olarak sol-alt koseye "O" koyarak
#		oyunu bitirmelidir.


liste1 = ["","",""]
liste2 = ["","",""]
liste3 = ["","",""]

kazanan = False

print("\n X-O-X OYUNUNA HOSGELDINIZ!!!")
devam1 = input("\nDevam etmek için Enter'a  basınız.\n")
while kazanan == False:
    secim = input("'X' yada 'O' seçimi yapınız!\n")
    yerSecimi = int(input("Secimizi yapmak için sayilardan birinizi seçiniz ...\n"))

    if (yerSecimi == 7):
            liste1[0] = secim

    elif(yerSecimi == 8):
            liste1[1] = secim

    elif(yerSecimi == 9):
            liste1[2] = secim

    elif(yerSecimi == 4):
            liste2[0] = secim

    elif(yerSecimi == 5):
            liste2[1] = secim

    elif(yerSecimi == 6):
            liste2[2] = secim

    elif(yerSecimi == 1):
            liste3[0] = secim

    elif(yerSecimi == 2):
            liste3[1] = secim

    elif(yerSecimi == 3):
            liste3[2] = secim

    else:
        print("Kordinatlamalar için 0 haricindeki rakamları kullanınız!")

    print(liste1)
    print(liste2)
    print(liste3)

    if (liste1[0] == liste1[1] == liste1[2]):

        if(liste1 == ["","",""]):
            kazanan = False
        elif(liste2 == ["","",""]):
            kazanan = False
        elif(liste3 == ["","",""]):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste2[0] == liste2[1] == liste2[2]):

        if (liste1 == ["", "", ""]):
            kazanan = False
        elif (liste2 == ["", "", ""]):
            kazanan = False
        elif (liste3 == ["", "", ""]):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste3[0] == liste3[1] == liste3[2]):

        if (liste1 == ["", "", ""]):
            kazanan = False
        elif (liste2 == ["", "", ""]):
            kazanan = False
        elif (liste3 == ["", "", ""]):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste1[0] == liste2[0] == liste3[0] != ""):

        if (liste1[1] == liste2[1] == liste3[1] == "" ):
            kazanan = False
        elif (liste1[2] == liste2[2] == liste3[2] == ""):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste1[1] == liste2[1] == liste3[1] != ""):

        if (liste1[0] == liste2[0] == liste3[0] == "" ):
            kazanan = False
        elif (liste1[2] == liste2[2] == liste3[2] == ""):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste1[2] == liste2[2] == liste3[2] != ""):

        if (liste1[0] == liste2[0] == liste3[0] == "" ):
            kazanan = False
        elif (liste1[1] == liste2[1] == liste3[1] == ""):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste1[0] == liste2[1] == liste3[2] != ""):
        if(liste1[0] == "" and liste2[1] == "" and liste3[2] == ""):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    elif (liste1[2] == liste2[1] == liste3[0] != ""):
        if(liste1[2] == "" and liste2[1] == "" and liste3[0]):
            kazanan = False
        else:
            kazanan = True
            print("Tebrikler Kazandınız!")

    else:
        if(liste1[0] != "" and liste1[1] != "" and liste1[2] != ""):
            if (liste2[0] != "" and liste2[1] != "" and liste2[2] != ""):
                if (liste3[0] != "" and liste3[1] != "" and liste3[2] != ""):
                    print ("Berabere!")
                    kazanan = True
            else:
                kazanan = False
        else:
            kazanan = False
    devam2 = input("Kaldığınız yerden devam etmek için Enter'a basınız!\n ")
