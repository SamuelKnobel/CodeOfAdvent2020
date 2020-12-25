import pandas as pd
with open("Data/inputDay12.txt") as f:
#with open("Data/inputDay12_test.txt") as f:
    rawData = f.read().splitlines()
    tuple_list= [(dir[:1],dir[1:]) for dir in rawData]


df= pd.DataFrame(tuple_list, columns =['direction', 'value'])
df["facing_direction"] = 90 # direction East
df["value"] = pd.to_numeric(df["value"])
df['newDirection'] = df['direction']

# calculate the facing directions
for i in df.index:
    if df.at[i, 'direction'] == "L":
        df.at[i, 'facing_direction'] = (df.at[i-1, 'facing_direction']-df.at[i, 'value']) % 360
    elif df.at[i, 'direction'] == "R":
        df.at[i, 'facing_direction'] = (df.at[i-1, 'facing_direction'] + df.at[i, 'value']) % 360
    else:
        if i>0:
            df.at[i, 'facing_direction'] = df.at[i-1, 'facing_direction']
        else:
            df.at[i, 'facing_direction'] = 90

    if df.at[i,'direction'] == "F":
        if df.at[i, 'facing_direction'] == 0:
            df.at[i, 'newDirection'] = 'N'
        elif df.at[i, 'facing_direction'] == 90:
            df.at[i, 'newDirection'] = 'E'
        elif df.at[i, 'facing_direction'] == 180:
            df.at[i, 'newDirection'] = 'S'
        elif df.at[i, 'facing_direction'] == 270:
            df.at[i, 'newDirection'] = 'W'

    if df.at[i,'newDirection'] == "S":
        df.at[i, 'newDirection'] = "N"
        df.at[i, 'value'] = -df.at[i, 'value']
    if df.at[i,'newDirection'] == "W":
        df.at[i, 'newDirection'] = "E"
        df.at[i, 'value'] = -df.at[i, 'value']

m1 =df[df['newDirection']=='E']['value'].sum()
m2= df[df['newDirection']=='N']['value'].sum()
print(m1)
print(m2)
print(abs(m1)+abs(m2))

