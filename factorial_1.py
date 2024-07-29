def main():
    z = int(input("ENTER: "))
    print(fac(z))

def fac(x):
    if (x == 0 or x == 1):
        return 1
    a = x * fac(x-1)
    return a

main()