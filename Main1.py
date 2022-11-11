#Creazione variabili e stampa delle stesse
x=18
y="Camilla"
print(x)
print(y)
#Riassegnazione del tipo della variabile x
x=76        #x è una variabile int
x="Rudolf"  #x ora è una variabile str
print(x)
#Per cambiare una variabile di un determinato tipo bisogna dischiararlo tramite il casting
x=str(7)    #7 è una stringa '7'
y=int(7)    #7 è un intero 7
z=float(7)  #7 è un decimale 7.0
#Scoprire il tipo di variabile
x=54
y="Gianpiero"
print(type(x))
print(type(y))
#Le variabili possono essere dichiarate sia con una virgoletta(') che con due("")
x='Bronag'
x="Bronag"   #sono la stessa cosa
#I nomi delle variabili vengono distinti tra minuscole  e maiuscole
a="Roberto"
A=4          #le variabili non si sovrascrivono
#Il nome delle variabili può iniziare con una lettera o un carattere di sottolineatura, non può iniziare con un numero, può contenere solo caratteri alfanumerici e trattini bassi, distingue maiuscol e minuscole
myvar = "Pingu"
my_var = "Pingu"
_my_var = " Pingu"
myVar = "Pingu"
MYVAR = "Pingu"
myvar2 = "Pingu"
#Si può assegnare più valori a diverse variabili nella stessa linea
x, y, z=  "Piero","Ugo","Dario"
print(x)
print(y)
print(z)
#Si può assegnare lo stesso valore a diverse variabili
x=y=z= "Giordy"
print(x)
print(y)
print(z)
#Avendo dei valori in una lista si possono estrarre da essa e assegnargli delle varibili
nomi_meravigliosi=["Asdrubale","Giangiovanni","Gennaro"]
x, y, z = nomi_meravigliosi
print(x)
print(y)
print(z)
#La funzione print serve per stampare le variabili
x = "Ho mal di pancia"
print(x)
#Si possono stampare diverse variabili separate da una virgola
x = "Io"
y = "ho"
z = "sonno"
print(x, y, z)
#Si può anche utilizzare il simbolo + per stampare diverse variabili
x = "Io "
y = "ho "
z = "sonno"
print(x+y+z)
#Con le variabili int + funziona come un operatore matematico
x = 4
y = 5
print(x+y)
#Se provi a sommare una stringa a una variabile int il programma da errore
x = 6
y = "Piero"
print(x+y)
#Il modo migliore per stampare una stringa e una vbariabile int insieme è dividerli con una virgola
x = 6
y = "Piero"
print(x, y)
#Si crea una variabile fuori dalla funzione e la usi all'interno della stessa
x = "meraviglioso"
def myfunc():
  print("Io sono" + x)
myfunc()
#Crea variabili all'interno della funzione con lo stesso nome della variabile global
x = "bellissimo"
def myfunc():
  x = "mirabolante"
  print("Python è " + x)
myfunc()
print("Python è " + x)
#Global permette di stampare la variabile definita nella funzione anche all'esterno di essa
def myfunc():
  global x
  x = "stratosferico"
myfunc()
print("Python è " + x)
#Per cambiare il valore di una variabile global all'interno della funzione bisogna definirla col termine global
x = "super"
def myfunc():
  global x
  x = "iper"
myfunc()
print("Python è " + x)
#Si crea una lista
thislist = ["apple", "banana", "cherry"]
print(thislist)
#Si può ripetere uno stesso valore
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#Si può stampare un valore indicando il numero che ha nella lista
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#Si usa il numero negativo per partire dalla fine della lista
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Si può definire un intervallo di variabili da stampare
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Si stampano le variabilio che precedonbo quella in posizione 4 esclusa
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#Si stampano le variabili che seguono quella in posizione 2 esclusa
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#Definisce un intervallo partendo dalla fine
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Verifica se una variabile è presente nella lista e stampa una stringa che verifica la presenza
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Cambia il valore di una variabile nella posizione indicata
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Cambia il valore di più variabili nelle posizioni indicate
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#Si sostituisce a una variabile due variabili
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#Si cambiano due variabili in una sola variabile
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#Permette di aggiungere altre variabili nella posizione scelta senza sostituirne
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#Permette di aggiungere unba variabile alla lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Si possono unire due liste
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Si può unire a una lista anche un altro oggetto
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#Permette di rimuovere una variabile dalla lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Rimuove il secondo elemento della lista
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#Rimuove l'ultimo elemento
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#Rimuove il primo elemento della lista
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#Riumove l'intera lista
thislist = ["apple", "banana", "cherry"]
del thislist
#Rimuove tutti gli elementi dalla lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#Stampa gli elementi uno per uno
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#Stampa facendo riferimento al numero di indice degli elementi
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
