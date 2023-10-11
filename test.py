import pandas as pd

sensorData = pd.read_csv(r"C:\Users\einar\Nordlys\pythonMDF2SCV\mdf2csv\mdf2csv\data-processing\output_joined.csv")

"""
The function under is meant to look for values outside a given range, constrained by expectedMin and expectedMax.
It looks in a given row of a dataframe for values outside this range. If it finds values outside the range, it
remembers the index of these values, and uses these indexes to compare the values outside the range with the 
associated values in another column (comparisonRow), and returns a dictionary with the associated values as keys
and the value itself as the value. The comparisonRow can use any row, but is most likely to be used for comparing
with timestamps.
"""

def valuesOutsideRange(investigatedRow: str, comparisonRow: str, expectedMin : "Lowest end of range", expectedMax : "Highest end of range") -> dict:
    dic = {}

    investigatedValues = [value for value in enumerate(sensorData[investigatedRow]) if (float(value[1]) < expectedMin) or (float(value[1]) > expectedMax)] 
    comparisonRowValues = [sensorData[comparisonRow][value[0]] for value in investigatedValues]

    for investigatedValue, comparisonrowValue in zip(investigatedValues, comparisonRowValues):
        dic[comparisonrowValue] = investigatedValue[1]
        
    return dic
    
def findSpecialValues(specialValue: tuple, investigatedRow: str, comparisonRow: str):
    dic = {}

    investigatedValues = [value for value in specialValue if sensorData[(sensorData['S1_PID_42_ControlModuleVolt'] == value)].index.values] 
    comparisonRowValues = [value for value in investigatedValues]
    print(investigatedValues)

    return dic

print(findSpecialValues((12.675, 14.324, 0.5), 'S1_PID_42_ControlModuleVolt', "TimeStamp"))
