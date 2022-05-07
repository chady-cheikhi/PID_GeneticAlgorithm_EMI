import control,numpy,scipy,matplotlib.pyplot as plt



Kp,Kd,Ki=0.2,0.1,0.1
Prop = control.TransferFunction(Kp,1)
Der = control.TransferFunction([0,Kd],1)
Int = control.TransferFunction(Ki,[0,1])
PID = control.parallel(Prop,Der,Int)

num = [1]
den = [1,0.2,1]
Proc = control.TransferFunction(num,den)


G=control.feedback(control.series(PID,Proc))
TR = control.step_response(G,[k/10 for k in range(1000)])
print(G.den,G.num)

Out = True
for k in range (1000):
    if (0.95/2 <TR.outputs[k] < 1.05/2 and Out) :
        Ir=k
        Out=False
    elif (0.95/2 > TR.outputs[k] or TR.outputs[k]> 1.05/2):
        Out=True


Tr = Ir/10
Dep = (max(TR.outputs)-0.5)*100
print("Le temps de reponse est de : ",Tr,' s')
print("Le depassement est de : ",Dep,'%')


plt.plot(TR.time,[0.95 for k in TR.time])
plt.plot(TR.time,[1.05 for k in TR.time])
plt.plot(TR.time,TR.outputs)
plt.show()
