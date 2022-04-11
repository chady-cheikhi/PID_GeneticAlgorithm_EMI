from math import floor
import random as rn
import matplotlib.pyplot as plt
import numpy as np

def floatToBin(number):
    binaryNum = []
    whole, dec = str(number).split(".")
    whole, dec = int(whole),int(dec)
    whole, dec = bin(whole).lstrip("0b"),bin(dec).lstrip("0b")
    
    listwhole=[]
    listwhole[:0]=whole
    listdec=[]
    listdec[:0]=dec
    return [listwhole,listdec]


def binTofloat(l):
    n=0
    m=0
    i=len(l[0])
    j=len(l[1])
    for k in l[0]:
        n+=k*2**(i-1)
        i-=1
    for k in l[1]:
        m+=k*2**(j-1)
        j-=1
    n+=m/10**(len(str(m)))
    return n


population = np.linspace(2,4,100)


def function(x):
    return (x-3)**2 + 2

def fitness(x):
    return function(x)

def fitnesscolculation(pop):
    fitnesses =[]
    for item in pop:
        fitnesses.append(item)
    return fitnesses 
    


def selection(fitnesses) :
    rouletteRusse = []
    resultat =[]
    for i in range(len(fitnesses)):
        for j in range(floor(fitnesses[1])):
            rouletteRusse.append(fitnesses[i])
    for i in range(50):
        choice=rn.randint(0,len(rouletteRusse)-1)
        resultat.append(rouletteRusse[choice])
        #resultat.sort()
    return resultat

def newGeneration(gen):
    newGen = []
    for i in range(1):
        newGen.append(gen[i])
    for i in range(2,len(gen)-1,2):
        for j in range(3,len(gen),2):
            newChild = crossover(gen[i],gen[j])
            newGen.append(newChild[0])
            newGen.append(newChild[1])
    
    return newGen

def crossover(x,y):
    x,y= floatToBin(x),floatToBin(y)
    print(x,y)
    if rn.randint(1,10)<=12:
        crossOverPoint = rn.randint(1, min(len(x[0]),len(y[0])))
        print(crossOverPoint)
        x[0],y[0] = x[0][:crossOverPoint]+y[0][crossOverPoint:],y[0][:crossOverPoint]+x[0][crossOverPoint:]
    return [x,y]


def mutation(x):
    if rn.randint(1,10)<=7:
        m=rn.randint(0,len(x[1]))
        if ([x][1][m] ==1) :
            globals()[x] = [1][m]=0
        else :
            globals()[x] = [1][m]=1



def GA():
    population = np.linspace(2,4,100)
    a=999
    while a !=0 :
        fitnesscolculation(population)
        selection(population)
        newGeneration()
        population = population[0:2] + [mutation(k) for k in population[2:]]
        print(population)







#GA()

