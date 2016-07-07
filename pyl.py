import os
os.chdir("C:\\Program Files (x86)\\swipl\\bin")
from pyswip import *
from Tkinter import *

master = Tk()
master.minsize(500,500)
prolog = Prolog()
prolog.consult("C:/sistema_solar.pl")

w = Label(master, text="3er Parcial")
w.pack()

def select(event):
    lunasFrames = Tk()
    contador = 0
    lunaList = Listbox(lunasFrames)
    e = event.widget
    index = int(e.curselection()[0])
    valor = e.get(index)
    for luna in prolog.query("satelites(Planeta,Luna)"):
        if valor == luna["Planeta"]:
            if luna["Luna"] == []:
                lunaList.insert(contador,"No tiene lunas")
            else:
                for moon in luna["Luna"]:
                    lunaList.insert(contador,moon)
                    contador += 1
    lunaList.pack()

    print 'You selected item %d: "%s"' % (index, valor)

def lunasPlanetas():
    child1 = Tk()
    Lb1 = Listbox(child1, selectmode=SINGLE)

    i=1
    for luna in prolog.query("satelites(Planeta,Luna)"):
        Lb1.insert(i, luna["Planeta"])
        i += 1

        """if luna["Luna"] == []:
            print "No hay luna(s) en ", luna["Planeta"]
            Lb1.insert(i, luna["Planeta"])
            i+= 1
        else:
            for una in luna["Luna"]:
                print una, "es luna de ", luna["Planeta"]
                Lb1.insert(i, luna["Planeta"])
                i += 1"""

    Lb1.bind('<<ListboxSelect>>',select)

    Lb1.pack()

b1 = Button(master,text="Lunas de Planetas",command = lunasPlanetas)
b2 = Button(master,text="Masa de Planetas")
b3 = Button(master,text="Tamano de Planetas")
b4 = Button(master,text="Tiempo respecto al Sol")


b4.pack()
b3.pack()
b2.pack()
b1.pack()

b4.place(relx=.35,rely=.6)
b3.place(relx=.375,rely=.53)
b2.place(relx=.39,rely=.46)
b1.place(relx=.39,rely=.39)




mainloop()