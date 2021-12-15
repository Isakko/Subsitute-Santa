#Isak Nordström
#Tetek20
#nån tomtegrej
#2021-12-14

"""Tomtevikariat
Ni ska skapa ert första github-projekt!

Gå in på github och skapa ett nytt repository ni kallar för "substitute_santa".
Lägg till en README

Projektet ni ska jobba med denna vecka är följande.
Tomten är sjuk och ni ska avlasta honom. 

Ditt program handlar om önskelistor.
Skapa ett program som har en meny.
Menyn ska ha två lägen.
1. Skapa önskelista.
2. Läs upp önskelista.

Skapa Önskelista
När du skapar en önskelista så behöver du be användaren om några saker.
1. Vad ska filen heta?
2. Vad heter barnet?
3. Vilka saker ska skrivas till på önskelistan? (for- eller while-loop)

Gör sedan så att du skriver ner i filen på följande sätt.
Rad 1: Namn på barnet
Rad 2 till n: Sak

Läs upp önskelista
Fråga användaren om vad filen heter.
Skriv sedan ut namnet på barnet (första raden).
Skriv sedan "ÖNSKELISTA"
Skriv sedan ut rad för rad vad önskelistan innehåller.

Mycket nöje! Vi jobbar med detta under tisdagen och onsdagen."""

#imports
from termcolor import colored
#globala variabler

#funktioner
def skapaönskelista():
    filnamn = input("Skriv vad filen ska heta:\n")
    with open(filnamn+".txt", "a", encoding="utf8") as körda:
        körda.write(input("Vad heter barnet?") + " \n")
        körda.write(colored('Önskelista:'+ '\n', 'blue', attrs=['bold']))
        print("Skriv in vad barnen önskar sig, skriv '#' om du är klar:" " \n")
        while True:
            saker = input("Vad hen önskar sig: ")
            if "#" in saker:
                break
            else:
                körda.write(f"{saker}" + " \n")
    
def läsa_önskelista():
    file = input("Vilke fil vill du läsa upp? (OBS. Du behöver inte skriva .txt efter):" + " \n")

    with open((file)+".txt", "r", encoding="utf8") as kör:
        adv = kör.readlines()
        print("")
        for line in adv:
            print(line,end="") 
#main
def meny():
    
    while True:
        x = input("Vill du skapa önskelista (skriv skapa), eller vill du läsa önskelista (skriv läsa), (skriv '#' för att avsluta)?:\n")
        
        if x.lower() == str("skapa"):
            skapaönskelista()
        
        elif x.lower() == str("läsa"):
            läsa_önskelista()
        
        elif x.lower() == str("#"):            
            print(colored('Programmet avslutas...', 'red', attrs=['bold']))
            break

if __name__ == "__main__":
    
    meny() 
