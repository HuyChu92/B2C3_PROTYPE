import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from classificationerror import  ErrorClassification
from regressionerror import ErrorRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import tkinter

class Model:
    """ Class model
    """
    def __init__(self,id,naam,train_percentage,df,X,y,scaling,soort):
        self.id = id
        self.soort = soort
        self.naam = naam
        self.model = None
        self.df = df
        self.df.dropna()
        self.train_percentage = train_percentage
        self.X = self.df[X]
        self.y = self.df[y]
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.scaling = scaling
        self.error_train = None
        self.error_test = None
    
    def show_summary_label(self):
        """ Laat het de naam, accuracy, r2 en type scaling zien op basis van type voorspelling
        """
        if self.soort == 'Classification':
            label = "Model: {}\nAccuracy: {}\nScaling: {}".format(self.naam,str(self.error_test.accuracy),self.scaling)
        else:
            label = "Model: {}\nRMSE: {}\nR2: {}\nSSE: {}\nScaling: {}".format(self.naam,str(self.error_test.rmse),self.error_test.r2,self.error_test.sse,self.scaling)
        return label
    
    def show_extensive_summary(self):
        """ Laat een uitgebreide summary zien van de errors o.b.v. classification of regression"""
        if self.soort == 'Classification':
            self.error_test.showConfusionMatrix()
        else:
            self.error_test.show_boxplot()

        
    def split_data(self):
        """ Split de trainingsdata o.b.v. type scaling en trainingspercentage
        """
        if self.scaling == 'Standaardiseer':
            self.X = pd.DataFrame(StandardScaler().fit_transform(self.X))
        elif self.scaling == 'Normaliseer':
            self.X = pd.DataFrame(MinMaxScaler().fit_transform(self.X))
        percentage = int(self.train_percentage.replace('%','')) / 100
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,test_size=percentage)
        return None

    def maak_model(self,k=5): 
        """ Maakt een model aan op basis van meegegeven techniek
        """
        # self.split_data()
        if self.naam == 'KNN Classification':
            self.X = pd.DataFrame(MinMaxScaler().fit_transform(self.X))
            percentage = int(self.train_percentage.replace('%','')) / 100
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,test_size=percentage)
            self.model = KNeighborsClassifier(n_neighbors=k)
        elif self.naam == 'KNN Regression':
            self.X = pd.DataFrame(MinMaxScaler().fit_transform(self.X))
            percentage = int(self.train_percentage.replace('%','')) / 100
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,test_size=percentage)
            self.model = KNeighborsRegressor(n_neighbors=k)
        elif self.naam == 'Logistic Regression':
            self.split_data()
            self.model = LogisticRegression()
        elif self.naam == 'MLR':
            self.split_data()
            self.model = LinearRegression()
        elif self.naam == 'Decision Tree Regression':
            self.split_data()
            self.model = DecisionTreeRegressor(max_leaf_nodes=k)
        else:
            self.split_data()
            self.model = tree.DecisionTreeClassifier()

        self.model.fit(self.X_train, self.y_train)

        if self.soort == 'Classification':
            pred_train = self.model.predict(self.X_train)
            self.error_train = ErrorClassification(self.y_train,pred_train)
            pred_test = self.model.predict(self.X_test)
            self.error_test = ErrorClassification(self.y_test,pred_test)
        else:
            pred_train = self.model.predict(self.X_train)
            self.error_train = ErrorRegression(self.y_train,pred_train)
            pred_test = self.model.predict(self.X_test)
            self.error_test = ErrorRegression(self.y_test,pred_test)

    
    def voorspel_uitkomst(self,waardes):
        """ Predict een uitkomst op basis van ingevoerde waardes
        """
        uitkomst = self.model.predict([waardes])
        return uitkomst[0]


            


    
        
