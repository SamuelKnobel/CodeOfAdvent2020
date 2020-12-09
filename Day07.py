
def get_outer_bags(input_string:str):
    str_split = input_string.split(" ")
    return " ".join(str_split[0:2])


def get_inner_bags(input_string:str):
    str_split = input_string.split(" ")
    return " ".join(str_split[2:])

with open("Data/inputDay07.txt") as f:
    rawData = f.read().splitlines()

target_bags = ['shiny gold']

outer_bags= list(map(get_outer_bags,rawData))
inner_bags= list(map(get_inner_bags,rawData))

containing_Bags= []
bags_to_check = target_bags
while len(bags_to_check)>0:
    new_bags=[]
    for bag_idx in range(len(inner_bags)):
        for target_bag in bags_to_check:
            if target_bag in inner_bags[bag_idx]:
                new_bags.append(outer_bags[bag_idx])
                containing_Bags.append(outer_bags[bag_idx])
    bags_to_check= new_bags

print(len(set(containing_Bags)))


# PART 2



# New Approach
import re
import numpy as np
Data= rawData.copy()

for l in range(len(Data)):
    short_line = Data[l].split(" ")
    Data[l] = " ".join(short_line[0:2]) + " " + " ".join(short_line[4:])
    Data[l] = Data[l].replace(" bags","")
    Data[l] = Data[l].replace(" bag", "")
    Data[l] = Data[l].replace(".", "")

bag_dict= {}
solved_bags = []
for line in Data:
    i = get_inner_bags(line)
    o = get_outer_bags(line)
    if "no other" in i:
        i="0"
        solved_bags.append(o)
    bag_dict[o] = i

while len(solved_bags)< len(bag_dict):
    for line in Data:
        i = get_inner_bags(line)
        o = get_outer_bags(line)
        for solved in solved_bags:
            if solved in i:
                bag_dict[o]=bag_dict[o].replace(solved,bag_dict[solved])
                try:
                    n= int(bag_dict[o])
                    continue
                except:
                    if len(bag_dict[o])<3:
                        continue
                    if not re.search('[a-zA-Z]', bag_dict[o]):
                        numbers = bag_dict[o].split(", ")
                        result=0
                        for number in numbers:
                            single_number = number.split(" ")
                            result = result+ int(single_number[0]) + int(single_number[0])*int(single_number[1])
                        bag_dict[o]= str(result)
                        solved_bags.append(o)





bag_dict['shiny gold']







for d in rawData:
    if "shiny gold" in d:
        print(d)