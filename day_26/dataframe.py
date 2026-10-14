student_dict ={
    "student" : ["Angela" , "james" , "Lily"],
    "score":[19,28,43]
}
for (key,value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)



for (key , value) in student_data_frame.items():
    print(value)

for (index , row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "james":
        print(row.score)