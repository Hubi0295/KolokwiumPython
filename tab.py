def main():
    n = int(input("Podaj ile liczb: "))
    while n<4:
        n = int(input("Podaj ile liczb: "))
    i=0
    tablica=[]
    while i<n:
        tablica.append(int(input("Podaj liczbe: ")))
        i+=1
    max=[tablica[0],tablica[1],tablica[2]]
    kanmax=[0]*3
    kankanmax=[tablica[0],tablica[1],tablica[2]]
    i=0
    liczniki=0
    index1=0
    while (i+2)!=len(tablica):
        kanmax[0]=tablica[i]
        kanmax[1]=tablica[i+1]
        kanmax[2]=tablica[i+2]
        if len(kanmax)==3:
            if (kanmax[0]+kanmax[1]+kanmax[2])>(max[0]+max[1]+max[2]):
                index1=liczniki
                kankanmax[0],kankanmax[1],kankanmax[2]=max[0],max[1],max[2]
                max[0],max[1],max[2]=kanmax[0],kanmax[1],kanmax[2]
        liczniki+=1
        i+=1
    print(tablica)
    print("drugi ciąg o najwiekszej sumie: ",kankanmax)
    print("Ciąg o największej sumie ", max)
    print("index początku, index końca", index1,",", index1+2)
if __name__=='__main__':
    main()