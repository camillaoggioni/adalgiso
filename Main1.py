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