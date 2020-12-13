#with open("Data/inputDay10_test.txt") as f:

#with open("Data/inputDay10_test2.txt") as f:
with open("Data/inputDay10.txt") as f:
    rawData = f.read().splitlines()
raw_list = list(map(int, rawData))
raw_list.append(0)
raw_list.append(max(raw_list)+3)

sorted_list = raw_list.copy()
sorted_list.sort()



difference = []
zip_object = zip(sorted_list[1:], sorted_list[:-1])
for list1_i, list2_i in zip_object:
    difference.append(list1_i-list2_i)

one_count=0
three_count=0
difflist = difference
for number in difflist:
    if number==3:
        three_count= three_count+1
    elif number==1:
        one_count= one_count+1
print(f'number of 3: {three_count}')
print(f'number of 1: {one_count}')
print(f'Result Part1: {one_count*three_count}')

# Part 2
# Find the number and length of the snippets of consecutive ones.


counter= 0
nb_of_ones=0
GroupList = list()
for number in difflist:
    if number == 1:
        nb_of_ones= nb_of_ones+1
    elif number==3:
        GroupList.append(nb_of_ones)
        nb_of_ones=0
        counter = counter + 1
        continue



four_count=0
three_count=0
two_count=0

for number in GroupList:
    if number==3:
        three_count= three_count+1
    elif number==2:
        two_count= two_count+1
    elif number==4:
        four_count= four_count+1
print(f'number of 2: {two_count}')
print(f'number of 3: {three_count}')
print(f'number of 4: {four_count}')

print(f'Result Part1: {2**two_count*4**three_count*7**four_count}')
