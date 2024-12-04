import re

input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('input.txt', "r") as fichier:
    input = fichier.read()

total = 0


# Traitement de texte avec les do et don't
regex = r"don't\(\).*?do\(\)"
traitement = re.sub(regex, "", input, flags=re.DOTALL)

regex2 = r"don't\(\).*?$"
traitement2 = re.sub(regex2, "", traitement, flags=re.DOTALL)

# repérage des mul
pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, traitement2)

for mul in matches:
    nombre1, nombre2 = map(int, mul)
    resultat = nombre1 * nombre2
    total += resultat

print(f"Total: {total}")