
def get_outer_bags(input_string:str):
    str_split = input_string.split(" ")
    return " ".join(str_split[0:2])


def get_inner_bags(input_string:str):
    str_split = input_string.split(" ")
    return " ".join(str_split[4:])

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
containing_Bags= []
bags_to_check = target_bags
number_of_new_bags=[]
while len(bags_to_check)>0:
    new_bags=[]
    for bag_idx in range(len(inner_bags)):
        for target_bag in bags_to_check:
            if target_bag in outer_bags[bag_idx]:
                sub_bags= inner_bags[bag_idx].split(", ")
                if len(sub_bags)==1:
                    if len(sub_bags[0].split(" "))==3: # no other bags
                        print("no further bags in " + target_bag)
                        continue
                    else:
                        bag_color = sub_bags[0].split(' ')
                        new_bags.append(" ".join(bag_color[1:3]))
                else:
                    for bag in sub_bags:
                        bag_color = bag.split(' ')
                        new_bags.append(" ".join(bag_color[1:3]))
                number_of_new_bags.append(sum([int(s) for s in inner_bags[bag_idx].split() if s.isdigit()]))

    bags_to_check= set(new_bags)


# New Approach

def find_number_of_bags_inside(input_string:str):
    outer_bags = list(map(get_outer_bags, rawData))
    inner_bags = list(map(get_inner_bags, rawData))

    for bag_idx in range(len(outer_bags)):
        if target_bag in outer_bags[bag_idx]:
            return inner_bags[bag_idx]



