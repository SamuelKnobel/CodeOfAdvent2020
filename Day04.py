
import re

with open("Data/inputDay04.txt") as f:
    rawData = f.read().splitlines()

counter = 1
subjectList = list(list())
for line in rawData:
    if line == "":
        counter = counter +1
    if len(subjectList )< counter:
        subjectList.append(line)
    else:
        subjectList[counter - 1] = subjectList[counter - 1] + " " + line

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validSubjectList_P1= []
for subject in subjectList:
    if all(x in subject for x in requiredFields):
        validSubjectList_P1.append(subject)
print(len(validSubjectList_P1))


def get_field_string(input_string: str, target_string: str):
    parts = input_string.split(" ")
    for i in parts:
        if target_string in i:
            return i
        else:
            continue
    return  None

def check_range(input_string:str, min:int, max:int):
    number = int(input_string)
    if number >= min and number <= max:
        return  True
    else:
        return  False


def check_birth_year(input_string: str):
    byr_string= get_field_string(input_string,'byr')
    byr_number = byr_string.split(':')[1]
    return check_range(byr_number,1920,2002)

def check_issue_year(input_string: str):
    iyr_string= get_field_string(input_string,'iyr')
    iyr_number = iyr_string.split(':')[1]
    return check_range(iyr_number,2010,2020)

def check_expir_year(input_string: str):
    eyr_string= get_field_string(input_string,'eyr')
    eyr_number = eyr_string.split(':')[1]
    return check_range(eyr_number,2020,2030)

def check_height(input_string: str):
    height_string= get_field_string(input_string,'hgt')
    if "in" in height_string:
        height_number = height_string[:-2].split(':')[1]
        return check_range(height_number,59,76)
    elif "cm" in height_string:
        height_number = height_string[:-2].split(':')[1]
        return check_range(height_number, 150, 193)
    else:
        return False

def check_hair_color(input_string: str):
    hcl_string= get_field_string(input_string,'hcl')
    hcl_string = hcl_string.split(':')[1]
    if hcl_string[0] != "#":
        return  False
    elif len(hcl_string) != 7:
        return False
    else:
        return bool(re.match(r'.{6,6}',hcl_string[1:]))
        #return bool(re.match(r'[A-Za-z0-9]{6,6}', hcl_string[1:]))


def check_eye_color(input_string: str):
    ecl_string= get_field_string(input_string,'ecl')
    ecl_string = ecl_string.split(':')[1]
    if any(x in ecl_string for x in ['amb' ,'blu', 'brn', 'gry', 'grn' ,'hzl' ,'oth']):
        return True
    else:
        return False

def check_PID(input_string: str):
    pid_string = get_field_string(input_string, 'pid')
    pid_string = pid_string.split(':')[1]
    if  len(pid_string) != 9:
        return False
    print(pid_string)
    return bool(re.match(r'\d{9}', pid_string))


validSubjectList_P2= []
for subject in validSubjectList_P1:
    if (check_height(subject) and check_birth_year(subject) and check_issue_year(subject) and check_expir_year(subject)
            and check_hair_color(subject) and check_eye_color(subject) and check_PID(subject)):
        validSubjectList_P2.append(subject)
print(len(validSubjectList_P2))
