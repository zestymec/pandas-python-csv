"""Day 30: errors, exceptions, and JSON."""

try:
    File = open("a_file.txt")
    dic = {"key" : "value"}
    print(dic[umer])
except FileNotFoundError:
    file = open("a_umer.txt" , "w")
    file.write("something")
except KeyError:
    print("key not found")