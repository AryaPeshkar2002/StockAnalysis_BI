import pandas as pd
import petl as etl
import numpy as np
import csv
import time
from petl import dateparser

db = pd.read_csv('transformed_data_temp.csv')
#print(db)
#print(db1)
table1 = [['Date','Turnover','P.E ratio','ShouldInvest'],
['26-05-2008','172637000000000','3.024','no'],
['27-05-2008','248837000000000','3.377','no'],
['28-05-2008','283753000000000','3.850','yes'],
['29-05-2008','298292000000000','3.799','yes'],
['30-05-2008','194593000000000','3.874','yes'],
['02-06-2008','150691000000000','4.113','yes'],
['03-06-2008','153108000000000','4.015','yes'],
['04-06-2008','170632000000000','3.562','yes'],
['06-06-2008','4.99433E+13','3.802','No'],
['10,09-06-2008','4.73958E+13','3.862','No'],
['10-06-2008','6.13897E+13','4.023','No'],
['11-06-2008','4.97503E+13','3.838','No']]
#table1 = [['Name','Sector','High'],
#[db1.head(15),db2.head(15),db3.head()]]'''

#table1 = [[]]

'''table2=etl.aggregate(table1,'Date',list)
print(table2)
print()
table3 = etl.aggregate(table1, key=None,aggregation=list, value=('P.E ratio', 'ShouldInvest'))
print(table3)
print()
table4 = etl.aggregate(table1, key=('ShouldInvest', 'Date'),aggregation=list, value=('Date', 'P.E ratio'))
print(table4)'''

#Slicing
table_temp1 = [['Date','ShouldInvest'],
['26-05-2008','no'],
['27-05-2008','no'],
['28-05-2008','yes'],
['29-05-2008','yes'],
['30-05-2008','yes'],
['02-06-2008','yes'],
['03-06-2008','yes'],
['04-06-2008','yes']]
table_temp2 = [['BrokerID'],
['AB12'],
['LW34'],
['AP56'],
['YR78'],
['NP90'],]

#print(table_temp[1:])

print("SLICING")
table5 = etl.annex(table_temp2,table_temp1)
print(table5)
print()
#DICING
table_temp3 = [['Date','P.E ratio','ShouldInvest'],
['26-05-2008','3.024','no'],
['27-05-2008','3.377','no'],
['28-05-2008','3.850','yes'],
['29-05-2008','3.799','yes'],
['30-05-2008','3.874','yes'],]
print("DRILL DOWN")
table6 = etl.annex(table_temp2,table_temp3)
print(table6)
print()


#DICING
print("DICING")
table6 = db.head(25)
print(table6)

'''table_temp4 = [['Date','P.E ratio','Year'],
['27-05-2008','3.377','2008'],
['28-05-2008','3.85','2008'],
['02-06-2008','4.113','2008'],
['03-06-2008','4.015','2008'],
['07-07-2008','3.101','2008'],
['08-07-2008','3.072','2008'],
['14-08-2008','3.173','2008']]
print("ROLL UP")
table7 = etl.annex(table_temp2,table_temp4)
print(table7)
print()'''


