import numpy as np
from collections import Counter
from utils import Utils

class Statistics:
    def __init__(self):
        self.utils = Utils()
        pass

    def basicDataArray(self, array):
        avg = np.mean(array)
        stdev = np.std(array)
        mode = Counter(array).most_common(1)[0][0]
        max_value = np.max(array)
        min_value = np.min(array)
        max_frequency = Counter(array).most_common(1)[0][1]
        sum_value = np.sum(array)
        return {
            'average': self.utils.round(avg,3),
            'standard deviation': self.utils.round(stdev,3), 
            'mode': self.utils.round(mode,3), 
            'max value': self.utils.round(max_value,3), 
            'min value': self.utils.round(min_value,3), 
            'max frequency': self.utils.round(max_frequency,3), 
            'sum': self.utils.round(sum_value,3)
            }