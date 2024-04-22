# String interpolation
name = "John"
age = 34
# print("My name is", name, ". I'm", age, "years old.")
# print("My name is" + " " + name + ". I'm " + str(age) + " years old.")
# print("My name is %s. I'm %d years old." % (name, age))
# print("My name is {}. I'm {} years old. {}".format(name, age, name))
# print("My name is {name}. I'm {age} years old.{name}".format(name=nameA, age=ageA))
# print(f"My name is {name}. I'm {age} years old. {age * 100}")

# import string
# template_string = string.Template("My name is $name. I'm $age years old.")
# print(template_string.substitute(name=name, age=age))


# TODO
container_name_or_id = "mongo"
# docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
# cmd = f"docker inspect -f '{{{{range.NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}' {container_name_or_id}"
# print(cmd)
new_line = '\n'
cmd = f"Line1{new_line}{container_name_or_id}"
print(cmd)