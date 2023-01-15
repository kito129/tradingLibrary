# tradingLibrary

A library of functions for use in trading projects.

## Features
- Ultra-fast performance
- Well-documented code
- Wide range of trading-related functions

## Installation

You can install the tradingLibrary package by using the following command:

  pip install tradingLibrary
  

## Usage

You can import the tradingLibrary package and use its functions like this:
```python
fromt tradingLibrary import TradingLibrary

# to test functions
testLibrary = TradingLibrary()

a = [1356.958,2.5251,3.68588,-58,-255.8]

# test report
print(testLibrary.report.pnl(a))

# test statistics
print(testLibrary.statistics.basicDataArray(a))

# test utils
print(testLibrary.utils.roundArray(a,2))



