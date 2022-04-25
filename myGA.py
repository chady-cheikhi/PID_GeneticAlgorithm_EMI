from math import floor,sin,cos
import random as rn
import matplotlib.pyplot as plt
import numpy as np

#define global variables
popsize=20
elite=4
pop = []
newpop=[]
a = 0
b = 3

#utilities
def generatePop():
    #CHECKED
    global pop
    radical = []
    for i in range (0,2) :
        for j in range (0,2) :
            for k in range (0,2) :
                for l in range (0,2) :
                    radical.append(str(i)+str(j)+str(k)+str(l))
    for i in radical :
        for j in radical :
            pop.append([i,j])
    while(len(pop)!=popsize):
        pop.pop(rn.randint(0,len(pop)-1))
    pop.sort(key=fitness,reverse=True)

def binTofloat(l):
    #CHECKED
    n=0
    i=4
    for k in l[0]:
        n+=int(k)*2**(i-1)
        i-=1
    for k in l[1]:
        i-=1
        n+=int(k)*2**(i)     
    return a+n/16*(b-a)

#function to minimise
def function(x):
    return sin(-x**2)

def functionForBin(x):
    return function(binTofloat(x))


#fitness function
def fitness(x):
    return function(binTofloat(x))*10+20

#ellitism
def selectElite():
    #CHECKED
    global newpop
    global pop
    newpop=pop[:elite]

#selection process
def selection() :
    global pop
    rouletteRusse = []
    resultat = []
    for i in pop:
        for j in range(floor(fitness(i))):
            rouletteRusse.append(i)
    for i in range(popsize-elite):
        choice=rn.randint(0,len(rouletteRusse)-1)
        resultat.append(rouletteRusse[choice])
    pop = resultat

#crossover
def crossover():
    #CHECKED
    x=rn.randint(0,popsize-elite-1)
    y=rn.randint(0,popsize-elite-1)
    while (x!=y):
        y=rn.randint(0,popsize-elite-1)
    global newpop
    global pop
    if rn.randint(1,10)<=7:
        crossOverPoint = rn.randint(1,3)
        newpop.append([pop[x][0][:crossOverPoint]+pop[y][0][crossOverPoint:],pop[x][1]])
        newpop.append([pop[y][0][:crossOverPoint]+pop[x][0][crossOverPoint:],pop[y][1]])


#mutation
def mutation():
    #CHECKED
    global newpop
    b=rn.randint(0,3)
    for idx,i in enumerate(newpop) :
        s=""
        if rn.randint(1,10)<=7 and idx>3:
            for j in range(4):
                if j==b :
                    s+= "0" if i[1][b]=="1" else "1"
                else :
                    s+=i[1][j]
            i[1]=s
    
#execution
iteration=1
#First We generate a population
print("Generation population...")
generatePop()
#Start Genetic Algorithm Loop
while (iteration < 50) :
    print("====================================")
    print("==Processing Generation Number "+str(iteration)+":==")
    print("====================================")
    #we apply ellitism
    print("Promoting the elite")
    selectElite()
    print([(binTofloat(i),fitness(i)) for i in newpop])
    #We go through selection
    print("Selecting...")
    selection()
    #we choose two random entites to be crossovered with a 70% probability till newpop is full
    while (len(newpop)!=popsize-elite) :
        crossover()
    print("Crossover is Over")
    #then we mutate with a 70% probability
    print("Mutating...")
    mutation()

    #we make new pop the actual pop
    newpop.sort(key=fitness,reverse=True)
    pop=newpop
    print("Generation Number "+str(iteration)+" is the following:")
    print([(binTofloat(i),fitness(i)) for i in pop])
    newpop=[]
    iteration+=1