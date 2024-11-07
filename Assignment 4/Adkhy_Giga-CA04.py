# Adkhy_Giga Nov2024 CA-04.py
# Grading program - inserts raw grade and days late, calculates final grade, starts with student ID 1 and goes up to 176

isDone = False
studentID = 1

# Loop to input grades for each student, use isDone flag to exit loop
while studentID <= 176 and isDone != True:
    # Initialize variables. Put inside loop to reset for each student
    testGrade = 0
    codeGrade = 0
    rawGrade = 0
    daysLate = 0
    latePenalty = 0
    finalGrade = 0

    print("=====================================")
    print("Student ID: ", studentID, "\n[ENTER EMPTY VALUES IF NO SUBMISSION/NO LATE SUBMISSION]")
    print("=====================================")

    # Input validation for test grade, code grade and days late
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
    
    # Calculate late penalty, raw grade, and final grade
    latePenalty = 5 * int(daysLate)
    print("Late penalty: ", latePenalty * -1, "(" + str(daysLate) + " days late)")

    rawGrade = (int(testGrade) + int(codeGrade)) / 2
    print("Student", str(studentID) + "'s raw grade: ", rawGrade)

    finalGrade = rawGrade - latePenalty

    # Final grade cannot be less than 0, a constraint
    if finalGrade < 0:
        finalGrade = 0
    
    print("Student", str(studentID) + "'s final grade: ", finalGrade)
    
    # Check if user is done grading
    isDone = input("Are you done grading? (Y/N): ").upper()
    if isDone == "Y":
        isDone = True
    else:
        isDone = False
        studentID += 1
    print()

print("=====================================")
print("Grading completed. Thank you!")
    

#! No test tables needed for this program