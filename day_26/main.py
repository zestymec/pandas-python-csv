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