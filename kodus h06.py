#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus06

# 6. Salakeel
# sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# kood kommenteeritud - 1p

print("Salakeele loomine või tõlkimine!") #pealkiri

valiku_tegemine = input("Kas soovite salakeelt luua või salakeelt tõlkida(sisesta '1' salakeele loomiseks või '2' salakeele tõlkimiseks): ") #anname kasutajale valiku, et kumba ta teha soovib

if valiku_tegemine == "1":
    tavaline_sona = input("Salakeele loomiseks sisestage tavaline sõna: ")
    salakeel = ""
    for taht in tavaline_sona:
        salakeel += taht + "o" + taht #iga tähe järele lisatakse o
        
    print(f"Sinu tavaline sõna on salakeeles: {salakeel}") #print on tsüklist eemaldatud, et annaks kohe lõpliku salajase sõna
    
elif valiku_tegemine == '2':
    salakeel_sona = input("Salakeele teisendamiseks sisestage salakeeles sõna: ")
    tavaline_keel = salakeel_sona[::3] #iga kolmas täht jääb alles, o-d võetakse vahelt ära
    print(f"Sinu salakeeles olev sõna on tavakeeles: {tavaline_keel}")
    
    #sõnadega "kutsa" ja "kiivi" see toimis
    #vaalalausuja salakeeles on vovaoaaoalolaoalolaoauousosuoujojaoa; teisendades on vovaoaaoalolaoalolaoauousosuoujojaoa tavakeeles vaalalausuja