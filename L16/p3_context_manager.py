# try:
#     file = open('data.txt')
#     data = file.read()
#     print(data)
#     1/0
# finally:
#     print("Closing file...")
#     file.close()

# with open('data.txt', 'r') as file:
#     data = file.read()
#     print(data)

# class BlockPrinter:
#
#     def __init__(self, header, footer):
#         self.header = header
#         self.footer = footer
#
#     def __enter__(self):
#         print(f"{'='*40} {self.header} {'='*40}")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#         print(f"{'=' * 40} {self.footer} {'=' * 40}")
#
#
# with BlockPrinter('HEADER', 'FOOTER'):
#     print(1)
#     1/0
#     print(2)


class UpperFile:

    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self):
        return self.file.read().upper()

    def __getattr__(self, item):
        return getattr(self.file, item)


#
# with UpperFile('p1_exceptions.py') as file:
#     print(file.read())

from contextlib import contextmanager

@contextmanager
def file(file_path, mode='r'):
    try:
        file_obj = open(file_path, mode)
        yield file_obj
    finally:
        print("In EXIT")
        file_obj.close()


with file('p1_exceptions.py') as f:
    1/0
    print(f.read())