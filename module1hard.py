grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grades_average = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
stud_dict = {students[0]:grades_average[0], students[1]:grades_average[1], students[2]:grades_average[2], students[3]:grades_average[3], students[4]:grades_average[4]}
print(stud_dict)