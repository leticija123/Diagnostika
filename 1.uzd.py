#Letīcija Skudra
correct_password =["python123"]                      #norāda, ka pareizā parole ir "python123"
while True :                                         #Uztaisa ciklu mūžīgu kamēr kaut kas to nebeigs
    password =input("Ievadi paroli:")                #input ievada doto terminālī 
    if password:correct_password                     #Ja parole būs pareiza...
    print("Piekļuve atļauta!")                       #printē doto atbildi
    break                                            #lauž mūžīgo ciklu
else:                                                #Ja neder parole
    print("Piekļuve liegta.Mēģini vēlreiz")          #printē doto atbildi