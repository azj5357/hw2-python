# Author: Archit Javkhedkar

def getGradePoint(letter):
    letter_gradepoint = {"A" : 4.0, "A-" : 3.67, "B+": 3.33, "B" : 3.0, "B-" : 2.67, "C+" : 2.33, "C" : 2.0, "D" : 1.0}
    if letter in letter_gradepoint:
        return letter_gradepoint[letter]
    return 0.0

total_creds = 0.0
total_gradepoint = 0.0
for i in range(1, 4):
    letter_grade = input("Enter your course {} letter grade: ".format(i))
    creds = float(input("Enter your course {} credit: ".format(i)))
    gp = getGradePoint(letter_grade)
    total_gradepoint = total_gradepoint + gp * creds
    total_creds = total_creds + creds
    print("Grade point for course {} is: {}".format(i, gp))

print("Your GPA is: {}".format(total_gradepoint / total_creds))




