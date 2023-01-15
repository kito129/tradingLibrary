import numpy as np

class Report:
    def __init__(self):
        pass

    #Return the Pnl from and array of number, example trade pl
    #IN: Get an array of number as 
    #OUT:
    def pnl(self, array):
        arr = np.array(array)
        return np.sum(arr)