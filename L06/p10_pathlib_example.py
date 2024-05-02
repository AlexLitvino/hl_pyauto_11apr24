import pathlib

some_path = pathlib.Path('PARENT_DIR', 'DIR', 'file.txt')  # combine parts of path
print(some_path)

home = pathlib.Path.home()  # get home dir for user
print(home)

another_path = pathlib.Path(home, pathlib.Path('DIR_IN_HOME', 'NESTED_DIR'), 'file_in_nested_dir.txt')
print(another_path)
print(another_path.name)
print(another_path.suffix)
print(another_path.parent)
print(another_path.parent.parent)

# for parent in another_path.parents:
#     print(parent)

# for part in another_path.parts:
#     print(part)

# print(another_path.exists())

# # Searching by pattern
# for file_path in pathlib.Path('walk_example').glob('dir_*'):
#     print(file_path)

# another_path.mkdir(mode, parents, exist_ok)  # create dir
# another_path.touch(mode, exist_ok)  # create file
# another_path.rename(target)  # renames file/dir
# another_path.read_text()  # reads text from file
# another_path.write_text()  # writes text to file
