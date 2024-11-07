# Adkhy_Giga 201847335  October2024 CA-4.py
# Grading program - inserts raw grade and days late, calculates final grade, starts with student ID 1 and goes up to 176

isDone = False
studentID = 1

while studentID <= 176 and isDone != True:
    rawGrade = 0
    daysLate = 0
    latePenalty = 0
    finalGrade = 0

    print("=====================================")
    print("Student ID: ", studentID, "\n[ENTER EMPTY VALUES IF NO SUBMISSION/NO LATE SUBMISSION]")
    print("=====================================")

    rawGrade = input("Enter the raw grade (0 - 100): ")
    if rawGrade == "":
        rawGrade = 0

    while str(rawGrade).isnumeric() == False or int(rawGrade) < 0 or int(rawGrade) > 100:
        rawGrade = input("Invalid input. Please enter an integer between 0 and 100: ")

    daysLate = input("Enter the number of days late (0 - 2): ")
    if daysLate == "":
        daysLate = 0
    while str(daysLate).isnumeric() == False or int(daysLate) < 0 or int(daysLate) > 2:
        daysLate = input("Invalid input. Please enter an integer between 0 and 2: ")
    
    latePenalty = 5 * int(daysLate)
    print("Late penalty: ", latePenalty, "(" + str(daysLate) + " days late)")
    finalGrade = int(rawGrade) - int(latePenalty)
    
    print("The student's final grade is: ", finalGrade)
    
    isDone = input("Are you done grading? (Y/N): ").upper()
    if isDone == "Y":
        isDone = True
    else:
        isDone = False
        studentID += 1
    