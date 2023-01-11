import datetime
import time
import math
def funkcja(ciag):
    if ciag[-1].isdigit():
        tab=[]
        for x in ciag:
            tab.append(x)
        newtab=[]
        tab.reverse()
        for x in tab:
            if x.isdigit():
                newtab.append(int(x))
            else:
                break
        licz=1
        liczba=0
        i=0
        while i<len(newtab):
            liczba+=newtab[i]*licz
            licz*=10
            i+=1
        liczba+=1
        stri=""
        flaga=0
        i=0
        while i<len(tab):
            if not(tab[i].isdigit()) and flaga==0:
                flaga=1
            if flaga==1:
                stri+=tab[i]
            i+=1
        newnew=[]
        for x in stri:
            newnew.append(x)
        newnew.reverse()
        newst=""
        for x in newnew:
            newst+=x
        newst+=str(liczba)
        return newst
    else:
        ciag+=str(1)
        return ciag
def zad2(ciag):
    i=0
    stri=""
    while i<len(ciag):
        if ord(ciag[i])>=65 and ord(ciag[i])<=90:
            newasc=ord(ciag[i])+13
            if newasc>90:
                newasc=65+(newasc-90)
            stri+= chr(newasc)
            i += 1
            continue
        if ord(ciag[i])>=97 and ord(ciag[i])<=122:
            newasc=ord(ciag[i])+13
            if newasc>122:
                newasc=97+(newasc-122)
            stri+= chr(newasc)
            i += 1
            continue
        stri+=ciag[i]
        i+=1
    return stri
def zad3(liczba, druga):
    a= time.time_ns()
    try:
        x = liczba/druga
    except ZeroDivisionError:
        print("Zero division")
    b= time.time_ns()
    print(b-a)
def main():
    ciag="0fz8oAZ999a"
    nowy_ciag = funkcja(ciag)
    print(nowy_ciag)
    rot13 = zad2(ciag)
    print(rot13)
    zad3(10,2)
if __name__ == "__main__":
    main()
