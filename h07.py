#Hanna-Liina Nöör 11.10.2025
#Harjutus07.2

# Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
        # Kuva mõõdetava kuu nimetus 
        # Kuva viimase mõõtmise tulemus
        # Kuva ainult temperatuurid
        # Leia kuu maksimaalne ja minimaalne temperatuur
        # Leia kuu keskmine temperatuur
        # Mitu korda esines -20 kraadi
        # Eemalda element nr 5
        # Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
        # Sorteeri temperatuurid nimekirjas kasvavas järjekorras

mootmised = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"Mõõdetav kuu: {mootmised[0]}")                             # Kuva mõõdetava kuu nimetus
print(f"Viimane mõõtmine: {mootmised[-1]}")                        # Kuva viimase mõõtmise tulemus
print(f"Mõõtmised: {mootmised[1:]}")
mootmised.pop(0)                                                   # Kuva ainult temperatuurid
print(f"min: {min(mootmised)}, max: {max(mootmised)}")             # Leia kuu maksimaalne ja minimaalne temperatuur
print(f"Keskmine temp: {round(sum(mootmised)/len(mootmised),2)}")  # Leia kuu keskmine temperatuur
print(f"-20 kraadi esineb {mootmised.count(-20)} korda")           # Mitu korda esines -20 kraadi
mootmised.pop(4)                                                   # Eemalda element nr 5
mootmised.insert(4,26)                                             # Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
mootmised.sort()                                                   # Sorteeri temperatuurid nimekirjas kasvavas järjekorras
print(mootmised)                                                   # Sorteeri temperatuurid nimekirjas kasvavas järjekorras

#Harjutus07.1

# nimede_loend = ["Alice", "Bob", "Carol", "Dave", "Eve"]
# 
# nimede_loend.append("Jyri")
# nimede_loend.insert(0, "Mari")
# 
# for i in nimede_loend:
#     print(i)

# Loo lugudest loend (koos numbrite ja jutumärkidega)
# 1. ALIKA – "Bridges"
# 2. Anett x Fredi – "Read Between The Lines"
# 3. villemdrillem – "leekiv armastus"
# 4. Clicherik & Mäx – "PAKSUD"
# 5. nublu – "ära ärata"
# 6. NOËP – "Move Your Feet"
# 7. Trad.Attack! – "Bring It On”
# 8. Bedwetters – “It Is What It Is”
# 9. Reket – “Panama paberid”
# 10. Grete Paia – “Võluväel”
        # Kuva kasutajale kõik lood massiivist
        # Küsi millist lugu ta “kuulata” soovib
        # Kuva kasutaja valitud lugu

#tegime notepad++-is nimekirja korda (st muutsime jutumärgid ära, võtsime rea lõpust tühiku ära ning lisasime ',)
        
albumid = ['1. ALIKA – "Bridges"','2. Anett x Fredi – "Read Between The Lines"','3. villemdrillem – "leekiv armastus"','4. Clicherik & Mäx – "PAKSUD"','5. nublu – "ära ärata"','6. NOËP – "Move Your Feet"','7. Trad.Attack! – "Bring It On"','8. Bedwetters – "It Is What It Is"','9. Reket – "Panama paberid"','10. Grete Paia – "Võluväel"']

print(20*"-","KÕIK LOOD",20*"-")
for i in albumid:
    print(i)
    
lugu = int(input("Millist lugu mängid: "))
print(f"Mängin: {albumid[lugu-1]}")
    