import sys

with open('input-exemple.txt', 'r') as file:
    input = file.read()

brutRules, brutPages = input.strip().split('\n\n')
rules = [list(map(int, line.split('|'))) for line in brutRules.split('\n')]
linePages = [list(map(int, line.split(','))) for line in brutPages.split('\n')]

total = 0
dictionnaire= {}

def checkRules(page, splitPage, pages):
    countRules = 0
    validRules = 0
    for rule in rules:
        if page in rule: 
            if(rule[0] not in pages or rule[1] not in pages):
                continue
            else: 
                countRules += 1
            if(page == rule[0]):
                if page not in dictionnaire:
                    dictionnaire[page] = []
                if rule[1] not in dictionnaire[page]:
                    dictionnaire[page].append(rule[1]) 
                validRules += 1
            elif(page == rule[1] and rule[0] in splitPage):
                validRules += 1
            else:
                continue 
    if(countRules == validRules):
        return True
    else: 
        return False
    

def getCenterNumber(pages):
    index = len(pages) // 2
    return  pages[index]

def tri(update):
    for i in range (0, len(update)):
        for j in range (0, len(update)):
            print(f"i {i} / j {j}")
            if(update[j] in dictionnaire[update[i]]):
                print("good")
            else:
                update.insert(i, update.pop(j))
                i = 0
                j = 0
    return update


for pages in linePages:
    print(f"pages: {pages}")
    actualPages = 0
    for i, page in enumerate(pages):
        splitPage = pages[:i]
        result = checkRules(page, splitPage, pages)
        if (result is True):
            actualPages += 1

    if(actualPages != len(pages)):
        print(dictionnaire)
        newList = tri(pages);
        print(f"newList: {newList}")
        centerNumber = getCenterNumber(newList)
        print(f"--Valide / centerNumber {centerNumber} ")
        total += centerNumber
        dictionnaire = {}


print(f"total: {total}")    
