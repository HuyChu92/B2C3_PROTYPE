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
        # self.summary = self.show_summary()
        self.accuracy = self.show_accuracy()    
    
    def showConfusionMatrix(self):
        sn.heatmap(self.conf_matrix, annot=True)
        plt.plot( label="Accuracy")
        plt.plot( label="Error")
        plt.title('Confusion Matrix')
        plt.show()
        return None

    # def show_summary(self):
    #     accuracy = round((accuracy_score(self.actual, self.predicted) * 100),2)
    #     error = 100-accuracy
    #     precision = round((precision_score(self.actual, self.predicted) * 100),2)
    #     recall = round((recall_score(self.actual, self.predicted) * 100),2)
    #     f1 = round((f1_score(self.actual, self.predicted) * 100),2)
    #     return 'Accuracy: {}%\nError: {}%\nprecision: {}%\nrecall: {}%\nfscore: {}'.format(accuracy,error,precision,recall,f1)

    def show_accuracy(self):
        # accuracy = round((accuracy_score(self.actual, self.predicted) * 100),2)
        # return str(accuracy)+'%'
        return round(accuracy_score(self.actual, self.predicted),2)


