import yandextranslate
from tkinter import *
import langs

class ydxargs:
	def __init__(o, l1, l2, text):
		o.l1=l1
		o.l2=l2
		o.text=text



class ydxgui:
	
	def trns(o, e):
		text=o.root.t1e.get()
		l1=o.langs[1][o.langs[0].index(str(o.lf.get()))]
		l2=o.langs[1][o.langs[0].index(str(o.lt.get()))]
		a=ydxargs(l1, l2, text)
		o.root.t2l.delete(0, END)
		o.root.t2l.insert(0, yandextranslate.ydx(a)["text"][0])
	
	def __init__(o):
		o.langs=langs.getlangs()		

		o.root=Tk()
		o.root.title("Yandex translate")
		#o.root.minsize(height=300, width=500)
				
		o.lf=StringVar(o.root)
		o.lf.set(o.langs[0][0])
		o.lt=StringVar(o.root)
		o.lt.set(o.langs[0][0])

		o.root.l1l=Label(o.root, text="From:")
		o.root.l2l=Label(o.root, text="To:")
		o.root.larrl=Label(o.root, text="->")
		o.root.l1e=OptionMenu(o.root, o.lf, *o.langs[0])
		o.root.l2e=OptionMenu(o.root, o.lt, *o.langs[0])
		o.root.t1e=Entry(o.root)
		o.root.t2l=Entry(o.root)
		o.root.trb=Button(o.root, text="Translate")
		
		o.root.l1l.grid(column=0, row=0)
		o.root.larrl.grid(column=1, row=1)
		o.root.l2l.grid(column=2, row=0)
		o.root.l1e.grid(column=0, row=1)
		o.root.l2e.grid(column=2, row=1)
		o.root.t1e.grid(column=1, row=2)
		o.root.t2l.grid(column=1, row=4)
		o.root.trb.grid(column=1, row=3)
		
		o.root.trb.bind("<Button-1>", o.trns)
		
		o.root.mainloop()
o=ydxgui()
