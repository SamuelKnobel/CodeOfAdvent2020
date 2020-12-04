import pandas as pd
import numpy as np

def lineParser(inputString: str):
    policy, pw = inputString.split(":")
    numbers, letter = policy.split(" ")
    lower, upper = numbers.split('-')
    return {"lower": lower, "upper": upper, "letter": letter, "pw": pw}


# PART 1
data = pd.read_table("Data/inputDay02.txt", header=None)
df = pd.DataFrame(map(lineParser, data[0]))
countArray = [df["pw"][lineIndex].count(df["letter"][lineIndex]) for lineIndex in range(len(df["pw"]))]
df['valid_Part1'] = (countArray<= df['upper'].values.astype(np.int)) & (countArray>= df['lower'].values.astype(np.int))

print(len(df['valid_Part1'][df['valid_Part1']== True]))


# PART 2
df["FirstLetter"] =[df["pw"][lineIndex][int(df["lower"][lineIndex])]== df['letter'][lineIndex] for lineIndex in range(len(df["pw"]))]
df["SecondLetter"] =[df["pw"][lineIndex][int(df["upper"][lineIndex])]== df['letter'][lineIndex] for lineIndex in range(len(df["pw"]))]

df["valid_Part2"]=np.logical_xor(df["SecondLetter"].values,df["FirstLetter"].values)
print(len(df['valid_Part2'][df['valid_Part2']== True]))



