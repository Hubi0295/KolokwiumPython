def main():
    tab=[]
    liczba = int(input("Podaj liczbe: "))
    if liczba!=0:
        tab.append(liczba)
    while liczba!=0 and len(tab)<10:
        liczba = int(input("Podaj liczbe: "))
        if liczba==0:
            break
        tab.append(liczba)
    ile = len(tab)
    lewy = 0
    prawy = ile-1
    while lewy<prawy:
        liczba=tab[lewy]
        if liczba%2==0:
            lewy=lewy+1
        else:
            tab[lewy]=tab[prawy]
            tab[prawy]=liczba
            prawy=prawy-1
    print(tab)
if __name__=='__main__':
    main()