# # TODO: Task: Get values for href attributes for <a> tag
href_attr_values = []

a_tag_begginning = '<a'

with open('wiki_page.txt') as f:
    #data = f.read()
    for line in f:
        if a_tag_begginning in line:
            start_a_tag_index = line.index(a_tag_begginning)
            start_href_attr_index = line.index('href="', start_a_tag_index)
            end_href_attr_index = line.index('"', start_href_attr_index + len('href="'))
            #print(start_href_attr_index)
            href_value = line[start_href_attr_index+len('href="'):end_href_attr_index]
            href_attr_values.append(href_value)

# print(href_attr_values)
#
# with open('wiki_page.txt') as f:
#     data = f.read()
# import re
# href_attr_values_using_re = re.findall(r'<a .*href=\"(.+?)\"', data)
# print(href_attr_values_using_re)


# # Solving the same problem but using regexp
# href_attr_values_using_re = []

# ######################################################################################################################

# # Recollect raw strings
r"\\"

# ######################################################################################################################

# # Two ways of regexp in Python
# pattern = "(\w{5})"
# string = "Hello, hello, hello, how low?"
#
# regexp_obj = re.compile(pattern)
# result1 = regexp_obj.findall(string)
# print(result1)
#
# result2 = re.findall(pattern, string)
# print(result2)
# print(result1 == result2)
# ######################################################################################################################
import re
text = "050111111 John Smith;+38022222222 Anna Poe; 5555555555 Aleksandr Miln"

# #re.search(pattern, string, flags=0)
# result = re.search(r'(\d+) (\w+)', text)
# print(result)
# print(result.group())
# print(result.group(0))
# print(result.groups())
# print(result.start())
# print(result.end())
# print(result.span())


# # re.match(pattern, string, flags=0)
# result = re.match(r'\d+', text)
# print(result)
# result = re.match(r'\d+', "A 555555555")
# print(result)


# # re.fullmatch(pattern, string, flags=0)
# result = re.fullmatch(r'\d+', text)
# print(result)
# result = re.fullmatch(r'\w+ \d+', "A 555555555")
# print(result)


# # re.split(pattern, string, maxsplit=0, flags=0)
# input_line = "[11,33,43,[22,54,87],54]"
# print(input_line.split(',[]'))
# split_line = re.split('[\[,\]]', input_line)
# print(split_line)

# result = re.split(r"\W*;", text, maxsplit=1)
# print(result)


# # re.findall(pattern, string, flags=0)
# result = re.findall(r'\d+', text)
# print(result)
# result = re.findall(r'(\d+)', text)
# print(result)
# result = re.findall(r'(\d+) (\w+)', text)
# print(result)


# # re.finditer(pattern, string, flags=0)
# result = re.finditer(r'\d+', text)
# print(result)
# for match in result:
#     print(match.group())


# # re.sub(pattern, repl, string, count=0, flags=0)
# result = re.sub(r'\d+', 'UNKNOWN', text)
# print(result)


# # re.subn(pattern, repl, string, count=0, flags=0)
# result = re.subn(r'\d+', 'UNKNOWN', text)
# print(result)


# # Flags
# input_line = "abcDefGh"
# print(re.findall('[a-z]', input_line))
# print(re.findall('[a-z]', input_line, flags=re.IGNORECASE))


# # input_line = "Hello Привет"
# # print(re.findall(r'(\w+)', input_line))
# # print(re.findall(r'(\w+)', input_line, flags=re.ASCII))


# multi_line = """Hello
# Привет
# Hola
# """
# print(re.findall(r'^(\w+)', multi_line))
# print(re.findall(r'^(\w+)', multi_line, flags=re.MULTILINE))
# print(re.findall(r'^(\w+)', multi_line, flags=re.MULTILINE | re.ASCII))


# # Greedy/non greedy
# text = "<html><h1>HEADER</h1><p>Paragraph</p></html>"
# res1 = re.findall('<.*>', text)
# print(res1)  # ['<html><h1>HEADER</h1><p>Paragraph</p></html>']
# res2 = re.findall('<.*?>', text)
# print(res2)  # ['<html>', '<h1>', '</h1>', '<p>', '</p>', '</html>']
