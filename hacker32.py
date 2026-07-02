def gradingStudents(grades):
    rounded_grades = []
    
    for grade in grades:
        # Rules don't apply to failing grades below 38
        if grade < 38:
            rounded_grades.append(grade)
        # Check if the grade is within 2 points of the next multiple of 5
        elif grade % 5 >= 3:
            remainder = grade % 5
            rounded_grades.append(grade + (5 - remainder))
        # Otherwise, keep the original grade
        else:
            rounded_grades.append(grade)
            
    return rounded_grades
