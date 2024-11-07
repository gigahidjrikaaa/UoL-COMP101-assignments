# Adkhy_Giga 201847335  October2024 CA-4.py
# Grading program
# 

isDone = False
studentID = 1

while studentID <= 176 and isDone != True:
    rawGrade = 0
    daysLate = 0
    latePenalty = 0
    finalGrade = 0

    print("Student ID: ", studentID, "\n[ENTER EMPTY VALUES IF NO SUBMISSION]")
    try:
        rawGrade = int(input("Enter the student's raw grade (1 - 100): "))
    except ValueError:
        while rawGrade < 0 or rawGrade > 100 or str(rawGrade).isnumeric() == False:
            print("Invalid input. Please enter an integer between 1 and 100.")
            rawGrade = int(input("Enter the student's raw grade (1 - 100): "))

    daysLate = int(input("Enter the number of days late (0 - 2): "))
    while daysLate < 0 or daysLate > 2 or str(daysLate).isnumeric() == False:
        print("Invalid input. Please enter an integer between 0 and 2.")
        daysLate = int(input("Enter the number of days late (0 - 2): "))
    
    latePenalty = 5 * daysLate
    finalGrade = rawGrade - latePenalty
    
    print("The student's final grade is: ", finalGrade)
    
    isDone = input("Are you done grading? (Y/N): ")
    isDone = isDone.upper()
    if isDone == "Y":
        isDone = True
    else:
        isDone = False
        studentID += 1
    