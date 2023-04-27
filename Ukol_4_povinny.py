#Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
#Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za #každých započatých 180 znaků

import math

TEL_CISLO=input("Zadej sve cislo: ")
def over_cislo(TEL_CISLO):
    if len(TEL_CISLO)==9:
        overeni=True
    elif len(TEL_CISLO)==13:
        if TEL_CISLO[:4]=="+420":
            overeni=True
        else:
            overeni=False
    else:
        overeni=False
    return overeni

over_cislo(TEL_CISLO)
if over_cislo(TEL_CISLO)==True:
    zprava=input("Zadej zpravu: ")
else:
    print(f"Tve telefonni cislo je chybne.")

def vypocet_ceny(zprava):
    delka_zpravy=len(zprava)
    kolik_180=math.ceil(len(zprava)/180)
    celkova_cena=kolik_180*3
    return (celkova_cena)

print(f"Tva cena k zaplacení je {vypocet_ceny(zprava)} Kč")

