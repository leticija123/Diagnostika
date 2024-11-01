#Letīcija Skudra
temperatūra = int(input("ievadi savu temperatūru:"))         #ievada terminālī
if temperatūra>35:                                           #ja temperatūra mazāka par 35 grādiem
    print("Tev ir nopietna ķermeņa atdzišana")               #printē doto atbildi
if 35<= temperatūra<=37:                                     #ja temperatūra no 35 līdz 37
    print("Temperatūra ir normas robežās")                   #printē doto atbildi
elif temperatūra< 38:                                        #Ja neatbilst iepriekšējiem nosacījumiem
    print("Tev ir drudzis")                                  #printē atbildi
