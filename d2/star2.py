input = [
[59, 55, 52, 49, 47, 44]
]

safe = 0

def testMethod(line, last):
    trend = None
    error = False

    if(last is False):
        print(f"---list {line}")
    else:
        print(f"---new list {line}")
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
                if(last is False):
                    if(i == 2):
                        if(elt <= line[i+1]):
                            line.pop(i - 1)
                        else:
                            line.pop(i)
                    else:
                        line.pop(i)
                    return testMethod(line, True)
                else:
                    return False;
        else:
            if(prevElt >= elt):
                print("ERROR INCREASE")
                if(last is False):
                    if(i == 2):
                        if(elt >= line[i+1]):
                            line.pop(i - 2)
                        else:
                            line.pop(i)
                    else:
                        line.pop(i)
                    return testMethod(line, True)
                else:
                    return False;

        ## CONDITION 2: diff entre deux niveaux
        diff = abs(prevElt - elt) 
        print(diff)
        if(1 <= diff <= 3):
            test = None
            print("OK")
        else:
            print("ERROR DIFF NIV")
            if(last is False):
                if(diff < 1):
                    line.pop(i-1)
                elif(diff > 3 and i == 1 and 0 > (elt - line[i+1]) <=3):
                    line.pop(i-2)
                elif(diff > 3 and i != len(line)-1 and 0 > (elt - line[i+1]) <=3 and 0 > (prevElt - line[i+1]) <= 3):
                    line.pop(i-1)
                else:
                    line.pop(i)
                return testMethod(line, True)
            else:
                return False;

        ## COMPTEUR SAFE
        prevElt = elt
        if(i == len(line) - 1 and error is False):
            print("-----------SAFE")
            return True


# TODO FAIRE fonctionner cette méthode et garder une logique simple dans la testMethod
def searchError(newLine):
    return newLine

# On parcourt toutes les lignes
for line in input:
    print("-----------INPUT ENTRY") 
    result = testMethod(line, False)
    if(result is True):
        safe += 1
    else:
        # Supprimer chaque élément dans la line et tester chaque element en moins
        # mettre une compteur et dire s'il y a un safe > 1 dans les ayant tous supprimer 
        newLine = searchError(line)
        result2 = testMethod(newLine, True)
        if (result2 is True):
            safe += 1 

print(f"Safe: {safe}")



