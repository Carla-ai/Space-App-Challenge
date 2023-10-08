#A program to sort csv file
import pandas as pd

#importing database
data = pd.read_csv('./mdb.csv')

#Sorting value
mass = 0.0042

#counter variable
c = 0

#loop to find how many planets have below the sorted value mass
for i in data["Mass"]:
  if(i<=mass):
    c = c+1

#Finally displaying the count
print(f"Count: {c}")
