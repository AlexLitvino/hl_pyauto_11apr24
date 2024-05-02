import collections

# # # Named tuple
# ConfigOption = collections.namedtuple('ConfigOption', ['name', 'value'])
# config_options = []
# base_url = ConfigOption(name='base_url', value='127.0.0.1')
# config_options.append(base_url)
# port = ConfigOption('port', '8000')
# config_options.append(port)
#
# def set_config_option(config_option):
#     print(f"Setting {config_option.name} to value {config_option.value}...")
#
#
# for config_option in config_options:
#     set_config_option(config_option)


# # Deque
# deque = collections.deque('abc', maxlen=3)
# print(deque)
# deque.append('d')
# print(deque)
# deque.appendleft('e')
# print(deque)


# # ChainMap
# d1 = {1: 'a', 2: 'b'}
# d2 = {3: 'c', 4: 'd', 5: 'e'}
# chain = collections.ChainMap(d1, d2)
# print(chain)
# d2[2] = 'key 2 from d2'
# print(chain)
# print(chain[2])
# chain[6] = 'f'
# print(chain)


# # Counter
# lst = [2, 4, 0, 3, 7, 1, 4, 8, 1, 3,
#        3, 6, 4, 4, 4, 9, 8, 1, 9, 5,
#        3, 3, 3, 1, 9, 1, 7, 8, 4, 9,
#        6, 3, 7, 9, 9, 3, 0, 6, 9, 7,
#        4, 2, 5, 6, 5, 4, 2, 4, 6, 2,
#        5, 1, 6, 6, 5, 8, 2, 6, 6, 2,
#        9, 1, 2, 4, 7, 5, 1, 9, 4, 5,
#        2, 7, 6, 8, 2, 6, 2, 5, 3, 3,
#        0, 0, 5, 0, 7, 1, 9, 5, 9, 3,
#        5, 6, 6, 5, 1, 8, 6, 5, 0, 5]
# print(lst)
#
# counter = collections.Counter(lst)
# print(counter)
# print(dir(counter))
# print(counter.keys())  # Elements meet in initial iterable
# print(counter[1])  # Frequency for key = 1

# collections.Counter([1, 2, [3]])


# # OrderedDict
# ordered_dict = collections.OrderedDict([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
# print(ordered_dict)
# ordered_dict.move_to_end(1)
# print(ordered_dict)
# ordered_dict.popitem(last=True)
# print(ordered_dict)
# ordered_dict.popitem(last=False)
# print(ordered_dict)


# # Defaultdict
person_by_age = collections.defaultdict(set)
Person = collections.namedtuple('Person', ['name', 'age'])
persons = [Person('John', 32), Person('Anna', 17), Person('Godfrua', 190), Person('Demian', 17)]
for person in persons:
    person_by_age[person.age].add(person.name)
print(person_by_age)
