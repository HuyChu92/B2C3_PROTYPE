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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import tkinter.tix as tkx
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
from classificationerror import ErrorClassification
# from evalueer import Evaluate
from voorspelframe import Voorspel
from modelhandler import Model

class Bestmodel:
    def __init__(self,root,k):
        self.k = k
        self.root = root
        self.best_knn = self.generate_best_knn()
        self.best_logistic = self.generate_logistic_model()
        self.best_decision_tree = self.generate_decisiontree_model()


    def best_model_frame(self):
        """ Summary venster zien
        """
        window = Toplevel(self.root)
        resizable = window.resizable(False,False)
        window.geometry("400x500")

        best_model_label = tk.LabelFrame(window)
        best_model_label.place(height=400, width=400, rely=0, relx=0)

        tv1 = ttk.Treeview(best_model_label)
        tv1.place(relheight=1, relwidth=1)

        treescrolly = tk.Scrollbar(best_model_label, orient='vertical', command=tv1.yview)
        treescrollx = tk.Scrollbar(best_model_label, orient='horizontal', command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")
        self.show_best_models(tv1)
        
        select_best_model = tk.LabelFrame(window,text='Selecteer een model en laad deze in')
        select_best_model.place(height=100, width=400, rely=0.8, relx=0)

        laad_button = Button(select_best_model,text='Laad model',command=lambda: self.model_laden(tv1,window))
        laad_button.place(relx=0.8,rely=0)
    
    def model_laden(self,tree,venster):
        """ Laad een model in
        """
        curItem = tree.focus()
        lijst = tree.item(curItem)
        if lijst['values'][0] == 'KNN':
            self.root.huidig_model = self.best_knn
            self.root.label_parameter.config(text=self.best_knn.show_summary_label())
        elif lijst['values'][0] == 'Logistic Regression':
            self.root.huidig_model = self.best_logistic
            self.root.label_parameter.config(text=self.best_logistic.show_summary_label())
        else:
            self.root.huidig_model = self.best_decision_tree
            self.root.label_parameter.config(text=self.best_decision_tree.show_summary_label())
        self.root.voorspel = Voorspel(self.root)
        self.root.voorspel.voorspel_venster()
        venster.destroy()
        
    def generate_best_knn(self):
        """ Geneert het beste model o.b.v. de K threshold. 
        """
        lijst_knn = []
        for num in range(1,self.root.k+1):
            model = Model(num,'KNN',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling)
            model.maak_model(num)
            lijst_knn.append(model)

        acc = 0
        best = None
        for model in lijst_knn:
            if model.error_test.accuracy > acc:
                acc = model.error_test.accuracy
                best = model
        print(best.X)
        return best

    def generate_logistic_model(self):
        """ Genereert logistic regression model
        """
        model = Model(1,'Logistic Regression','60%',self.root.df,self.root.X,self.root.y,self.root.scaling)
        model.maak_model()
        return model

    def generate_decisiontree_model(self):
        """ Genereet best decision  classification tree model
        """
        model = Model(1,'Decision Tree','60%',self.root.df,self.root.X,self.root.y,self.root.scaling)
        model.maak_model()
        return model

    def show_best_models(self,window):
        """ Laat alle beste modellen binnen classification zien
        """
        model_name = []
        accuracy = []

        accuracy.append(self.best_knn.error_test.accuracy)
        accuracy.append(self.best_logistic.error_test.accuracy)
        accuracy.append(self.best_decision_tree.error_test.accuracy)

        model_name.append(self.best_knn.naam)
        model_name.append(self.best_logistic.naam)
        model_name.append(self.best_decision_tree.naam)

        df = pd.DataFrame(list(zip(model_name, accuracy)), columns =['Model', 'Accuracy']) 
        window["column"] = list(df.columns)
        window["show"] = "headings"
        for column in window["columns"]:
            window.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            window.insert("", "end", values=row)

    def laad_model(self):
        models = [self.best_knn,self.best_logistic,self.best_decision_tree]
        acc = 0
        best_model = None
        for model in models:
            if model.error_test.accuracy > acc:
                acc = model.error_test.accuracy
                best_model = model
        self.root.huidig_model = best_model
        self.root.label_parameter.config(text=best_model.show_summary_label())
        self.root.voorspel = Voorspel(self.root)
        self.root.voorspel.voorspel_venster()
        return messagebox.showinfo('Gelukt','Beste model op basis van ingevoerde variabelen:\n{}'.format(best_model.show_summary_label()))
      
