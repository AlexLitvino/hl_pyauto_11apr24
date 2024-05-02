# try:
#     file = open('set_methods.md', 'r')
#     data = file.read()
# except IOError:
#     print("Error")
# finally:
#     file.close()
# print(data)


# with open('set_methods.md') as file:
#     data = file.read()
#     print(data)


# with open('new_file2.txt', 'w') as f:
#     #f.write('AAA\nBBB')
#     #f.writelines(['CCC\n', 'DDD\n'])
#     f.write('QA')

# with open('L06/new_file.txt', 'r') as f:
#     print(f.read())

with open('image.png', 'rb') as f:
    data = f.read()
    print(data)