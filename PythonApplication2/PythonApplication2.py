from tkinter import *
name=["весы","близнецы","лев","телец","водолей","Рак","Стрелец","Скорпион","дева","рыбы","Овен","козерог"]  #Содержание списка
foto_list=["весы.gif","близнецы.gif","лев.gif","телец.gif","водолей.gif","Рак.gif","Стрелец.gif","Скорпион.gif","дева.gif","рыбы.gif","Овен.gif","козерог.gif"]
def list_to_txt(event):
 global can,foto
 txt.delete(0.0,END)
 valik=lbox.curselection()  #Выдаст значения
 txt.insert(END,lbox.get(valik[0]))
 can.delete(ALL)
 foto=PhotoImage(file=foto_list(valik[0]))
 can.create_image(0,0,image=foto,anchor=NW)
 def txt_to_list(event):
     text=txt.get(0,0,END)
     text=text[-2:-1]
     if text=='\n':
      pass
     else:
         list_.append(text)
         print(list_)
win=Tk()
lbox=Listbox(win,width=20,height=len(name),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)
lbox.grid(row=0,column=0)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=1,width=20,wrap=WORD)
txt.grid(row=0,column=1)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=130,bg="black")
can.grid(row=1,column=0,columnspan=2)
foto=PhotoImage(file="vse.png")
can.create_image(0,0,image=foto,anchor=NW)
win.maailoop()
