import tkinter as tk
from tkinter import (PhotoImage, Label, Menu, IntVar, Checkbutton,
                     Listbox, Scrollbar, RIGHT, END, Y, messagebox,
                     filedialog,ttk)
from tkinter import *
from tkinter.ttk import *

class Geavanceerd:
    def __init__(self,root):
        self.root = root

    def geavanceerd_venster(self):
        window = Toplevel(self.root)
        window.title('Geavanceerde instellingen')
        resizable = window.resizable(False,False)
        window.geometry("400x500")
        window.grab_set()

        label_preprocess = tk.LabelFrame(window, text='Wijzig de parameters')
        label_preprocess.place(height=150, width=400, rely=0, relx=0)

        train_label = tk.Label(label_preprocess,text='Kies train %')
        train_label.place(rely=0, relx=0.1)

        variable1 = tk.StringVar(label_preprocess)
        keuzes_train = ['50%', '55%', '60%', '65%', '70%', '75%', '80%', '85%', '90%', '95%']
        train_percentage = OptionMenu(label_preprocess,variable1,*keuzes_train)
        train_percentage.place(rely=0.2, relx=0.1)
        
        label_schalen = tk.Label(label_preprocess,text='Scaling')
        label_schalen.place(rely=0, relx=0.35)

        variable2 = tk.StringVar(label_preprocess)
        keuzes_schalen = ['Standaardiseer','Normaliseer','Niet schalen']
        train_percentage = OptionMenu(label_preprocess,variable2,*keuzes_schalen)
        train_percentage.place(rely=0.2, relx=0.35)

        button_preprocess_ok = Button(label_preprocess,text='OK',command=lambda: self.apply_process_parameter(variable1.get(),variable2.get()))
        button_preprocess_ok.place(relx=0.8,rely=0.8)

        parameter_knn_label = tk.LabelFrame(window, text='Wijzig de parameters binnen KNN')
        parameter_knn_label.place(height=150, width=400, rely=0.33, relx=0)

        threshold_label = tk.Label(parameter_knn_label,text='Threshold K')
        threshold_label.place(rely=0, relx=0.1)

        threshold_k = tk.StringVar(parameter_knn_label)
        keuzes_threshold = [num for num in range(1,31)]
        threshold_menu = OptionMenu(parameter_knn_label,threshold_k,*keuzes_threshold)
        threshold_menu.place(rely=0.2, relx=0.1)

        button_knn_ok = Button(parameter_knn_label,text='OK',command=lambda: self.apply_threshold_k(threshold_k.get()))
        button_knn_ok.place(relx=0.8,rely=0.8)

        parameter_logistic_label = tk.LabelFrame(window, text='Wijzig de parameters binnen Logistic Regression')
        parameter_logistic_label.place(height=150, width=400, rely=0.66, relx=0)

        cutoff_label = tk.Label(parameter_logistic_label,text='Cutoff threshold')
        cutoff_label.place(rely=0, relx=0.1)

        cutoff = tk.StringVar(parameter_logistic_label)
        keuzes_cutoff = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]
        threshold_menu = OptionMenu(parameter_logistic_label,cutoff,*keuzes_cutoff)
        threshold_menu.place(rely=0.2, relx=0.1)

        button_logistic_ok = Button(parameter_logistic_label,text='OK',command=lambda: self.apply_cutoff(cutoff.get()))
        button_logistic_ok.place(relx=0.8,rely=0.8)
    
    def apply_process_parameter(self,train,scaling):
        self.root.train = train
        self.root.scaling = scaling
        print(self.root.train,self.root.scaling)
        return messagebox.showinfo('Gelukt','Parameters datapreprocessing aangepast')

    def apply_threshold_k(self,k):
        self.root.k = int(k)
        print(self.root.k)
        return messagebox.showinfo('Gelukt','Threshold K aangepast')

    def apply_cutoff(self,value):
        self.root.cutoff = float(value)
        print(self.root.cutoff)
        return messagebox.showinfo('Gelukt','Cutoff value aangepast')
        

        


        
        