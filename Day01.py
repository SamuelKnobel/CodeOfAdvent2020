import pandas as pd


data = pd.read_table("Data/inputDay1.txt",header=None)
bigger = data[0][data[0]>1010]
smaller = data[0][data[0]<=1010]

solution = [(x * y) for x in bigger for y in smaller if x+y ==2020]
print(solution)
