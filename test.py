import random as rn

def crossover(x,y):
    x,y= floatToBin(x),floatToBin(y)
    print(x,y)
    if rn.randint(1,10)<=12:
        crossOverPoint = rn.randint(1, min(len(x[0]),len(y[0])))
        print(crossOverPoint)
        x[0],y[0] = x[0][:crossOverPoint]+y[0][crossOverPoint:],y[0][:crossOverPoint]+x[0][crossOverPoint:]
    return [x,y]





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

print (crossover(125.36,36.20))