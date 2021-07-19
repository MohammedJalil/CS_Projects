# File: Project1.py
# Student: Mohammed Jalil
# UT EID: mhj476
# Course Name: CS303E
# 
# Date Created: 3/18/21
# Date Last Modified: 3/21/21 
# Description of Program: This program acts as a grade calculator, specifically
# for CS 303E and will take the inputs of homework, project, and exam grades
# in order to calculate the average of those three categories and the course
# average as a whole while also including a letter grade.

def homework():  # Storing the correct inputs of homework grades.

    homework.homeworkTotal = 0
    homeworkCount = 0
    while homeworkCount < 1:
        homework1 = int(input("  Enter HW1 grade: "))
        if homework1 > 10 or homework1 < 0:
            print("  Grade must be in range [0..10]. Try again.")
        else:
            homework.homeworkTotal += homework1
            homeworkCount += 1
    while homeworkCount < 2:
        homework2 = int(input("  Enter HW2 grade: "))
        if homework2 > 10 or homework2 < 0:
            print("  Grade must be in range [0..10]. Try again.")
        else:
            homework.homeworkTotal += homework2
            homeworkCount += 1
    while homeworkCount < 3:
        homework3 = int(input("  Enter HW3 grade: "))
        if homework3 > 10 or homework3 < 0:
            print("  Grade must be in range [0..10]. Try again.")
        else:
            homework.homeworkTotal += homework3
            homeworkCount += 1

def exam(): # Storing the correct inputs of exam grades

    exam.examTotal = 0
    examCount = 0
    while examCount < 1:
        exam1 = int(input("  Enter Exam1 grade: "))
        if exam1 > 100 or exam1 < 0:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            exam.examTotal += exam1
            examCount += 1
    while examCount < 2:
        exam2 = int(input("  Enter Exam2 grade: "))
        if exam2 > 100 or exam2 < 0:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            exam.examTotal += exam2
            examCount += 1

def project(): # Storing the correct inputs of project grades.

    project.projectTotal = 0
    projectCount = 0
    while projectCount < 1:
        project1 = int(input("  Enter Project1 grade: "))
        if project1 > 100 or project1 < 0:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            project.projectTotal += project1
            projectCount += 1
    while projectCount < 2:
        project2 = int(input("  Enter Project2 grade: "))
        if project2 > 100 or project2 < 0:
            print("  Grade must be in range [0..100]. Try again.")
        else:
            project.projectTotal += project2
            projectCount += 1

def average(): # Calculating the course average and letter grade.

    average.averageTotal = 0 # Caulating the course average given other averages.
    average.averageTotal += ((homework.homeworkTotal / 30) * 100 * .3 + \
                            (project.projectTotal / 200) * 100 * .3 + \
                            (exam.examTotal / 200) * 100 * .4)

    print("  Student course average:", \
          format(average.averageTotal, "2.2f")) # Calculating letter grade.
    if average.averageTotal >= 90 and average.averageTotal < 100:
        print("  Course grade (CS303E: Spring, 2021): A")
    elif average.averageTotal >= 80 and average.averageTotal < 90:
        print("  Course grade (CS303E: Spring, 2021): B")
    elif average.averageTotal >= 70 and average.averageTotal < 80:
        print("  Course grade (CS303E: Spring, 2021): C")
    elif average.averageTotal >= 60 and average.averageTotal < 70:
        print("  Course grade (CS303E: Spring, 2021): D")
    else:
        print("  Course grade (CS303E: Spring, 2021): F")
    print("")


print("")
name = input("Enter the student's name: ")
print("")
print("HOMEWORKS:")
homework() # need to call the homework function.
print("")
print("PROJECTS:")
project() # need to call the project function.
print("")
print("EXAMS:")
exam() # need to call the exam function.
print("")
print("Grade report for:", name)
print("  Homework average (30% of grade):", \
        format((homework.homeworkTotal / 30) * 100, "2.2f")) #Homework average
print("  Project average (30% of grade):", \
        format((project.projectTotal / 200) * 100, "2.2f")) # Project average
print("  Exam average (40% of grade):", \
        format((exam.examTotal / 200) * 100, "2.2f")) # Exam average

average()



