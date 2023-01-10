from math import *
def znajdz_liczby_pierwsze(koniec_przedzialu):
    ostatnia_liczba = koniec_przedzialu
    tab = [True]*(ostatnia_liczba-1)
    aktualna_liczba = 2
    pierwiastek_ostatniej = sqrt(koniec_przedzialu)
    while aktualna_liczba<pierwiastek_ostatniej:
        status = tab[aktualna_liczba-2]
        if status==True:
            wykreslana = aktualna_liczba*2
            while wykreslana<ostatnia_liczba:
                tab[wykreslana-2] = False
                wykreslana+=aktualna_liczba
        aktualna_liczba+=1
    sprawdzana = 2
    bucket=[]
    while sprawdzana<ostatnia_liczba:
        if tab[sprawdzana-2]==True:
            bucket.append(sprawdzana)
        sprawdzana+=1
    return bucket

def main():
    x=int(input("Podaj koniec przedziału: "))
    tablica = znajdz_liczby_pierwsze(x)
    print(tablica)
if __name__ == "__main__":
    main()



















    ostatnia_liczba = int(input("Podaj koniec przedzialu: "))
    # tab = [True]*(ostatnia_liczba-1)
    # akt_liczba = 2
    # pierwiastek_ostatniej = sqrt(ostatnia_liczba)
    # while akt_liczba<pierwiastek_ostatniej:
    #     status=tab[akt_liczba-2]
    #     if status==True:
    #         wykreslana = akt_liczba*2
    #         while wykreslana <=ostatnia_liczba:
    #             tab[wykreslana-2] = False
    #             wykreslana+=akt_liczba
    #     akt_liczba+=1
    # sprawdzana = 2
    # while sprawdzana <=ostatnia_liczba:
    #     if tab[sprawdzana-2] == True:
    #         print("Liczba pierwsza", sprawdzana)
    #     sprawdzana+=1