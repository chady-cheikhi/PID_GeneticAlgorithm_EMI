from math import floor
import random as rn
import matplotlib.pyplot as plt
import numpy as np

population = np.linspace(2,4,100)


def function(x):
    return (x-3)**2 + 2

def fitness(x):
    return function(x)

def fitnesscolculation(pop):
    fitnesses =[]
    for item in pop:
        fitnesses.append((item,fitness(item)))
    return fitnesses 
    


def selection(fitnesses) :
    rouletteRusse = []
    for i in range(len(fitnesses)):
        for j in range(floor(fitnesses[i])):
            rouletteRusse.append(pop[i])
    for i in range(50):
        choice=rn.randint(0,len(rouletteRusse)-1)
        besties.append(rouletteRusse[choice])
        besties.sort()
    return besties

def newgeneration(pop, besti):
    pop = []
    for i in range(1):
        pop.append(besti[i])
    for i in range(2,len(besti)-1):
        for j in range(3,len(besti)):
            newChild = crossover(besti[i],besti[j])
            pop.append(newChild[0])
            pop.append(newChild[1])
    return pop

def crossover(x,y):
    if rn.randint(1,10)<=4:
        x,y = floatToBin(x),floatToBin(y)
        crossOverPoint = rn.randint(1, min(len(x),len(y)))    
        newX, newY = x[:crossOverPoint].append(y[crossOverPoint:]),y[:crossOverPoint].append(x[crossOverPoint:])
    else: newX, newY= x,y
    return newX, newY

def mutation(x):
    if rn.randint(1,10)<=7:
        if len(x) < 4:
            if x[0] == '0': x[0]='1'
            else: x[0] = '0'
        else :
            if x[-4] == '0': x[-4]='1'
            else: x[-4] = '0'
    return x


def GA():
    population = np.linspace(2,4,100)
    a=999
    while a !=0 :
        fitnesscolculation(population)
        selection(population)
        newgeneration()
        population = population[0:2] + [mutation(k) for k in population[2:]]
        print(population)









def floatToBin(number):
    binaryNum = []
    whole, dec = str(number).split(".")
    whole, dec = int(whole),int(dec)
    whole, dec = bin(whole).lstrip("0b"),bin(dec).lstrip("0b")
    binaryNum = [k for k in whole]
    binaryNum.append('.')
    for e in dec:
        binaryNum.append(e) 
    listwhole=[]
    listwhole[:0]=whole
    listdec=[]
    listdec[:0]=dec
    return binaryNum, listwhole, listdec

GA()

