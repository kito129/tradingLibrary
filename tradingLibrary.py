from report import Report
from statistics import Statistics
from utils import Utils

class TradingLibrary:

    def __init__(self):
        self.report = Report()
        self.statistics = Statistics()
        self.utils = Utils()
        pass



# to test functions
testLibrary = TradingLibrary()

a = [1356.958,2.5251,3.68588,-58,-255.8]

# test report
print(testLibrary.report.pnl(a))

# test statistics
print(testLibrary.statistics.basicDataArray(a))

# test utils
print(testLibrary.utils.roundArray(a,2))