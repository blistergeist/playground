import os
import pandas as pd

os.chdir('C:\\Users\\mallison\\Documents\\Tek\\zInteractionLogs\\AE Interaction Logs 2017')
files = (os.listdir('.'))

oFileName = 'C:\\Users\\mallison\\Documents\\Tek\\zInteractionLogs\\AE Interaction Logs 2017\\AE Interaction Log 3.0 - Allison - AP1704.xlsx'
aFileName = oFileName

original = pd.ExcelFile(oFileName)
append = pd.ExcelFile(aFileName)

print(original.sheet_names)

df1 = original.parse(original.sheet_names[0])