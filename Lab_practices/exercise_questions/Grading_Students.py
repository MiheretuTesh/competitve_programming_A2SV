def gradingStudents(grades):
    # Write your code here
    grade_report = []
    for grade in grades:
        if(grade>=38):
            if((grade+1)%5==0):
                grade_report.append(grade+1)
            elif((grade+2)%5==0):
                grade_report.append(grade+2)
            else:
                grade_report.append(grade)  
        else:
            grade_report.append(grade)
    return grade_report

print(gradingStudents([50,51,54,65,86,57,48,89,23,37]))