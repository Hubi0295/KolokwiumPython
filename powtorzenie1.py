def main():
    liczba=1
    flaga=0
    srednia=0
    licznik=0
    while liczba>=0:
        liczba = int(input("Podaj liczbe: "))
        if liczba<0:
            break
        if liczba==0 and flaga==0:
            flaga=1
            continue
        if liczba!=0 and flaga==1:
            srednia+=liczba
            licznik+=1
        if liczba==0 and flaga==1:
            flaga=0
    print("Srednia liczb wynosi: ", srednia/licznik)


if __name__=='__main__':
    main()