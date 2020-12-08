
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
outer_bags= list(map(get_outer_bags,rawData))
inner_bags= list(map(get_inner_bags,rawData))

def find_number_of_bags_inside(input_string:str, data=rawData):
    outer = list(map(get_outer_bags, data))
    inner = list(map(get_inner_bags, data))
    for idx in range(len(outer)):
        if input_string in outer[idx]:
            parts = inner[idx].split(" ")
            return (parts[0]," ".join(parts[1:3]))
    return None



# New Approach
import re

Data = 'light red bags contain 1 bright white bag, 2 muted yellow bags.\n\
dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n\
bright white bags contain 1 shiny gold bag.\n\
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n\
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n\
dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n\
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n\
faded blue bags contain no other bags.\n\
dotted black bags contain no other bags.'

Data= Data.splitlines()

Data="shiny gold bags contain 2 dark red bags.\n\
dark red bags contain 2 dark orange bags.\n\
dark orange bags contain 2 dark yellow bags.\n\
dark yellow bags contain 2 dark green bags.\n\
dark green bags contain 2 dark blue bags.\n\
dark blue bags contain 2 dark violet bags.\n\
dark violet bags contain no other bags."
Data= Data.splitlines()

Data= rawData.copy()

for l in range(len(Data)):
    short_line = Data[l].split(" ")
    Data[l] = " ".join(short_line[0:2]) + " " + " ".join(short_line[4:])

elements_to_update =[]
lines_to_delete =[]

replacer = []
counter=0
bagcounter=[]
while "shiny gold" not in elements_to_update:

    for l in lines_to_delete:
        Data.remove(l)

    for idx in range(len(Data)):
        for e in range(len(elements_to_update)):
            if elements_to_update[e] in Data[idx]:
                i = get_inner_bags(Data[idx])
                o = get_outer_bags(Data[idx])
                line_split= i.split(",")
                new_line = []
                for part in line_split:
                    if elements_to_update[e] in part.strip():
                        new_line.append(part.strip().split(" ")[0] + " " + replacer[e])
                    else:
                        new_line.append(part.strip())
                Data[idx] = o+" "+ ",".join(new_line)
                print(o+" "+ ",".join(new_line))

    lines_to_delete =[]
    elements_to_update =[]
    replacer= []

    for bag_line in Data:
        inner = get_inner_bags(bag_line)
        outer = get_outer_bags(bag_line)
        if "no other bag" in inner:
            lines_to_delete.append(bag_line)
            elements_to_update.append(outer)
            replacer.append("1")
        elif "bags" not in inner and "bag" not in inner:
            lines_to_delete.append(bag_line)
            elements_to_update.append(outer)
            dif_numbs= []
            diff_bags= inner.split(",")
            for b in diff_bags:
                if len(b)<2:
                    continue
                numbers = b.strip().split(" ")[0:2]

                dif_numbs.append(int(re.search(r'\d+', numbers[0])[0])*int(re.search(r'\d+', numbers[1])[0]))

            replacer.append(str(sum(dif_numbs)))


#To low...6596

for d in Data:
    if "shiny gold" in d:
        print(d)

for d in rawData:
    if "shiny gold" in d:
        print(d)