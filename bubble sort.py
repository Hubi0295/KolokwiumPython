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
def binary(tab, x):
    i=0
    while i<len(tab)-1:
        n=len(tab)
        if x>tab[n//2]:
            tab = tab[n//2:n]
        elif x<tab[n//2]:
            tab = tab[0:n//2]
        else:
            return True
    return False

def main():
    tab = [4,412,2,1,5,120,21,410,-123]
    newtab = bubblesort(tab)
    print(newtab, tab)
    y = binary(newtab, 21)
    print(y)
if __name__=="__main__":
    main()