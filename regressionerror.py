import math
import numpy as np
import math
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt


class ErrorRegression:
    def __init__(self,actual,predicted):
        self.actual = actual
        self.predicted = predicted
        self.residuals = self.calculate_residuals()
        self.r2 = self.rootsquaredBerekenen()
        self.rmse = self.rmseBerekenen()
        self.sse = self.sseBerekenen()
        
    def rootsquaredBerekenen(self):
        """ Geeft r2 terug"""
        rootsquared = round(r2_score(self.actual,self.predicted),2)
        return rootsquared

    def rmseBerekenen(self):
        """ Geeft rmse terug"""
        rmse = mean_squared_error(self.actual, self.predicted, squared=False)
        return round(rmse,2)
    
    def sseBerekenen(self):
        """ Geeft sse terug"""
        uitkomst = []
        for num in self.residuals:
            uitkomst.append(num*num)
        return sum(uitkomst)

    def calculate_residuals(self):
        """ Berekent residuals o.b.v. actual en predicted"""
        verschil = []
        for i, waarde in enumerate(self.actual):
            verschil.append(abs(waarde - self.predicted[i]))
        return verschil
        
    def show_boxplot(self):
        """ Laat een weergave van een Boxplot van de residuals met de bijbehorende
            mean, median, min value en max value"""
        mean = np.round(np.mean(self.residuals), 2)
        median = np.round(np.median(self.residuals), 2)
        min_value = round(min(self.residuals))
        max_value = round(max(self.residuals))
        plt.boxplot(self.residuals)
        plt.figtext(0,0,'Mean:{}\nMedian: {}\nMin value: {}\nMax Value: {}'.format(mean,median,min_value,max_value))
        plt.show()
     

