from math import sqrt
def pierwiastki(a,b,c):
    delta = b * b - (4 * a * c)
    if delta>0:
        x1 = (-b-sqrt(delta))/2
        x2 = (-b+sqrt(delta))/2
        return x1,x2
    elif delta==0:
        x0 = -b/2
        return x0
    else:
        print("Delta mniejsza od zera")
        return 0
def main():
    print("Wzor ax2+bx+c")
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    c = int(input("Podaj c: "))
    pier = pierwiastki(a,b,c)
    print("Pierwiastki wynosza: ", pier)
if __name__ == '__main__':
    main()