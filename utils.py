import numpy as np
from collections import Counter

class Utils:
    def __init__(self):
        pass

    def round(self, number, places):
        return round(number, places)

    def roundArray(self, array, places):
        return np.around(array, decimals=places)