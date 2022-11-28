def main():
    n = int(input("Podaj ile elementow chcesz wprowadzic do tablicy:"))
    tab = [0] * n
    i = 0
    while n > 0:
        wartosc = int(input("Podaj liczbe: "))
        tab[i] = wartosc
        i += 1
        n -= 1
    A = int(input("Podaj poczatek przedzialu: "))
    B = int(input("Podaj koniec przedzialu: "))
    licznik=0
    for x in tab:
        if x>=A and x<=B:
            licznik+=1
    print(licznik)

if __name__ =='__main__':
    main()