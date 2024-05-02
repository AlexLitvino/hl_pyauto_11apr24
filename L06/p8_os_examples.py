import os

# Getting platform
# print(os.uname())  # not for Windows
# import platform
# print(platform.platform())

# Working with environment variables
#print(os.environ)
# os.getenv()
# os.putenv()


# Working with working directory
# print(os.getcwd())
# os.chdir(<PATH>)


# # Returns list of directory content (files and dirs)
# print(os.listdir('walk_example'))

# # # os.walk(root_directory)
# for dirpath, dirnames, filenames in os.walk('walk_example'):
#     #print(dirpath, dirnames, filenames)
#     for file_name in filenames:
#         print(file_name)



# os.mkdir('NEW_DIR')  # create directory
# os.remove('FILE')  # removes file

# Renaming file dirs, different exceptions depending if empty or not
# os.rename()
# os.replace(<PATH>)
# os.renames()

#os.makedirs('NEW_DIR/LEVEL2/LEVEL3')  # creates parent directories if missing
# os.rmdir('NEW_DIR')  # removes directory
# os.removedirs('NEW_DIR\LEVEL2\LEVEL3')  # removes empty directories from bottom to top


# # Submodule os.path
#print(__file__)
#print(os.path.basename(__file__))
# print("QQQ")
# print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
# print(os.path.exists(__file__))
# print(os.path.exists(__file__ + 'Q'))
# print(os.path.isdir(__file__))
# print(os.path.isfile(__file__))
#
print(os.path.split(__file__))
parent = os.path.split(os.path.split(__file__)[0])[0]
path_to_new_file = os.path.join(parent, 'NEW_FILE')
print(path_to_new_file)
