student_name_list = ['Ivanov', 'Petrov', 'Yablochkin', 'Grushin', 'Lastochkin']
student_class = ['10A', '10B', '10V']
subject_math = [3, 4, 5, 5, 4]
subject_physics = [2, 4, 4, 5, 3]
subject_ruslan = [2, 5, 5, 5, 2]

# НАДО ИСПОЛЬЗОВАТЬ АППЕНД 
# НЕ РАБОТАЕТ


def marks_B(student_name_list, subject_math, subject_physics, subject_ruslan):
    marks_B = []
    for i in range(len(student_name_list)):
        if subject_math[i] >= 4 and subject_physics[i] >= 4 and subject_ruslan[i] >= 4:
                student_name_list.append(marks_B)
            
    return marks_B
print(marks_B)

def one_bad_mark_student(student_name_list, subject_math, subject_physics, subject_ruslan):
    one_bad_mark_student = []
    for i in range(len(student_name_list)):
        if 2 in subject_math[i] and 2 in subject_physics[i] and 2 in subject_ruslan[i]: 
            one_bad_mark_student(student_name_list[i])
            
    return one_bad_mark_student
print(one_bad_mark_student)