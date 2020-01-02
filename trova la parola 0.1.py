# trova la parola in python
# By lore
# per miglioramenti --------------
import time
def programm() :
    spazio1 = 1
    while spazio1 != 5:
        print(" ")
        spazio1 = spazio1 + 1
    parola_segreta = input("per iniziare inserisci la parola segreta: ")
    limitemax = input("inserisci il un limite di tentativi massimo: ")
    while limitemax == "":
        print(" ")
        print("non hai scritto niente di buono (in tutti i sensi)")
        limitemax = input("Inserisci un vero numero di tentativi: ")
    while limitemax.isnumeric() == False:
        print(" ")
        print("e secondo te cosa dovrei contare? le lettere?")
        limitemax = input("Inserisci un vero numero di tentativi: ")
    if limitemax == "0" :
        print(" ")
        print("bhe senza tentativi non giochi")
        print("quindi indirettamente hai perso")
        print("addio")
        time.sleep(5)
        quit()
    domanda = input ("inserisci una domanda (facoltativa): ")
    suggerimento = input("scrivi un aiuto(facoltativo) altrimenti premi invio ")
    limite = 1
    spazio = 1
    while suggerimento == parola_segreta:
        print(" ")
        print("cosa cavolo scrivi la parola segreta come suggerimento")
        suggerimento = input("scrivi un vero suggerimento: ")
    while spazio != 50:
        print(" ")
        spazio = spazio + 1
    parola_scritta = ""
    print("passa il pc a qualcuno")
    while parola_segreta != parola_scritta:
        print(domanda)
        parola_scritta = input("inserisci la parola :")
        print(" ")
        print(str(limite) +  " su " + str(limitemax))
        limite = limite + 1
        print(" ")
        if limite * 2 == float(limitemax): #migliorare questa funzione
            print("aiuto:" + suggerimento)
        while limite == float(limitemax) + 1:
            print("sei un fallimento")
            print("la parola era " + parola_segreta)
            input("premi enter per chiudere")
            quit()
    print("congratulationzioni hai vinto")
programm()
si = "si"
no = "no"
continuo = input("vuoi continuare? si o no ?")
print(" ")
while continuo == si:
    programm()
    continuo = input("vuoi continuare? si o no ?")
    print(" ")

else:
    print("arevoir")
    time.sleep(5)
    quit()
