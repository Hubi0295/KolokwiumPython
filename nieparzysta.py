def main():
    liczba = int(input("Podaj liczbe: "))
    flaga=0
    while flaga==0:
        if liczba>0 and liczba%2==0:
            min = liczba
            max = liczba
            flaga=1
        else:
            liczba = int(input("Podaj liczbe: "))
    while liczba%2==0:
        if liczba<0:
            break
        if liczba>max:
            max=liczba
        if liczba<min:
            min=liczba
        liczba = int(input("Podaj liczbe: "))
    print(min,max)
    kopia = max
    potega=1
    while kopia>0:
        potega = potega*min
        kopia-=1
    print(potega)
if __name__ == '__main__':
    main()