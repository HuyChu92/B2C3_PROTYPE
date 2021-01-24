import math
import numpy as np
import math
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import plot_confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt
from tkinter import messagebox
from sklearn.metrics import f1_score, precision_score, recall_score

class ErrorClassification:
    def __init__(self, actual, predicted):
        self.actual = actual
        self.predicted = predicted
        self.conf_matrix = confusion_matrix(self.actual, self.predicted)
        self.accuracy = self.show_accuracy()    
        self.recall = self.show_recall()
        self.error = round((1 - self.accuracy),2)
        self.precision = self.show_precision()
    
    def showConfusionMatrix(self):
        sn.heatmap(self.conf_matrix, annot=True)
        plt.plot( label="Accuracy")
        plt.plot( label="Error")
        plt.figtext(0,0,'Accuracy: {}\nError: {}\nRecall: {}\nPrecision: {}'.format(self.accuracy,
                                                                                    self.error,
                                                                                    self.recall,
                                                                                    self.precision))
        plt.title('Confusion Matrix')
        plt.show()
        return None

    def show_accuracy(self):
        """ Geeft de accuracy terug
        """
        return round(accuracy_score(self.actual, self.predicted),2)
    
    def show_recall(self):
        """ Geeft de recall score terug """
        return round((recall_score(self.actual, self.predicted)*100),2)

    def show_precision(self):
        """ Geeft de precision score terug """
        return round(f1_score(self.actual, self.predicted),2)
    




