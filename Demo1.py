# 创建一个list
animals = ['bear', 'dinosaur', 'wolf', 'sheep']

# list的“写”的操作
# 1）增加新的元素
# Append, 在list的末尾添加元素
animals.append('cat')
# Insert，在list的指定位置添加元素
animals.insert(0, 'cat')
# Extend, 将其他list中的元素附加到原有的list中
small_animals = ['cat', 'dog']
animals.extend(small_animals)

# 2)删除元素
# Remove, 删除指定的元素
animals.remove('bear')
# Pop，将list中的最后一个元素删除，并返回此元素
popped_animal = animals.pop()
# del, 删除指定位置的元素
del animals[1]

# 3)修改元素
# 修改某个元素
animals[1] = 'cat'
# 修改一段元素
animals[:2] = ['cat', 'dog']

# list转换成字符串
str_animals = '-'.join(animals)
# 字符串转换成list
list_animals = str_animals.split('-')

# list的遍历
for item in enumerate(animals):
    print(item)

for index, item in enumerate(animals):
    print(index, item)

# list的排序
animals.reverse()
animals.sort()
animals.sort(reverse=True)

# 用in判断某个元素是否存在于list中
print('wolfs' in animals)