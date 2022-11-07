import math     #Importazione della libreria math per poter usare il pi greco

def per_quadrato():     #Questa è la funzione per_quadrato() la quale ha il compito di calcolarne il perimetro facendo inserire all'utente il lato
    x=float (input("\nInserisci la lunghezza del lato del quadrato: "))
    y= x*4
    print ("Il perimetro del quadrato e' di : ",y)      #Stampa del valore del perimetro

def cir_cerchio():      #Questa è la funzione cir_cerchio la quale ha lo scopo di calcolarne la circonferenza dato il raggio inserito dall'utente
    x=float (input("\nInserisci la lunghezza del raggio del cerchio: "))
    y= 2*math.pi*x
    print ("La circonferenza del cerchio e' di: ",y)    #Stampa del valore della circonferenza

def per_rettangolo():       #Questa è la funzione per_rettangolo la quale ha il compito di calcolarne il perimetro del rettangolo dato in input dall'utente la base e l'altezza
    x=float (input("\nInserisci la lunghezza della base del rettangolo: "))
    y=float (input("\nInserisci la lunghezza dell'altezza del rettangolo: "))
    z= x*2+y*2
    print ("Il perimetro del rettangolo e' di: ",z)     #Stampa del valore del perimetro

