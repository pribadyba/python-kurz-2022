#Zadání: Vyvíjíš software pro obchod s elektronickými součástkami. Firma eviduje informace o počtu součástek na skladě ve slovníku. Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. 

#Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.

#Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.

#Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

Kod = input("Zadej kod soucastky: ")
if Kod in sklad:
    Mnozstvi = int(input("Zadej mnozstvi: "))
    if Mnozstvi > sklad[Kod]:
        print(f"Lze prodat pouze {sklad[Kod]} kusu")
        sklad.pop("KC147")
        print(sklad)
    else:
        print(f"Soucastka {Kod} je na skladě ve vybranem mnozstvi {Mnozstvi} ks.")
        sklad[Kod]-=Mnozstvi
        print(sklad)
else:
    print(f" Soucastka {Kod} bohuzel neni na skladě")