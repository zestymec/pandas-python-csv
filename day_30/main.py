"""Day 30: errors, exceptions, and JSON."""

try:
    file = open("a_file.txt")
    dic = {"key" : "value"}
    print(dic["key"])
except FileNotFoundError:
    file = open("a_file.txt" , "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print(f"{file}file is closed")
    raise TypeError("this error come because i raise it thorough rise (typeerr)")