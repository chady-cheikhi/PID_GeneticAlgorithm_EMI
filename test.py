import random as rn
x=[0,[1,1,1,1,1,1]]
def mutation(x):
    if rn.randint(1,10)<=7:
        m=rn.randint(0,len(x[1])-1)
        if (x[1][m] ==1) :
            globals()[x] = [1][m]=0
        else :
            globals()[x] = [1][m]=1
mutation(x)
print(x)