numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "umer"
new_list = [letter.title() for letter in name]
print(new_list)


rang = range(1 , 5)

range_list = [num*2 for num in rang]
print(range_list)



names = ['Azhar' , 'Taha' , 'Huzaifa' , 'Ahad' , 'Anas' , 'Rafay']

new = [name.upper() for name in names if len(name) > 5]
print(new)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(x) for x in list_of_strings]
print(numbers)

with open("file1.txt", "r") as file1:
    number_1 = [line.strip() for line in file1]
with open("file2.txt", "r") as file2:
    number_2 = [line.strip() for line in file2]


result = [int(num) for num in number_1 if num in number_2]

print(result)