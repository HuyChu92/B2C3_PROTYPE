import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
from classificationerror import  ErrorClassification
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class Model:
    """ Class model
    """
    def __init__(self,id,naam,train_percentage,df,X,y,scaling):
        self.id = id
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
        """ Laat het de naam, accuracy en type scaling zien
        """
        label = "Model: {}\nAccuracy: {}\nScaling: {}".format(self.naam,str(self.error_test.accuracy),self.scaling)
        return label
        
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
        self.split_data()
        if self.naam == 'KNN':
            self.model = KNeighborsClassifier(n_neighbors=k)
        elif self.naam == 'Logistic Regression':
            self.model = LogisticRegression()
        else:
            self.model = tree.DecisionTreeClassifier()

        self.model.fit(self.X_train, self.y_train)

        pred_train = self.model.predict(self.X_train)
        self.error_train = ErrorClassification(self.y_train,pred_train)
        # print(pred_train)
        pred_test = self.model.predict(self.X_test)
        self.error_test = ErrorClassification(self.y_test,pred_test)
    
    def voorspel_uitkomst(self,waardes):
        """ Predict een uitkomst op basis van ingevoerde waardes
        """
        uitkomst = self.model.predict([waardes])
        return uitkomst[0]


            


    
        
