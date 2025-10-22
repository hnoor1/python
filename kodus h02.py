#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus02

# 2. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# küsitakse valuuta kogust ja tehakse arvutused - 2p
# kood kommenteeritud - 1p

print("Eurokalkulaator") #pealkiri
print("Kalkulaatori abil saab valuutat kalkuleerida EUR->EEK või EEK->EUR") #kirjeldus

sisend = input("Kas soovid kalkuleerida EUR->EEK või EEK->EUR?(sisesta '1' EUR->EEK või '2' EEK->EUR): ") #anname kasutajale valiku, et kalkulaatorit saaks kasutada

if sisend == '1':                        #eurodest kroonidesse
    EUR = float(input("Sisesta eurode arv, mida soovid kroonideks arvutada: "))
    EEK = EUR * 15.6466
    print(f"{EUR} eurot = {EEK:.2f} krooni")
    
elif sisend == '2':                    #kroonidest eurodesse
    EEK = float(input("Sisesta kroonide arv, mida soovid eurodeks arvutada: "))
    EUR = EEK / 15.6466
    print(f"{EEK} krooni = {EUR:.2f} eurot")

else:              #annab veateate, kui sisestatakse mõni muu number või tekst
    print("Viga! Sisesta valuuta kalkuleerimiseks 1 või 2")