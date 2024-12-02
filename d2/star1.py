input = [
    [7,6,4,2,1], # SAFE
    [1,2,7,8,9], # UNSAFE
    [9,7,6,2,1], # UNSAFE
    [1,3,2,4,5], # UNSAFE
    [8,6,4,4,1], # UNSAFE
    [1,3,6,7,9], # SAFE
]

trend = None
error = False
safe = 0

# On parcourt toutes les lignes
for line in input:
    #print("INPUT ENTRY") 
    for i, elt in enumerate(line): 
        ## CONDITION 1 : Croissant ou Décroissant
        #print(f"start {i} with {elt}")
        if(error is True):
            continue
        if(i == 0): 
            prevElt = elt;
            continue
        if(trend is None):
            if(prevElt > elt):
                trend = 'decreasing'
            else:
                trend = 'increase'
        #print(f" prevElt {prevElt} // elt {elt} // trend {trend}")
        if(trend == 'decreasing'):
            if(prevElt <= elt):
                error = True
                #print("ERROR")
        else:
            if(prevElt >= elt):
                error = True
                #print("ERROR")

        ## CONDITION 2: diff entre deux niveaux
        diff = abs(prevElt - elt) 
        #print(diff)
        if(1 <= diff <= 3):
            test = None
            #print("OK")
        else:
            error = True

        ## COMPTEUR SAFE
        prevElt = elt
        if(i == len(line) - 1 and error is False):
            safe += 1
            #print("SAFE")
        

    #print(f"Trend: {trend}")
    trend = None
    error = False

print(f"Safe: {safe}")