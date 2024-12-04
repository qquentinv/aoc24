import re

input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


with open('input.txt', "r") as fichier:
    input = fichier.read()

total = 0

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, input)

for mul in matches:
    nombre1, nombre2 = map(int, mul)
    resultat = nombre1 * nombre2
    total += resultat

print(f"Total: {total}")