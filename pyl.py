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

#cuando se selecciona una luna
def select(event):
    lunasFrames = Toplevel()
    contador = 0
    lunaList = Listbox(lunasFrames)
    e = event.widget
    index = int(e.curselection()[0])
    valor = e.get(index)
    for luna in prolog.query("satelites(Planeta,Luna)"):
        if valor == luna["Planeta"]:
            if luna["Luna"] == []:
                lunaList.insert(contador,"No tiene luna(s)")
            else:
                for moon in luna["Luna"]:
                    lunaList.insert(contador,moon)
                    contador += 1
    lunaList.pack()

    print 'You selected item %d: "%s"' % (index, valor)

def lunasPlanetas():
    child1 = Toplevel()
    Lb1 = Listbox(child1, selectmode=SINGLE)

    i=1
    for luna in prolog.query("satelites(Planeta,Luna)"):
        Lb1.insert(i, luna["Planeta"])
        i += 1

    Lb1.bind('<<ListboxSelect>>',select)

    Lb1.pack()


def llamada(masas,diccionario):
    print masas.split()
    masaFrame2 = Toplevel()
    listamasa = Listbox(masaFrame2)
    k = 0  # contador para listamasa
    for planeta in masas.split():
        if planeta in diccionario:
            listamasa.insert(k, planeta + ": " + str(diccionario[planeta]))
            k += 1
        else:
            listamasa.insert(k, planeta + " no es valido")
            k += 1
    listamasa.pack()


def dibujar(listaPlaneta):
    dibujos = Toplevel()
    listPlan =  listaPlaneta.split()
    d = Canvas(dibujos)
    k=0

    for var in prolog.query("planeta(Planeta,Clasificacion,Masa,Posicion)"):
        for plan in listPlan:
            if var["Planeta"] == plan:
                oval = d.create_oval(var["Posicion"]*k,var["Posicion"]+10,var["Masa"]*10,var["Masa"]+10,fill = "blue")
                #labels = Label(dibujos, text=var["Planeta"])
                k+5
    d.pack()
    #labels.pack(side = TOP)



def masaPlanetas():
    masaFrame = Toplevel()
    masaFrame.minsize(400,400)
    lista = Listbox(masaFrame)
    diccionario = {}

    i = 1
    for luna in prolog.query("planeta(Planeta,Clasificacion,Masa,Posicion)"):
        lista.insert(i,str(luna["Posicion"])+". "+ luna["Planeta"])
        diccionario[luna["Planeta"]] = [luna["Masa"]]
        i += 1
    lista.pack()

    labels = Label(masaFrame,text="Numero(s) de Planeta(s):")
    labels.pack()
    labels.place(relx=.05,rely=.8)
    listaPlaneta = Entry(masaFrame,bd=15)
    listaPlaneta.pack(side=BOTTOM)
    listaPlaneta.place(relx=.5, rely=.82)

    botonMasa = Button(masaFrame, text="Masa", command = lambda: llamada(listaPlaneta.get(),diccionario))
    botonMasa.pack()
    botonMasa.place(relx=.06, rely=.87)
    botonTamano = Button(masaFrame, text="Tamano",command = lambda: dibujar(listaPlaneta.get()))
    botonTamano.pack()
    botonTamano.place(relx=.2, rely=.87)




b1 = Button(master,text="Lunas de Planetas",command = lunasPlanetas)
b2 = Button(master,text="Masa de Planetas",command = masaPlanetas)
b3 = Button(master, text="Tiempo respecto al Sol")


b3.pack()
b2.pack()
b1.pack()

b3.place(relx=.35, rely=.53)
b2.place(relx=.39,rely=.46)
b1.place(relx=.39,rely=.39)




mainloop()