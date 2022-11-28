def main():
    tab=[]
    liczba=int(input("Podaj liczbe: "))
    if liczba!=0:
        tab.append(liczba)
    else:
        pass
    while liczba!=0:
        liczba = int(input("Podaj liczbe: "))
        if liczba==0:
            break
        tab.append(liczba)
    print(tab)
    licznik=0
    i=-1
    j=0
    dlugosc = len(tab)
    flaga=0
    tabkop=[]
    for x in tab:
        while j!=dlugosc:
            if x==tab[j]:
                licznik+=1
            if licznik==3:
                if x not in tabkop:
                    tabkop.append(x)
            j+=1
        licznik=0
        j=0
        if x==tab[i]:
            i-=1
        else:
            flaga=1

    if flaga==1:
        print("Nie jest")
    else:
        print("Jest")
    print(tabkop)
if __name__ == '__main__':
    main()