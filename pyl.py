import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *

prolog = Prolog()
prolog.consult("C:/sistema_solar.pl")

for luna in prolog.query("satelites(Planeta,Luna)"):
    if luna["Luna"] == []:
        print "No hay luna(s) en ", luna["Planeta"]
    else:
        for una in luna["Luna"]:
            print una , "es luna de " , luna["Planeta"]