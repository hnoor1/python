import random

#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus03

# 3. Täringud
# kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# kasutaja võistleb kahe täringuga arvuti vastu - 1p
# kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# kood kommenteeritud - 1p

print("Täringumäng!") #pealkiri
print("Mängus võistleb kasutaja kahe täringuga arvuti vastu - suurim punktisumma võidab\n") #kirjeldus

pakkumine = float(input("Mängu alustamiseks sisestage pakkumine eurodes: ")) #pakkumise kirjeldus

kasutaja_taring1 = random.randint(1,6) #kasutaja esimene täring
kasutaja_taring2 = random.randint(1,6) #kasutaja teine täring
arvuti_taring1 = random.randint(1,6) #arvuti esimene täring
arvuti_taring2 = random.randint(1,6) #arvuti teine täring

kasutaja_summa = kasutaja_taring1 + kasutaja_taring2 #kasutaja kahe täringu summa
arvuti_summa = arvuti_taring1 + arvuti_taring2 #arvuti kahe täringu summa

print("Veeretama!\n") #vahekäsklus

print(f"Kasutaja veeretas {kasutaja_taring1} ja {kasutaja_taring2}, kokku {kasutaja_summa}") #võimalik tulemus
print(f"Arvuti veeretas {arvuti_taring1} ja {arvuti_taring2}, kokku {arvuti_summa}") #võimalik tulemus

if kasutaja_summa > arvuti_summa: #kui kasutaja võidab
    print(f"Palju õnne, kasutaja võitis endale {pakkumine} eurot")
elif kasutaja_summa < arvuti_summa: #kui kasutaja kaotab
    print(f"Kahjuks kasutaja kaotas. Arvuti võitis {pakkumine} eurot")



