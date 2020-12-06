
with open("Data/inputDay05.txt") as f:
    rawData = f.read().splitlines()

def get_seat_ID(inputstring:str):
    lower = 1
    upper = 128
    left = 1
    right = 8
    for l in range(len(inputstring)):
        letter = inputstring[l]
        if letter == "B":
            lower = lower + 2 ** (7 - l - 1)
        elif letter == "F":
            upper = upper - 2 ** (7 - l - 1)
        elif letter == "R":
            left = left + 2 ** (10 - l - 1)
        elif letter == "L":
            right = right - 2 ** (10 - l - 1)

    SeatID = (upper - 1) * 8 + (right - 1)
    return SeatID

SeatIDs= list(map(get_seat_ID,rawData))
print(max(SeatIDs))

##PART2

import numpy as np

sortedList= SeatIDs
sortedList.sort()
result = (np.subtract(sortedList[:-1],sortedList[1:])).tolist()

print(result.index(min(result)))
sortedList[result.index(min(result)):result.index(min(result))+2]
my_seat= sortedList[result.index(min(result))]+1
print(my_seat)