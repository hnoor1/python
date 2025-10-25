# #Iseseisev töö

# # Iseseisev töö 1
# # 1.1. Tervitus
# # Koostada programm, mis väljastaks ekraanile teksti Tere, maailm! täpselt sellisel kujul - koma ja hüüumärgiga.

# print("Tere, maailm!")
           
# # 1.2. Aasta liblikas
# # Koostada programm, mille
# # 1. real luuakse muutuja nimega aasta ning antakse sellele väärtuseks 2020 (arvuna);
# # 2. real luuakse muutuja nimega liblikas ning antakse sellele väärtuseks "teelehe-mosaiikliblikas" (sõnana);
# # 3. real luuakse muutuja nimega lause_keskosa ning antakse sellele väärtuseks ". aasta liblikas on " (sõnena);
# # 4. real luuakse muutuja nimega lause, mille väärtuse saamiseks ühendatakse üheks sõnaks muutujad aasta, lause_keskosa ja liblikas (vajadusel tuleb kasutada funktsiooni, 
# # mis teisendab arvu sõneks);
# # 5. real väljastatakse muutuja lause väärtus ekraanile.

# # muutuja 2020
# # muutuja teelehe-mosaiikliblikas
# # muutuja 

# aasta = 2020
# lause_keskosa = ".aasta liblikas on"
# liblikas = "teelehe-mosaiikliblikas."

# print(aasta,lause_keskosa,liblikas)



# # 1.3. Pilved
# # Pilvede alumise pinna (aluse) kõrguse järgi liigitatakse pilvi ülemise, keskmise ja alumise kihi pilvedeks. 
# # Ülemiste pilvede alus on kõrgemal kui 6 km, keskmistel pilvedel on 2-6 km kõrgusel, alumistel pilvedel on madalamal kui 2 km. Koostada programm, mis
# # küsib kasutajalt pilvede aluse kõrgust (kilomeetrites),
# # väljastab ekraanile Need on ülemised pilved, kui sisestatu on üle 6,0 km,
# # väljastab Need ei ole ülemised pilved, kui kõrgus on 6,0 km või alla selle.
# # Kasutaja peab saama sisestada pilvede kõrgust nii täisarvuna kui ka ujukomaarvuna, nt 7.5.


# # pilvede aluse kõrgus nr 7.5
# # kui sisestatud on üle 6,0 km
# # kui kõrgus on 6,0 km või alla selle
# #alumistel pilvedel on madalamal kui 2 km


# korgus = float(input("Mis on pilvede aluse kõgus?: "))
# if korgus > 6:
#     print("Need on ülemised pilved.")
# elif korgus >= 2 and korgus <= 6:
#     print("Need on keskmised pilved. ")
# else:
#     print("Need ei ole ülemised pilved!")


# 1.4. Bussid
# Meil on vaja transportida teatud arv inimesi mingi arvu identsete bussidega. 
# Eeldame, et reisijaid on vähemalt üks. Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi kohtade arvu (just sellises järjekorras) ning 
# väljastab ekraanile, mitu bussi on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid on täis).
# Võib-olla on abi nendest tehetest
# // täisarvuline jagamine, 36 // 10 → 3
# % jäägi leidmine 36 % 10 → 6
# Testige oma programmi muuhulgas järgmiste algandmetega:
# inimeste arv: 60, kohtade arv: 40;
# inimeste arv: 80, kohtade arv: 40;
# inimeste arv: 20, kohtade arv: 40;
# inimeste arv: 40, kohtade arv: 40.
# Püüdke ka mõista, miks just sellised testandmed valiti.

inimesed = int(input("Kui palju inimesi transporditakse: "))
kohad = int(input("Sisestage kohtade arv: "))
# busse vaja = 2
# viimases bussis inimesi = 40

bussid = inimesed // kohad
if inimesed // kohad != 0:
    bussid += 1

viimases_bussis = inimesed // kohad
if viimases_bussis != 0: 
    viimases_bussis = kohad
print("Busse on vaja kokku", bussid)
print("Viimases bussis inimesi on: ", viimases_bussis)


