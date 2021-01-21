import tkinter as tk
from tkinter import (PhotoImage, Label, Menu, IntVar, Checkbutton,
                     Listbox, Scrollbar, RIGHT, END, Y, messagebox,
                     filedialog,ttk)
from tkinter import *
from tkinter.ttk import *

class Voorspel:
    def __init__(self,root):
        self.root = root
        # self.X = list(X.columns)
        # self.model = model
        # self.model.fit(X_train,y_train)
        # self.venster = self.voorspel_venster(root)
        # self.values = []

    def voorspel_venster(self):
        window = Toplevel(self.root)
        window.title('Predict')
        window.grab_set()
        resizable = window.resizable(False,False)
        window.geometry("400x500")

        info_frame = tk.LabelFrame(window)
        info_frame.place(height=400, width=200, rely=0, relx=0)

        # parameter_label = tk.LabelFrame(window)
        # parameter_label.place(height=100, width=200, rely=0, relx=0.5)

        parameter_text = Label(window,text=self.root.huidig_model.show_summary_label())
        parameter_text.place(rely=0, relx=0.55)
        
        values = []
        for count, value in enumerate(self.root.X):
            mylabel = Label(info_frame,text=value)
            mylabel.pack()
            my_entry = Entry(info_frame)
            my_entry.pack()
            values.append(my_entry)

        btnVoorspel = Button(window,text='Voorspel',command=lambda:self.show_answer(values))
        btnVoorspel.place(relx=0,rely=0.8)
        

    def show_answer(self,values):
        values_converted = []
        for entry in values:
            new = int(entry.get())
            # print(new)
            values_converted.append(new)
        print(values_converted)
        antwoord =  self.root.huidig_model.model.predict([values_converted])
        # for i in values_converted:
        #     print(i)
        # print(antwoord)
        return messagebox.showinfo('Voorspelling','Voorspelling op basis van ingevoerde waarde(s) : {}'.format(antwoord))




