
with open("Data/inputDay06.txt") as f:
    rawData = f.read().splitlines()

def convert_raw_to_grouped_list(input_list:list):
    counter = 1
    GroupList = list(list())
    for line in input_list:
        if line == "":
            counter = counter +1
        if len(GroupList )< counter:
            GroupList.append(line)
        else:
            GroupList[counter - 1] = GroupList[counter - 1] + " "+ line
    return GroupList

def dedup_string(input_string:str):
    input_string= input_string.replace(" ", "")
    return "".join(set(input_string))

def get_string_length(input_string:str):
    return len(input_string)

# PART 1
group_list= convert_raw_to_grouped_list(rawData)
sortened_list= list(map(dedup_string,group_list))
length_list= list(map(get_string_length,sortened_list))
print(sum(length_list))


# PART 2

def count_common_letters(input_string:str):
    input_string=input_string.strip()
    parts = input_string.split(" ")
    if len(parts)==1:
        return len(parts[0])
    intersect = set(parts[1]).intersection(set(parts[0]))
    for i in range(2,len(parts)):
        part= parts[i]
        intersect = intersect.intersection(set(parts[i]))
    return len(intersect)

every_one_list= list(map(count_common_letters,group_list))
print(sum(every_one_list))

