

def calc_paris(start_index:int, data:list):
    if start_index<25:
        return None
    else:
        pairs= []
        elements_to_make_pairs= data[start_index-25:start_index]
        for element1 in elements_to_make_pairs:
            for element2 in elements_to_make_pairs:
                if element1 != element2:
                    #print(element1+element2)
                    pairs.append(element1+element2)
        return pairs

with open("Data/inputDay09.txt") as f:
    rawData = f.read().splitlines()
raw_list = list(map(int, rawData))

for l_idx in range(len(raw_list)):
    pairs= calc_paris(l_idx,raw_list)
    if pairs== None or raw_list[l_idx] in pairs:
        continue
    else:
        print(l_idx)
        print(raw_list[l_idx])
        break

# PART 2
#testset='35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'
#testset=testset.splitlines()
#raw_list = list(map(int, testset))




invalidNumber= 167829540
#invalidNumber= 127
summ=0
number_of_elements_to_sum_up=2
while summ != invalidNumber and number_of_elements_to_sum_up< len(raw_list):
    summ = 0
    for l_idx in range(len(raw_list)-number_of_elements_to_sum_up):
        elements_to_sum_up= raw_list[l_idx:l_idx+number_of_elements_to_sum_up]
        summ = sum(elements_to_sum_up)
        if  summ!= invalidNumber:
            continue
        else:
            print("found")
            print(len(elements_to_sum_up))
            print(elements_to_sum_up[0])
            print(elements_to_sum_up[len(elements_to_sum_up)-1])
            print(min(elements_to_sum_up)+max(elements_to_sum_up))

            break
    number_of_elements_to_sum_up= number_of_elements_to_sum_up+1








