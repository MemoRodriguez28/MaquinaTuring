from mt import *


#Inversión de bits (igual que en tabla)
funcionTransicion = {("q0","0"):("1", "R", "q0"),
                     ("q0","1"):("0", "R", "q1"),
                     ("q1","0"):("1", "R", "q1"),
                     ("q1","1"):("0", "R", "qfinal")}
qfinales = {"qfinal"}

mt = MT("0101 ", q0="q0", qfinales=qfinales, funcionTransicion=funcionTransicion)

print("Input en Cinta: \n" + mt.getCinta())

while not mt.final(): 
    mt.step()

print("Resultado de la ejecución de la MT:")
print(mt.getCinta())