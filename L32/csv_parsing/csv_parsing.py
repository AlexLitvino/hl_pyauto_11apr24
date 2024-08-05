import csv

# with open('data.csv') as f:
#     reader = csv.reader(f)
#     # TODO: how to skip headers?
#     print()
#     # iter, next
#     next(reader)
#     for line in reader:
#         print(line)


# with open('data.csv') as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line)

# data = [['test_id', 'param1', 'param2'],
#         ['id1', 1, '34'],
#         ['id2', 3, '54']]
#
# with open('csv_output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(data)

dict_data = [
    {'id': 3333, 'name': 'John', 'age': '34'},
    {'id': 2222, 'name': 'Anna', 'age': '35'}
]

with open('dict.csv', 'w', newline='') as f:
    dict_writer = csv.DictWriter(f, dict_data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(dict_data)
