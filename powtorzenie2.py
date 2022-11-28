def main():
    n = int(input("Podaj wielkosc tablicy: "))
    tab=[0]*n
    i=0
    while i<n:
        tab[i]=int(input("Podaj liczbe: "))
        i+=1
    print(tab)
    srednia=0
    suma=0
    licznik=0
    for a in tab:
        if a>tab[-1]:
            suma+=a
            srednia+=a
            licznik+=1
    print("suma wiekszych od ", tab[-1], "wynosi: ", suma)
    print("srednia wiekszych od ", tab[-1], "wynosi: ", srednia/licznik)
if __name__=='__main__':
    main()