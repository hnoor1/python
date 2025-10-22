#Kodused harjutamised
#Hanna-Liina Nöör
#Harjutus05


# 5. Kaugushüpe
# kasutaja sisestab 3 kaugushüppe tulemust - 1p
# sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# kood kommenteeritud - 1p

print("Kaugushüppe tulemused!") #pealkiri
print("Sisesestage palun kolm kaugushüppe tulemust\n") #kirjeldus

#kasutaja sisestab kolme hüppe tulemused
kaugus1 = float(input("Sisestage esimese kaugushüppe tulemus meetrites: ")) 
kaugus2 = float(input("Sisestage teise kaugushüppe tulemus meetrites: "))
kaugus3 = float(input("Sisestage kolmanda kaugushüppe tulemus meetrites: "))

kaugused = [kaugus1, kaugus2, kaugus3] #kauguste jada

parim_tulemus = max(kaugused) #maksimaalne parim tulemus
keskmine_tulemus = sum(kaugused) / 3 #kolm hüpet ehk summa jagatud kolmega = keskmine tulemus

print(f"Parim tulemus on {parim_tulemus:.2f} meetrit. Palju õnne parima tulemuse puhul!") #parima tulemuse kalkuleerimine
print(f"Keskmine tulemus on {keskmine_tulemus:.2f} meetrit.")