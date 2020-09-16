def gradingStudents(grades):
    for count in range(len(grades)):
        if grades[count] < 38:
            continue
        else:
            # setting comparision COM
            COM = (grades[count] // 5 + 1) * 5
            if COM - grades[count] < 3:
                grades[count] = COM
            else:
                pass
    return grades

if __name__ == '__main__':
    grade_count = int(input().strip())
    grades = []

    for _ in range(grade_count):
        grades.append(int(input().strip()))
    result = gradingStudents(grades)
    print('\n'.join(map(str, result)))

                
                
                
