#Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.Soubor si ulož a načti do slovníku.
#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
#Výsledný slovník ulož jako JSON do souboru prospech.json

import json
with open('body.json', encoding='utf-8') as file:
    hodnoceni=json.load(file)

    for key_jmeno, value_znamka in hodnoceni.items():
        if value_znamka >= 60:
            print(key_jmeno, "Pass")
        else: print(key_jmeno, "Fail")

import json
with open ('prospech.json', mode="w", encoding='utf-8') as file_2:
    json.dump(hodnoceni,file_2,ensure_ascii=False)