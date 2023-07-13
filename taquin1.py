from random import randrint
import math 

n=int(input("donner la dimension du carrée: "))
m=sqrt(n)
tab[m][m]

def initState():
    for i in range(m-1):
        
        for j in range(m-1):
            
            tab.append(random.randint(0, n))
    for i in range(m-1):
        
        for j in range(m-1):
            
            if t[i][j]==0:
                
                t[i][j]='X'
    for i in range(m-1):
        for j in range(m-1):
            print(tab[i][j]+"   ");
        print("\n")

def finaleState():
    x=1
    for i in range(m-1):
        
       for j in range(m-1):       
	  print(x+"   ")
	  x=x+1
	  print("\n")

def leftAction(x,y):
    int aux
    aux=tab[x][y-1]
	tab[x][y-1]=tab[x][y]
	tab[x][y]=aux

def rightAction(x,y):
    int aux
    aux=tab[x][y+1]
    tab[x][y+1]=tab[x][y]
    tab[x][y]=aux


def topAction(x,y):
    int aux
    aux=tab[x-1][y]
	tab[x-1][y]=tab[x][y]
	tab[x][y]=aux

def bottemAction(x,y):
    int aux
    aux=tab[x+1][y]
    tab[x+1][y]=tab[x][y]
	tab[x][y]=aux
	
initState()
finaleState()
leftAction(x,y)
rightAction(x,y)
topAction(x,y)
bottemAction(x,y)
