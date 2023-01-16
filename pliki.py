def bubblesort(tab):
    n = len(tab)-1
    i=0
    while n!=0:
        i = 0
        while i<n:
            if tab[i]>tab[i+1]:
                k=i
                while k<n:
                    tab[k], tab[k+1]=tab[k+1],tab[k]
                    k+=1
            i+=1
        n-=1
    return tab
def main():
    separator = ','
    tab=[]
    plik_we = open("wejscie.txt", "r")
    rozbita_tablica = plik_we.read().split(separator)
    for wartosc in rozbita_tablica:
        tab.append(int(wartosc))
    plik_we.close()
    print(tab)
    bubblesort(tab)
    i=0
    plik_wy = open("wynik.txt", "w")
    for wartosc in tab:
        if i==len(tab)-1:
            separator=''
        plik_wy.write(str(wartosc)+separator)
        i+=1
    plik_wy.close()
if __name__=="__main__":
    main()