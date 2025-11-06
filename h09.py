#Harjutus09
# import random

# for i in range(1,21): #Genereeri ja kuva arvud arvud 1-20
#     if i%15 == 0:                                         #Arvud, mis jagunevad 3, lisa tekst TIK (näiteks 3 TIK)
#         print(i, "TIKTAK")
#     elif i%3 == 0:
#         print(i,"TIK")
#     elif i%5 == 0:
#         print(i,"TAK")
#     else:
#         print(i)


#Harjtus 09.13
#Mitmemõõtmelise massiivi kasutamine for-tsükliga
#Tutvu elektriautode nimekirjaga, mis sisaldab 10 elektriauto mudelit, nende läbisõidu ulatust ja hinda. Mõista, kuidas andmed on struktureeritud.

# Kuva andmed ridade kaupa, vorminda tulpadena
# Leia keskmine läbisõidu ulatus ja hind
# Kuva auto nimed, mille läbisõidu ulatus on suurem kui 300 km
# Analüüsi andmeid, et tuvastada, kas kõrgema hinnaga autodel on tõepoolest pikem läbisõidu ulatus

ev_data = [
['vehicle', 'range', 'price'],
['Tesla Model Y Long Range', '330', '58990'],
['Volkswagen ID.4 Pro', '260', '39995'],
['Ford Mustang Mach-E', '300', '42995'],
['Audi e-tron GT', '238', '102700'],
['Nissan Leaf', '149', '27400'],
['BMW iX xDrive50', '324', '83995'],
['Polestar 2', '265', '45500'],
['Kia EV6 Long Range', '310', '47795'],
['Mercedes-Benz EQS 450+', '350', '102310'],
['Hyundai Kona Electric', '258', '37400']
]

#print(ev_data[0][-1])

# Kuva andmed ridade kaupa, vorminda tulpadena
# for i in (ev_data):
#     print(f"{i[0]:30} {i[1]:10} {i[2]:10}") #vormindan tulpadena :30 on laius

# Leia keskmine läbisõidu ulatus ja hind
lugeja = 0
r_kokku = 0
p_kokku = 0

for i in (ev_data):
    print(f"{i[0]:30} {i[1]:10} {i[2]:10}") #vormindan tulpadena :30 on laius
    if (i[1]).isnumeric()==True:  #kui tegemist on numbriga, siis annab selle keskmise sõiduulatuse
        r_kokku+=int(i[1])
        p_kokku+=int(i[2])
        lugeja+=1 #+=1 tähendab lühemalt nt lugeja + 1
        print("Autod, mille läbisõidu ulatus on suurem kui 300 km")
        if int(i[1])>=300:
            print(i[0])

print(f"Sõidu ulatus keskmine: {r_kokku/lugeja}") 
print(f"Hind keskmine: {p_kokku/lugeja}") 

print("Autod, mille läbisõidu ulatus on suurem kui 300 km")
for i in (ev_data):
    if (i[1]).isnumeric()==True:
        if int(i[1]) >= 300:
            print(i[0])

parim_hinnasuhe = 1000000000000000
parim_auto = ""

for i in (ev_data):
    if (i[1]).isnumeric()==True:
        km_tasu = int(i[2]) / int(i[1])
        if km_tasu<parim_hinnasuhe:
            parim_hinnasuhe = km_tasu
            parim_auto = i[0]
        

print(f"Parim elektriauto: {parim_auto}")