
import copy

with open("Data/inputDay11.txt") as f:
    rawData = f.read().splitlines()
    position_array = [list(line) for line in rawData]

def getNeighbours(line: int, position: int, fullarray):
    small_array= []
    start_line = line-1
    end_line = line+2
    start_pos = position-1
    end_pos = position+2

    if line-1<0:
        start_line=0
    if line+1 > len(fullarray)-1:
        end_line = len(fullarray)
    if position - 1 < 0:
        start_pos = 0
    if position + 1 > len(fullarray[0]) - 1:
        end_pos = len(fullarray[0])

    for l in range(start_line, end_line):
        small_array.append(fullarray[l][start_pos:end_pos])
    return (small_array,fullarray[line][position])

def count_empy_full(small_array, center_str):
    longstring= ''.join([''.join(t) for t in (small_array)])
    if  center_str=="L":
        return (longstring.count("L")-1,longstring.count("#"))
    elif center_str =="#":
        return (longstring.count("L"),longstring.count("#")-1)
    elif center_str == ".":
        return (None,None)
    else:
        return (longstring.count("L"),longstring.count("#"))

next_position_array=  copy.deepcopy(position_array)


while previous_position_array != next_position_array:
    previous_position_array = copy.deepcopy(next_position_array)
    for line_idx in range(len(previous_position_array)):
        line= previous_position_array[line_idx]
        for row_idx in range(len(line)):
            row= line[row_idx]
            target= previous_position_array[line_idx][row_idx]
            neighbours= getNeighbours(line_idx, row_idx,previous_position_array)
            (L_count, Hash_count)= count_empy_full(neighbours[0],neighbours[1])
            if  target ==".":
                continue
            elif target == "L":
                if Hash_count ==0 :
                    next_position_array[line_idx][row_idx] = "#"
            elif target == "#":
                if Hash_count >=4 :
                    next_position_array[line_idx][row_idx] = "L"

count_empy_full(previous_position_array," ")


import matplotlib.pyplot as plt

for line_idx in range(len(position_array)):
    line = position_array[line_idx]
    for row_idx in range(len(line)):
        row = line[row_idx]
        target= position_array[line_idx][row_idx]
        if  target ==".":
            plt.plot(line_idx,row_idx,'ro')
        elif target == "L":
            plt.plot(line_idx,row_idx,'go')
        elif target == "#":
            plt.plot(line_idx,row_idx,'bo')

plt.show()


# --- Part Two ---
def check_left_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if position <= 0:
        neigbour_exists= False
    else:
        pos_index=position-1
        while pos_index>=0:
            n = fullarray[line][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                pos_index = pos_index-1
    return neigbour_exists

def check_right_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if position >= len(fullarray[0])-1:
        neigbour_exists= False
    else:
        pos_index=position+1
        while pos_index<=len(fullarray[0])-1:
            n = fullarray[line][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                pos_index = pos_index+1
    return neigbour_exists

def check_bottom_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line >= len(fullarray)-1:
        neigbour_exists= False
    else:
        line_index=line+1
        while line_index<=len(fullarray)-1:
            n = fullarray[line_index][position]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index+1
    return neigbour_exists

def check_top_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line <=0 :
        neigbour_exists= False
    else:
        line_index=line-1
        while line_index>=0:
            n = fullarray[line_index][position]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index-1
    return neigbour_exists

def check_top_left_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line <=0 or position<=0 :
        neigbour_exists= False
    else:
        line_index=line-1
        pos_index= position-1
        while line_index>=0 and pos_index >= 0:
            n = fullarray[line_index][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index-1
                pos_index=pos_index-1
    return neigbour_exists

def check_bottom_left_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line >=len(fullarray)-1 or position<=0 :
        neigbour_exists= False
    else:
        line_index=line+1
        pos_index= position-1
        while line_index<=len(fullarray)-1 and pos_index >= 0:
            n = fullarray[line_index][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index+1
                pos_index=pos_index-1
    return neigbour_exists

def check_bottom_right_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line >=len(fullarray)-1 or position>=len(fullarray[0])-1 :
        neigbour_exists= False
    else:
        line_index=line+1
        pos_index= position+1
        while line_index<=len(fullarray)-1 and pos_index<=len(fullarray[0])-1 :
            n = fullarray[line_index][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index+1
                pos_index=pos_index+1
    return neigbour_exists

def check_top_right_neighbour(line: int, position: int, fullarray):
    neigbour_exists = False
    if line <=0 or position>=len(fullarray[0])-1 :
        neigbour_exists= False
    else:
        line_index=line-1
        pos_index= position+1
        while line_index>=0 and pos_index<=len(fullarray[0])-1 :
            n = fullarray[line_index][pos_index]
            if n == "#":
                neigbour_exists= True
                break
            elif n == "L":
                neigbour_exists = False
                break
            else:
                line_index=line_index-1
                pos_index=pos_index+1
    return neigbour_exists

def count_all_neighbours(line: int, position: int, fullarray):
    left = check_left_neighbour(line, position, fullarray)
    right = check_right_neighbour(line, position, fullarray)
    top = check_top_neighbour(line, position, fullarray)
    bottom = check_bottom_neighbour(line, position, fullarray)
    tl = check_top_left_neighbour(line, position, fullarray)
    tr = check_top_right_neighbour(line, position, fullarray)
    br = check_bottom_right_neighbour(line, position, fullarray)
    bl = check_bottom_left_neighbour(line, position, fullarray)
    total = int(left) + int(right) + int(top) + int(bottom) + int(tl) + int(tr) + int(br) + int(bl)
    return total



next_position_array=  copy.deepcopy(position_array)

while previous_position_array != next_position_array:
    previous_position_array = copy.deepcopy(next_position_array)
    for line_idx in range(len(previous_position_array)):
        line= previous_position_array[line_idx]
        for row_idx in range(len(line)):
            row= line[row_idx]
            target= previous_position_array[line_idx][row_idx]
            Hash_count= count_all_neighbours(line_idx,row_idx,previous_position_array)
            if target == ".":
                continue
            elif target == "L":
                if Hash_count ==0 :
                    next_position_array[line_idx][row_idx] = "#"
            elif target == "#":
                if Hash_count >=5 :
                    next_position_array[line_idx][row_idx] = "L"

count_empy_full(previous_position_array," ")

array_to_plot= next_position_array
for line_idx in range(len(array_to_plot)):
    line = array_to_plot[line_idx]
    for row_idx in range(len(line)):
        row = line[row_idx]
        target= array_to_plot[line_idx][row_idx]
        if  target ==".":
            plt.plot(line_idx,row_idx,'ro')
        elif target == "L":
            plt.plot(line_idx,row_idx,'go')
        elif target == "#":
            plt.plot(line_idx,row_idx,'bo')

plt.show()