from Perimetro import *     #Importanzione del modulo chamato Perimetro

i=5     #Inizializzazione a 5 della varibile i usata per il ciclo while
while(i>0):     #Ciclo while usato per eseguire più volte le operazioni con un massimo di 5
    print("\nInserisci uno dei seguenti numeri per effettuare il calcolo, ricordati che puoi usarmi altre ",i, " volte prima di dovermi avviare di nuovo\n\n1) Perimetro del Quadrato\n\n2) Circonferenza del Cerchio\n\n3)Perimetro del rettangolo\n\n4) Esci dal programma\n\n")
    x= input("Risposta: ")  #Inserimento dell'input dato dall'utente
    
    if(x == '1'):
        per_quadrato()      #Se l'utente inserisce 1, il programma andrà ad eseguire la funzione per_quadrato() per calcolare il perimetro di esso inserendo un lato
        i=i-1   #Decremento della variabile i
    elif (x=='2'):      
        cir_cerchio() #Se l'utente inserisce 2, il programma andrà ad eseguire la funzione cer_cerchio() per calcolare la circonferenza di un cerchio dato il suo raggio
        i=i-1
    elif (x=='3'):
        per_rettangolo()    ##Se l'utente inserisce 3, il programma andrà ad eseguire la funzione per_rettangolo() per calcolare il perimetro del rettangolo dati in input la base e l'altezza
        i=i-1
    elif(x=='4'):
        print ("Alla prossima")     #Aggiunta la possibilità di uscire direttamente dal programma grazie alla funzione quit()
        quit()
    else:
        print ("Valore non valido")     #Se l'utente non inserirà nessuna delle precendeti scelte ritornerà al menù iniziale decrementando ugualmente la variabile i
        i=i-1
