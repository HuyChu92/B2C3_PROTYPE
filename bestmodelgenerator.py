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
        self.best_knn_classification = self.generate_best_knn_classification()
        self.best_knn_regression = self.generate_best_knn_regression()
        self.best_logistic = self.generate_logistic_model()
        self.best_decisiontree_class = self.generate_decisiontreeClassification()
        self.best_decisiontree_regr = self.generate_decisiontreeRegression()
        self.best_mlr = self.generate_mlr_model()


    def best_model_frame(self):
        """ Summary venster zien
        """
        window = Toplevel(self.root)
        resizable = window.resizable(False,False)
        window.geometry("600x500")

        best_model_label = tk.LabelFrame(window)
        best_model_label.place(height=400, width=600, rely=0, relx=0)

        tv1 = ttk.Treeview(best_model_label)
        tv1.place(relheight=1, relwidth=1)

        treescrolly = tk.Scrollbar(best_model_label, orient='vertical', command=tv1.yview)
        treescrollx = tk.Scrollbar(best_model_label, orient='horizontal', command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")
        if self.root.name == 'Classification':
            self.show_best_models_classification(tv1)
        else:
            self.show_best_models_regression(tv1)
        
        select_best_model = tk.LabelFrame(window,text='Selecteer een model en laad deze in of bekijk een uitgebreide summary van het geselecteerde model')
        select_best_model.place(height=100, width=600, rely=0.8, relx=0)

        laad_button = Button(select_best_model,text='Laad model',command=lambda: self.model_laden(tv1,window))
        laad_button.place(relx=0.85,rely=0)

        extensive_summary = Button(select_best_model,text='Extensive Summary',command=lambda: self.extensive_summary_model(tv1))
        extensive_summary.place(relx=0,rely=0)
    
    def extensive_summary_model(self,tree):
        """ Laat een uitgebreide error summary zien als de gebruiker op de knop drukt"""
        curItem = tree.focus()
        lijst = tree.item(curItem)
        if lijst['values'][0] == 'KNN Classification':
            self.best_knn_classification.show_extensive_summary()
        elif lijst['values'][0] == 'KNN Regression':
            self.best_knn_regression.show_extensive_summary()
        elif lijst['values'][0] == 'MLR':
            self.best_mlr.show_extensive_summary()
        elif lijst['values'][0] == 'Logistic Regression':
            self.best_logistic.show_extensive_summary()
        elif lijst['values'][0] == 'Decision Tree Regression':
            self.best_decisiontree_regr.show_extensive_summary()
        else:
            self.best_knn_classification.show_extensive_summary()
        # curItem = tree.focus()
        # lijst = tree.item(curItem)
        # if lijst['values'][0] == 'KNN Classification':
        #     self.best_knn_classification.show_extensive_summary()
        
        # elif lijst['values'][0] == 'Logistic Regression':
        #     self.best_logistic.show_extensive_summary()
        # else:
        #     self.best_decisiontree_class.show_extensive_summary()


    def model_laden(self,tree,venster):
        """ Laad een model in
        """
        curItem = tree.focus()
        lijst = tree.item(curItem)
        if lijst['values'][0] == 'KNN Classification':
            self.root.huidig_model = self.best_knn_classification
            self.root.label_parameter.config(text=self.best_knn_classification.show_summary_label())
        elif lijst['values'][0] == 'KNN Regression':
            self.root.huidig_model = self.best_knn_regression
            self.root.label_parameter.config(text=self.best_knn_regression.show_summary_label())
        elif lijst['values'][0] == 'MLR':
            self.root.huidig_model = self.best_mlr
            self.root.label_parameter.config(text=self.best_mlr.show_summary_label())
        elif lijst['values'][0] == 'Logistic Regression':
            self.root.huidig_model = self.best_logistic
            self.root.label_parameter.config(text=self.best_logistic.show_summary_label())
        elif lijst['values'][0] == 'Decision Tree Regression':
            self.root.huidig_model = self.best_decisiontree_regr
            self.root.label_parameter.config(text=self.best_decisiontree_regr.show_summary_label())
        else:
            self.root.huidig_model = self.best_decisiontree_class
            self.root.label_parameter.config(text=self.best_decisiontree_class.show_summary_label())
        self.root.voorspel = Voorspel(self.root)
        self.root.voorspel.voorspel_venster()
        venster.destroy()
        
    def generate_best_knn_classification(self):
        """ Geneert het beste model o.b.v. de K threshold. 
        """
        if self.root.name == 'Regression':
            return None
        lijst_knn = []
        for num in range(1,self.root.k+1):
            model = Model(num,'KNN Classification',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Classification')
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

    def generate_best_knn_regression(self):
        """ Geneert het beste model o.b.v. de K threshold. 
        """
        if self.root.name == 'Classification':
            return None
        lijst_knn = []
        for num in range(1,self.root.k+1):
            model = Model(num,'KNN Regression',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Regression')
            model.maak_model(num)
            lijst_knn.append(model)

        r2 = 0
        best = None
        for model in lijst_knn:
            if model.error_test.r2 > r2:
                r2 = model.error_test.r2
                best = model
                # print(best.naam)
        # print(best.X)
        return best

    def generate_logistic_model(self):
        """ Genereert logistic regression model
        """
        if self.root.name == 'Regression':
            return None
        model = Model(1,'Logistic Regression',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Classification')
        model.maak_model()
        return model

    def generate_mlr_model(self):
        """ Genereert MLR model 
        """ 
        if self.root.name == 'Classification':
            return None
        model = Model(1,'MLR',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Regression')
        model.maak_model()
        return model

    def generate_decisiontreeClassification(self):
        """ Selecteer het beste decision tree regression model op 
            basis van de 'max leaves nodes' en accuracy score
        """
        if self.root.name == 'Regression':
            return None
        lijst_dtr = []
        for num in range(2,100):
            model = Model(num,'Decision Tree Classification',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Classification')
            model.maak_model(num)
            lijst_dtr.append(model)

        acc = 0
        best = None
        for model in lijst_dtr:
            if model.error_test.accuracy > acc:
                acc = model.error_test.accuracy
                best = model
        return best

    def generate_decisiontreeRegression(self):
        """ Selecteer het beste decision tree regression model op 
            basis van de 'max leaves nodes' en rmse score
        """
        if self.root.name == 'Classification':
            return None
        lijst_dtr = []
        for num in range(2,100):
            model = Model(num,'Decision Tree Regression',self.root.train,self.root.df,self.root.X,self.root.y,self.root.scaling,'Regression')
            model.maak_model(num)
            lijst_dtr.append(model)

        rmse = 100000
        best = None
        for model in lijst_dtr:
            if model.error_test.rmse < rmse:
                rmse = model.error_test.rmse
                best = model
        return best
  

    def show_best_models_classification(self,window):
        """ Laat alle beste modellen binnen classification zien
        """
        model_name = []
        accuracy = []

        accuracy.append(self.best_knn_classification.error_test.accuracy)
        accuracy.append(self.best_logistic.error_test.accuracy)
        accuracy.append(self.best_decisiontree_class.error_test.accuracy)

        model_name.append(self.best_knn_classification.naam)
        model_name.append(self.best_logistic.naam)
        model_name.append(self.best_decisiontree_class.naam)

        df = pd.DataFrame(list(zip(model_name, accuracy)), columns =['Model', 'Accuracy']) 
        window["column"] = list(df.columns)
        window["show"] = "headings"
        for column in window["columns"]:
            window.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            window.insert("", "end", values=row)

    def show_best_models_regression(self,window):
        """ Laat alle beste modellen binnen classification zien
        """
        model_name = []
        r2 = []
        rmse = []
        r2.append(self.best_knn_regression.error_test.r2)
        r2.append(self.best_mlr.error_test.r2)
        r2.append(self.best_decisiontree_regr.error_test.r2)

        rmse.append(self.best_knn_regression.error_test.rmse)
        rmse.append(self.best_mlr.error_test.rmse)
        rmse.append(self.best_decisiontree_regr.error_test.rmse)

        model_name.append(self.best_knn_regression.naam)
        model_name.append(self.best_mlr.naam)
        model_name.append(self.best_decisiontree_regr.naam)

        df = pd.DataFrame(list(zip(model_name,rmse,r2)), columns =['Model','RMSE', 'R2']) 
        window["column"] = list(df.columns)
        window["show"] = "headings"
        for column in window["columns"]:
            window.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            window.insert("", "end", values=row)

    def laad_model_classification(self):
        """ Laad een classification model in op basis van selectie""" 
        models = [self.best_knn_classification,self.best_logistic,self.best_decisiontree_class]
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

    def laad_model_regression(self):
        """ Laad een regression model in op basis van selectie""" 
        models = [self.best_knn_regression,self.best_mlr,self.best_decisiontree_regr]
        rmse = 100000000
        best_model = None
        for model in models:
            if model.error_test.rmse < rmse:
                rmse = model.error_test.rmse
                best_model = model
        self.root.huidig_model = best_model
        self.root.label_parameter.config(text=best_model.show_summary_label())
        self.root.voorspel = Voorspel(self.root)
        self.root.voorspel.voorspel_venster()
        return messagebox.showinfo('Gelukt','Beste model op basis van ingevoerde variabelen:\n{}'.format(best_model.show_summary_label()))
      
