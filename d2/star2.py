input = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]

input = []

with open("input.txt", "r") as file:
    for line in file:
        array_lines = list(map(int, line.split()))
        input.append(array_lines)

safe = 0

def testMethod(line):
    trend = None
    error = False

    for i, elt in enumerate(line): 
        ## CONDITION 1 : Croissant ou Décroissant
        print(f"start {i} with {elt}")
        if(i == 0): 
            prevElt = elt;
            continue
        if(trend is None):
            if(prevElt > elt):
                trend = 'decreasing'
            else:
                trend = 'increase'
        print(f" prevElt {prevElt} // elt {elt} // trend {trend}")
        if(trend == 'decreasing'):
            if(prevElt <= elt):
                print("ERROR DECREASING")
                return False;
        else:
            if(prevElt >= elt):
                print("ERROR INCREASE")
                return False;

        ## CONDITION 2: diff entre deux niveaux
        diff = abs(prevElt - elt) 
        print(diff)
        if(1 <= diff <= 3):
            test = None
            print("OK")
        else:
            print("ERROR DIFF NIV")
            return False;

        ## COMPTEUR SAFE
        prevElt = elt
        if(i == len(line) - 1 and error is False):
            print("-----------SAFE")
            return True

def generateNewLines(line):
    return [line[:i] + line[i+1:] for i in range(len(line))]

# On parcourt toutes les lignes
for line in input:
    print("-----------INPUT ENTRY") 
    result = testMethod(line)
    if(result is True):
        safe += 1
    else:
        newSafe = 0
        newLines = generateNewLines(line)
        for newLine in newLines:
            result2 = testMethod(newLine)
            if (result2 is True):
                newSafe += 1 
        if(newSafe > 0):
            safe += 1

print(f"Safe: {safe}")