#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus04

# 4. Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p

print("Emaili kontroll") #pealkiri

email = input("Palun sisestage oma email kujul enimi.pnimi@gmail.com: ") #kasutajale ülesanne


if "@" not in email:
    print("Aadress on sisestatud vigasel kujul. Sisestage @!")

else:
    kasutajanime_osa, server_osa = email.split("@")
    enimi, _ = kasutajanime_osa.split(".")
    gmail, domeen = server_osa.split(".")
    print(f"Tere {enimi}, sinu email on {gmail} serveris ja domeeniks on sul {domeen}")
    
    
