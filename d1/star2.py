exampleL1 = [3,4,2,1,3,3]
exampleL2 = [4,3,5,3,9,3]

l1 = []
l2 = []

count = 0;

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        columns = line.split()
        
        l1.append(int(columns[0]))
        l2.append(int(columns[1]))


if len(l1) != len(l2):
    print("Les listes non pas autant d'élément")


# Défi partie 2 
sum = 0

for elt in l1:
    occ = l2.count(elt)
    find = elt * occ
    sum += find

print(f"sum: {sum}")
