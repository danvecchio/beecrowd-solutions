runs = int(input())
for i in range(runs):
    popa,popb,ga,gb = input().split()
    ga = float(ga)
    gb = float(gb)
    popa = int(popa)
    popb = int(popb)
    ga = ga/100 + 1
    gb = gb/100 + 1
    for i in range(1,102):
        popa= int(popa*ga)
        popb = int(popb*gb)
        if(popa>popb):
            break
    if(i<=100):
        print(i,"anos.")
    else:
        print("Mais de 1 seculo.")