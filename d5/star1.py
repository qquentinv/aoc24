with open('input.txt', 'r') as file:
    input = file.read()

brutRules, brutPages = input.strip().split('\n\n')
rules = [list(map(int, line.split('|'))) for line in brutRules.split('\n')]
linePages = [list(map(int, line.split(','))) for line in brutPages.split('\n')]

total = 0

def checkRules(page, splitPage, pages):
    countRules = 0
    validRules = 0
    for rule in rules:
        print(f"rule: {rule}")
        if page in rule: 
            if(rule[0] not in pages or rule[1] not in pages):
                continue
            else: 
                countRules += 1
            if(page == rule[0]):
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

for pages in linePages:
    print(f"pages: {pages}")
    actualPages = 0
    for i, page in enumerate(pages):
        print(f"actuelPage: {page}")
        splitPage = pages[:i]
        print(f"splitPage: {splitPage}")
        result = checkRules(page, splitPage, pages)
        print(f"result: {result}")
        if (result is True):
            actualPages += 1
    if(actualPages == len(pages)):
        centerNumber = getCenterNumber(pages)
        print(f"--Valide / centerNumber {centerNumber} ")
        total += centerNumber


print(f"total: {total}")    
