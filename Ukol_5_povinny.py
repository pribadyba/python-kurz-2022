#Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#Vytvoř seznam průměrných teplot pro každý den.
prumer=[sum(teplota)/len(teplota) for teplota in teploty]
print(prumer)

#Vytvoř seznam ranních teplot.
rano=[teplota[0] for teplota in teploty]
print(rano)

#Vytvoř seznam nočních teplot.
vecer=[teplota[2] for teplota in teploty]
print(vecer)

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledne_noc=[[teplota[1],teplota[3]] for teplota in teploty]
print(poledne_noc)
