import numpy as np
import pandas as pd
import re

# import the data
df = pd.read_csv("ITEM MASTER DIRECT EXCEL.csv")

# data manipulation
x = df["OEMCode"].str.split(",")

# create the two columns
# BBH Code
# check for BBH code in 1st row
import re
bbh_code = list()
for k in range(x.shape[0]):
    for l in range(len(x[k])):
        bbh = x[k][l].strip()
        val = ""
        if re.findall("\AB", bbh):
            val = bbh
            break
    bbh_code.append(val)
        
df["BBH Code"] = bbh_code

# ISBN
# check the lenght of list equals to 1
isbn = list()
for n in x:
    if len(n) == 1:
        isbn.append(n[0])
    elif re.findall("\ABBH", n[0]):
        isbn.append(n[1])
    else:
        isbn.append(n[0])
        
df["ISBN"] = isbn

ean1 = list()
ean2 = list()
ean3 = list()
for n in x:
    if len(n) == 3:
        ean1.append(n[0])
        ean2.append(n[1])
        ean3.append(n[2])
    elif len(n) == 2:
        ean1.append(n[0])
        ean2.append(n[1])
        ean3.append("")
    else:
        ean1.append(n[0])
        ean2.append("")
        ean3.append("")



# reorder the data
item_master = pd.DataFrame()
item_master["Category"] = df["Category"]
item_master["Product Group"] = df["Product Group"]
item_master["Item Code"] = df["Item Code"]
item_master["Item Name"] = df["Item Name"]
item_master["OEMCode"] = df["OEMCode"]
item_master["EAN 1"] = ean1
item_master["EAN 2"] = ean2
item_master["EAN 3"] = ean3
item_master["BBH Code"] = df["BBH Code"]
item_master["ISBN"] = df["ISBN"]
item_master["HSNCode"] = df["HSNCode"]
item_master["Brand"] = df["Brand"]
item_master["Size"] = df["Size"]
item_master["RSP"] = df["RSP"]
item_master["MRP"] = df["MRP"]
item_master["OSP"] = df["OSP"]
item_master["Vendor"] = df["Vendor"]
item_master["CreateDate"] = df["CreateDate"]
item_master["LastModifiedDate"] = df["LastModifiedDate"]
item_master["GST%"] = df["GST%"]
item_master["CESS"] = df["CESS"]

# export the csv file
item_master.to_csv("output.csv", index=False)
