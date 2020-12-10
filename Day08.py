
testData= 'nop +0\n\
acc +1\n\
jmp +4\n\
acc +3\n\
jmp -3\n\
acc -99\n\
acc +1\n\
jmp -4\n\
acc +6'
testData=testData.splitlines()



def action_acc(current_acc:int, number_to_add:int):
    return current_acc+number_to_add

def action_jmp(current_index:int, number_to_add:int):
    return current_index + number_to_add

def action_nop(current_index:int):
    return current_index +1


def pars_line(input_str:str, current_line:int, current_acc:int):
    parts= input_str.split(" ")
    number= int(parts[1])
    action_type= parts[0]

    new_acc= current_acc
    if action_type =="nop":
        new_line= action_nop(current_line)

    elif action_type =="jmp":
        new_line= action_jmp(current_line,number)

    elif action_type =="acc":
        new_acc= action_acc(current_acc,number)
        new_line= action_nop(current_line)

    return (new_line, new_acc)



with open("Data/inputDay08.txt") as f:
    rawData = f.read().splitlines()


visited_index = []
line_index = 0
accumulator= 0
while line_index not in visited_index:

    (new_index,accumulator)= pars_line(rawData[line_index],line_index,accumulator)
    if new_index in visited_index:
        print(f'accumulator: {accumulator}')
        print(f'line: {line_index}')
        break
    else:
        visited_index.append(line_index)
        line_index= new_index

#Part 2

#rawData=testData
visited_index = []
line_index = 0
accumulator= 0
changable_Data= rawData.copy()
for l_inx in range(len(rawData)):
    visited_index = []
    line_index = 0
    accumulator = 0
    changable_Data = rawData.copy()
    parts= changable_Data[l_inx].split(" ")
    number= int(parts[1])
    action_type= parts[0]
    if action_type =='acc': continue

    #print(f'line to change:{changable_Data[l_inx]}, {l_inx}')
    if action_type =='jmp':
        changable_Data[l_inx]=changable_Data[l_inx].replace('jmp','nop')
    elif action_type =='nop':
        changable_Data[l_inx]=changable_Data[l_inx].replace('nop','jmp')
    #print(f'Old:{rawData[l_inx]}, new:{changable_Data[l_inx]} ')

    while line_index not in visited_index:
        (new_index,accumulator)= pars_line(changable_Data[line_index],line_index,accumulator)
        if new_index in visited_index:
            #print("loop reached")
            #print(f'accumulator: {accumulator}')
            #print(f'line: {line_index}\n')
            break
        else:
            visited_index.append(line_index)
            line_index= new_index

        if line_index >= len(changable_Data):
            print(f'accumulator: {accumulator}')
            print(f'line: {line_index}')
            print("end reached")
            break

        #print(f'accumulator: {accumulator}')
        #print(f'line: {line_index}')




