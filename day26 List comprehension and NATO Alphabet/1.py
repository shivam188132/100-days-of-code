student_dict = {"students": ["Angela", "Shivam", "Ram"],
                "grade": [34, 56, 67]}
# looping through dictionary
# for (ram, sita) in student_dict.items():
# or for (key, value) in student_dict.items():
# print(key)
#     print(sita)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# looping through data frame
# for (key, value) in student_data_frame.items():
#      print(value)
# loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row)
