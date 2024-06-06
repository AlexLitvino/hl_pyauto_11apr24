"""
3qq 5qqqq
2q
"""


# file_path = 'data2.txt'
#
# try:
#     with open(file_path, 'r') as f:
#         data = f.read()
#         size = len(data)
#         words_number = len(data.split())
#         average_symbols_per_word = size / words_number
#     print(average_symbols_per_word)
# # except (FileNotFoundError, ZeroDivisionError):
# #     print("Common error")
# # except ZeroDivisionError as e:
# #     print(e)
# #     print("Empty file")
# # except ArithmeticError:
# #     print("Arithmetic error")
# # except FileNotFoundError:
# #     print("Specify correct file")
# # except:
# #     print("Catch everything")
# except Exception as e:
#     print(e)
# # else:
# #     print("No errors")
# finally:
#     print("Clean up")

# import time
# while True:
#     try:
#         print("RUN")
#         time.sleep(0.5)
#     except KeyboardInterrupt:
#         print("In except")
#         break
# print("After")

class MyAppException(Exception):
    pass

class InvalidComponent(MyAppException):

    def __init__(self, message, file):
        self.message = message
        self.file = file

    def log(self):
        with open(self.file, 'a') as f:
            f.write(self.message)

try:
    raise InvalidComponent('ERROR!!!', 'error.log')
except InvalidComponent as e:
    e.log()

#raise FileNotFoundError
raise FileNotFoundError("ERROR")
