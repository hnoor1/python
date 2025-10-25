# #Harjutus 08

# #Kuva Mari telefoninumber +
# #Lisa sõnastikku oma nimi ja telefoninumber +
# #Kustuta Kristi number +
# #Muuda Eva telefoninumbri väärtuseks 55555555 + 
# #Kuva kõik numbrid + 
# #Lisa võimalus kasutajal otsida nime järgi telefoninumbreid. Lisa teade, kui otsitavat nime ei leitud.


# telefonid={
# 'Mari': '5957503',
# 'Toomas': '5719979',
# 'Kertu': '5201750',
# 'Siim': '5580027',
# 'Piret': '5960799',
# 'Jaan': '5160415',
# 'Lea': '5760164',
# 'Mart': '5337951',
# 'Anni': '5004818',
# 'Tõnu': '5721873',
# 'Kai': '5811884',
# 'Rasmus': '5859489',
# 'Eva': '5039393',
# 'Oskar': '5635812',
# 'Liina': '5696114',
# 'Peeter': '5560756',
# 'Sandra': '5257415',
# 'Heiki': '5207248',
# 'Kristi': '5703338',
# 'Urmas': '5400549'
# }

# print(telefonid['Mari']) #näitab Mari numbrit

# telefonid["Liina"] = "56716397"
# print(telefonid['Liina']) #näitab minu numbrit

# eemalda = telefonid.pop("Kristi") #popitud_vaartus = sonastik.pop('vanus', 'Ei ole olemas')
# print(telefonid)

# telefonid["Eva"] = "55555555555"
# print(telefonid["Eva"])

# for i in telefonid:
#     print(telefonid[i])


# nimi = input("Sisesta nimi: "). capitalize()
# #try:
# #    print(telefonid[nimi])
# #except:
# #    print("Sellist nime pole")


#Harjutus08.2

# Programm peaks kasutajalt küsima toote nime, mida ta soovib osta +
# Seejärel küsitakse kasutajalt soovitud kogust + 
# Kontrolli, kas otsitav toode on sõnastikus olemas: + 
# Kui toodet ei ole, kuvatakse sõnum, et toodet ei leitud + 
# Kontrolli, kas soovitud kogus on saadaval + 
# Kui kogus on saadaval, arvutatakse ja kuvatakse ostu kogusumma + 
# Kui kogus ei ole piisav, teavitatakse kasutajat sellest + 
# Kui ost on võimalik, vähendatakse toote kogust laoseisus vastavalt ostetud kogusele
# Lõpetuseks kuvatakse uuendatud laoseisu info.

tooted = {
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}

#print(tooted["piim"]["kogus"])

try:
    toode = input("Lisa toode: ").lower() #Programm küsib kasutajalt toodet
    kogus = int(input("Vali kogus: ")) #Programm küsib kogust

    if toode in tooted.keys(): #keys on see sõnastiku värk
        if kogus <= tooted[toode]["kogus"] and kogus > 0: 
            print("Kogus olemas")
            summa = kogus * tooted[toode]["hind"] #Kui kogus on saadaval, arvutatakse ja kuvatakse ostu kogusumma
            print(f"{round(summa,2)}eur") #võib panna summa ümarduse roundi asemel: 0.2f
            tooted [toode]["kogus"] -= kogus 
            print(tooted)
       
       
        else:
            print("Pole piisavalt!") #kui kogust pole, siis annab teate

    else:
        print(f"{toode} Ei leitud") #kui toodet ei eksisteeri, annab sellest teada
   

except Exception as e:
    print("Ole nüüd normaalne!")

