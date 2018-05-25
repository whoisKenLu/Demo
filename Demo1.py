animals = ['bear', 'dinosaur', 'wolf', 'sheep']

str_animals = '-'.join(animals)

list_animals = str_animals.split('-')

print(str_animals )
print(list_animals )

for index, item in enumerate(animals):
    print(index, item)

print('wolfs' in animals)