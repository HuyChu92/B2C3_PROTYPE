import math
import numpy as np
import math
from sklearn.metrics import r2_score, mean_squared_error


class ErrorRegression:
    def __init__(self,actual,predicted):
        self.actual = actual
        self.predicted = predicted
        self.r2 = self.rootsquaredBerekenen()
        self.rmse = self.rmseBerekenen()
        
    def rootsquaredBerekenen(self):
        rootsquared = round(r2_score(self.actual,self.predicted),2)
        return rootsquared

    def rmseBerekenen(self):
        rmse = mean_squared_error(self.actual, self.predicted, squared=False)
        return rmse
