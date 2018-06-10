# Tuple的创建
animals1 = ('bear', 'dinosaur', 'wolf', 'sheep')

# Set的创建
animals1 = {'bear', 'dinosaur', 'wolf', 'sheep'}
animals2 = {'cat', 'dog', 'wolf', 'duck', 'bear'}

# 两个Set的交集
print(animals1.intersection(animals2))
# 两个Set的并集
print(animals1.union(animals2))
# 两个Set的差，animals1-animals2
print(animals1.difference(animals2))

# 创建空的list
empty_list = []
empty_list = list()
# 创建空的tuple
empty_tuple = ()
empty_tuple = tuple()
# 创建空的set
empty_set = set()

