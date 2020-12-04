import pandas as pd

# PART 1
data = pd.read_table("Data/inputDay01.txt",header=None)
bigger = data[0][data[0]>1010]
smaller = data[0][data[0]<=1010]

solution = [(x * y) for x in data[0] for y in data[0] if x+y ==2020]
print(solution)

# PART 2
solution = [(x , y, z) for z in data[0] for x in data[0] for y in data[0] if x+y+z ==2020 ]
print(solution)
solution = [(x * y* z) for z in data[0] for x in data[0] for y in data[0] if x+y+z ==2020 and x!=y and y!= z and z!= x ]
print(solution)