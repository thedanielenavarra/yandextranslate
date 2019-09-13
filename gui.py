import yandextranslate
from tkinter import *

class ydxargs:
	def __init__(o, l1, l2, text):
		o.l1=l1
		o.l2=l2
		o.text=text

class ydxgui:
	
	def trns(o, e):
		text=o.root.t1e.get()
		l1=o.root.l1e.get()
		l2=o.root.l2e.get()
		a=ydxargs(l1, l2, text)
		o.root.t2l["text"]=yandextranslate.ydx(a)["text"]
	
	def __init__(o):
		o.root=Tk()
		o.root.title("Yandex translate")
		o.root.minsize(height=300, width=500)
		
		o.root.l1l=Label(o.root, text="From:")
		o.root.l2l=Label(o.root, text="To:")
		o.root.larrl=Label(o.root, text="->")
		o.root.l1e=Entry(o.root)
		o.root.l2e=Entry(o.root)
		o.root.t1e=Entry(o.root)
		o.root.t2l=Label(o.root)
		o.root.trb=Button(o.root, text="Translate")
		
		o.root.l1l.grid(column=0, row=0)
		o.root.larrl.grid(column=1, row=1)
		o.root.l2l.grid(column=2, row=0)
		o.root.l1e.grid(column=0, row=1)
		o.root.l2e.grid(column=2, row=1)
		o.root.t1e.grid(column=0, row=2)
		o.root.t2l.grid(column=2, row=2)
		o.root.trb.grid(column=1, row=2)
		
		o.root.trb.bind("<Button-1>", o.trns)
		
		o.root.mainloop()
o=ydxgui()
