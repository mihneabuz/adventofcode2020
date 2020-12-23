import sys

foods = []
ingredients = ""
alergens = ""
for line in sys.stdin:
    ingredients, alergens = [x[:-1] for x in line[:-1].split("(contains ")]
    ingredients = ingredients.split(" ")
    alergens = alergens.split(", ")
    foods.append([set(ingredients), set(alergens)])

ingredients = set(foods[0][0])
allergens = set(foods[0][1])

for food in foods[1:]:
    ingredients.update(food[0])
    allergens.update(food[1])

#print("ingredients: ", ingredients)
#print("allergens: ", allergens)

possible = set()
for allerg in allergens:
    current = ingredients
    for food in foods:
        if (allerg in food[1]):
            current = current.intersection(food[0])
    possible.update(current)

count = 0
impossible = ingredients - possible
for ing in impossible:
    for food in foods:
        if (ing in food[0]):
            count += 1
print("Part one:", count)

for food in foods:
    food[0] -= impossible
ingredients -= impossible

allergmap = {}
while(len(allergmap) < len(allergens)):
    for allerg in allergens:
        current = ingredients
        for food in foods:
            if (allerg in food[1]):
                current = current.intersection(food[0])
        if (len(current) == 1):
            for food in foods:
                food[0] -= current
            allergmap.update({allerg: current.pop()})

sorted = list(allergens)
sorted.sort()

print("Part two: ", end = '')
for i in sorted[:-1]:
    print(allergmap[i], end = ',')
print(allergmap[sorted[-1]])
