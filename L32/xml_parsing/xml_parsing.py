import xml.etree.ElementTree as ET

# my_tree_string = """
# <data>
#     <country name="Liechtenstein">
#         <rank>1</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>
#     <country name="Singapore">
#         <rank>4</rank>
#         <year>2011</year>
#         <gdppc>59900</gdppc>
#         <neighbor name="Malaysia" direction="N"/>
#     </country>
#     <country name="Panama">
#         <rank>68</rank>
#         <year>2011</year>
#         <gdppc>13600</gdppc>
#         <neighbor name="Costa Rica" direction="W"/>
#         <neighbor name="Colombia" direction="E"/>
#     </country>
# </data>
# """
#
# root = ET.fromstring(my_tree_string)
# print(root)


tree = ET.parse('countries.xml')
root = tree.getroot()
# print(root)
# print(root.attrib)
# print(root.text)
# print(root.tail)

# for element in root:
#     print(element)
#     print(element.attrib)
#     print(element.text)
    #print(element.tail)

country1 = root[0]
# print(country1)
# print(country1.attrib)
# year_country1 = root[0][1]
# print(year_country1.text)

# for element in country1:
#     print(element)
#     print(element.attrib)
#     print(element.text)
#     print()

# #for element in root.iter():
# for element in root.iter('year'):
#     print(element)
#     print(element.attrib)
#     print(element.text)

# print(root.findall('.//rank'))
# print(root.findall('/country'))  # error

# print(root.find('country').attrib)

# country1 = root[0]
# print(country1.get('name1', 'QQQQ'))
# print(country1.attrib['name'])

root[0][1].text = "99999999"
root[0].set('name', 'New Zeland')
root[0].set('attr', 'value')
panama = root[2]
root.remove(panama)

population = ET.Element('population', {'attr2': 'value2'})
root[0].append(population)
population.text = '777777777777777'
tree.write('countries_out.xml')
