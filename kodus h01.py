#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus01

# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

print("Paarisarvu või paaritu arvu kontroll") #pealkiri
sisend = input("Sisestage number: ")          #ülesanne, mida kasutaja peab tegema


if sisend == "":                              #kui jätab välja tühjaks, saab veateate
    print("Istu 2, sisestama peab arvu")

elif sisend == "0":                           #kui sisestab nulli, saab veateate
    print("Istu 2, ära sisesta nulli")

else:                                         #kui sisestab korrektse arvu, mis pole null, saab vastuseks kas selle, et arv on paaris või paaritu
    num= int(sisend)

    if (num % 2) == 0:
        print("{0} on paarisarv".format(num))
    else:
        print("{0} on paaritu arv".format(num))

    
