import tkinter as tk
from tkinter import (PhotoImage, Label, Menu, IntVar, Checkbutton,
                     Listbox, Scrollbar, RIGHT, END, Y, messagebox,
                     filedialog,ttk)
from tkinter import *
from tkinter.ttk import *
import pandas as pd
import numpy 
import xlrd as xl
import openpyxl as ox
import numpy as np
from classificationerror import ErrorClassification
from voorspelframe import Voorspel
from bestmodelgenerator import Bestmodel
from geavanceerdframe import Geavanceerd


class Classification(tk.Frame):
    """
    """
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.width = 800
        self.height = 600
        self.file = self.master.file
        self.df = self.master.path
        self.huidig_model = None
        self.X = []
        self.y = None
        self.best_model = None
        self.voorspel = None
        self.geavanceerd = Geavanceerd(self)
        self.k = 10
        self.cutoff = 0.5
        self.train = '60%'
        self.scaling = 'Standaardiseer'
        
        canvas = tk.Canvas(self, height=self.height, width=self.width)
        canvas.pack()

        self.label_predictors = tk.LabelFrame(self, text="Voeg de independent variabel(en) toe")
        self.label_predictors.place(height=400, width=500, rely=0, relx=0)
        
        self.tool_label = tk.LabelFrame(self, text="Selecteer wat u wilt doen")
        self.tool_label.place(height=400, width=290, rely=0, relx=0.63)

        self.parameter_frame = tk.LabelFrame(self, text="Parameters")
        self.parameter_frame.place(height=150, width=250, rely=0.68, relx=0)

        self.label_bestand = tk.Label(self.parameter_frame,text=self.master.file)
        self.label_bestand.pack()

        self.label_parameter = tk.Label(self.parameter_frame,text='Test')
        self.label_parameter.pack()

        self.list_columns = Listbox(self.label_predictors)
        self.list_columns.place(relheight=0.7, relwidth=0.4)
        scrollbar = Scrollbar(self.list_columns)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.show_colums(self.list_columns,self.df)

        button_add = tk.Button(self.label_predictors, text="⇨", command=lambda : self.add_independent_var(self.list_columns))
        button_add.place(rely=0.7, relx=0.35)

        button_remove = tk.Button(self.label_predictors, text="✖", command=lambda : self.remove_independent_var())
        button_remove.place(rely=0.7, relx=0.85)
        
        self.list_independent = Listbox(self.label_predictors)
        self.list_independent.place(relheight=0.7, relwidth=0.4, rely=0, relx=0.5)
        scrollbar = Scrollbar(self.list_independent)
        scrollbar.pack(side=RIGHT, fill=Y)

        variable = StringVar(self.label_predictors)
  
        pred_val = OptionMenu(self.label_predictors, variable, *self.get_categorical_columns())
        pred_val.place(rely=0.9, relx=0.1)

        button_select_y = tk.Button(self.label_predictors, text="Selecteer", command=lambda : self.choose_dependent_val(variable.get()))
        button_select_y.place(rely=0.9, relx=0.5)

        button_partitie = tk.Button(self, text="Terug", command=lambda : self.master.start())
        button_partitie.place(rely=0.9, relx=0.9)

        button_train = tk.Button(self.label_predictors, text="Train", 
                                command=lambda : messagebox.showerror('Waarschuwing','Selecteer eerst alle variabelen') if self.y == None
                                else self.train_button())
        button_train.place(rely=0.8, relx=0.82)

        button_clear = tk.Button(self.label_predictors, text="Clear", command=lambda : self.clear())
        button_clear.place(rely=0.9, relx=0.82)

        button_voorspel = tk.Button(self.tool_label, text="Voorspel",
                                    command=lambda :messagebox.showerror('Waarschuwing','Maak eerst het model!')if self.voorspel == None
                                    else self.voorspel.voorspel_venster())               
        button_voorspel.place(rely=0.1, relx=0.1)
  
        button_summary = tk.Button(self.tool_label, text="Summary",
                                    command=lambda :self.best_model.best_model_frame())                
        button_summary.place(rely=0.2, relx=0.1)

        button_geavanceerd = tk.Button(self.tool_label, text="Geavanceerd",command=lambda : self.geavanceerd.geavanceerd_venster())                      
        button_geavanceerd.place(rely=0.3, relx=0.1)

    def train_button(self):
        """ Verwijdert NaN values uit dataframe en maakt een object(Bestmodel) aan
            waarbij het beste model word gegenereerd op basis van de ingevoerde variabelen
        """
        self.df.dropna(how='any')
        self.df.dropna(how='any',inplace= True)
        self.best_model = Bestmodel(self,self.k)
        self.best_model.laad_model()

    def show_colums(self, box, dataframe):
        """ Weergeeft de column
        """
        for clm in dataframe.columns:
            box.insert(END, clm)
    
    def add_independent_var(self, columns):
        """ Voegt de geselecteerde variabel toe aan self.X
        """
        waarde = self.list_columns.get(self.list_columns.curselection())
        if waarde == self.y:
            return messagebox.showwarning("Warning", "Variabel is als dependent variabel gekozen!")
        elif waarde in self.X:
            return messagebox.showwarning('Warning', 'Variabel reeds gekozen!')
        else:
            self.X.append(waarde)
            self.list_independent.delete(0, END)
            self.show_colums(self.list_independent,self.df[self.X])
        return None

    def remove_independent_var(self):
        """ Verwijdert geselecteerd variabel uit self.X
        """
        waarde = self.list_independent.get(self.list_independent.curselection())
        self.X.remove(waarde)
        self.list_independent.delete(0, END)
        self.show_colums(self.list_independent,self.df[self.X])

    def get_categorical_columns(self):
        """ Selecteert de categorische columns uit df 
        """
        category_features = []
        threshold = 4
        for each in self.df.columns:
            if self.df[each].nunique() < threshold:
                category_features.append(each)
        for each in category_features:
            self.df[each] = self.df[each].astype('category')
        return category_features

    def choose_dependent_val(self, dependent):
        """ Stel de dependent variabel in
        """
        if dependent in self.X:
            return messagebox.showwarning("Warning", "Gekozen y variable zit al in de predictors!")
        self.y = dependent
        return messagebox.showinfo("Gelukt", "'{}' als dependent variabel gekozen".format(dependent))

    def clear(self):
        """ Wis het het huidige model en zet alle parameters terug naar hun beginwaardes
        """
        self.huidig_model = None
        self.X = []
        self.y = None
        self.best_model = None
        self.voorspel = None
        self.k = 5
        self.list_independent.delete(0,'end')
        self.label_parameter.config(text='')

    