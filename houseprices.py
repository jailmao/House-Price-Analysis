import pandas as pd
import xlrd
import numpy as np
file_path = "Houseprices.xls"
prices = pd.read_excel(file_path, sheet_name="1a", skiprows=5)
names = pd.read_csv("MsoaNames.csv", usecols=["MSOA21CD", "MSOA21NM", "WD23NM"])
print("Enter an area")
query=input()
code=names.loc[names["WD23NM"]==query]["MSOA21CD"].reset_index(drop=True)
areaPrices=[]
for i in range(len(code)):
    areaPrices.append(prices.loc[prices["MSOA code"]==code[i]])

print(areaPrices)

