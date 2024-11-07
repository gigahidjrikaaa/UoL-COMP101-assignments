# Adkhy_Giga 201847335  October2024 CA-4.py
# Grading program - inserts raw grade and days late, calculates final grade, starts with student ID 1 and goes up to 176

isDone = False
studentID = 1

while studentID <= 176 and isDone != True:
    testGrade = 0
    codeGrade = 0
    rawGrade = 0
    daysLate = 0
    latePenalty = 0
    finalGrade = 0

    print("=====================================")
    print("Student ID: ", studentID, "\n[ENTER EMPTY VALUES IF NO SUBMISSION/NO LATE SUBMISSION]")
    print("=====================================")

    testGrade = input("Enter the test grade (0 - 100): ")
    if testGrade == "":
        testGrade = 0

    while str(testGrade).isnumeric() == False or int(testGrade) < 0 or int(testGrade) > 100:
        testGrade = input("Invalid input. Please enter an integer between 0 and 100: ")

    codeGrade = input("Enter the code grade (0 - 100): ")
    if codeGrade == "":
        codeGrade = 0

    while str(codeGrade).isnumeric() == False or int(codeGrade) < 0 or int(codeGrade) > 100:
        codeGrade = input("Invalid input. Please enter an integer between 0 and 100: ")

    daysLate = input("Enter the number of days late (0 - 2): ")
    if daysLate == "":
        daysLate = 0
    while str(daysLate).isnumeric() == False or int(daysLate) < 0 or int(daysLate) > 2:
        daysLate = input("Invalid input. Please enter an integer between 0 and 2: ")
    
    latePenalty = 5 * int(daysLate)
    print("Late penalty: ", latePenalty, "(" + str(daysLate) + " days late)")

    rawGrade = (int(testGrade) + int(codeGrade)) / 2
    print("The student's raw grade is: ", rawGrade)

    finalGrade = rawGrade - latePenalty
    
    print("The student's final grade is: ", finalGrade)
    
    isDone = input("Are you done grading? (Y/N): ").upper()
    if isDone == "Y":
        isDone = True
    else:
        isDone = False
        studentID += 1
    