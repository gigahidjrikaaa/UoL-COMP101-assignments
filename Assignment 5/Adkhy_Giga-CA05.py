# Adkhy_Giga Nov2024 CA-5.py
# Asks the user for input from the Cryosat-2 readings - Calculate ice floe volume and check primes and odds - Output the volume and prime/odd status
 
def primeAndOddTest(checked_num):
    '''Function to check if a number is odd and prime using the trial division method (no return value)'''
    # Odd Test
    # Check if number is divisible by 2 (remainder is 0). If so, it is not odd
    if checked_num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
    
    # Prime Test - Trial Division Method
    # Check if number is 1 or less. If so, it is not prime
    notPrimeMsg = "Number is not prime."
    isPrimeMsg = "Number is prime."
    if checked_num <= 1:
        print(notPrimeMsg)
    # Check if number is divisible by any number from 2 to sqrt(checked_num) [rounded down to nearest integer]
    for i in range(2, int(checked_num ** 0.5) + 1): 
        if checked_num % i == 0:
            print(notPrimeMsg)    # if divisible by any of the values (remainder is 0), number is not prime. Otherwise, it is prime.
    print(isPrimeMsg)
    return ''

def getInput():
    '''Function to get input from user and return the values'''
    try:
        length = input("Enter the length of the ice floe: ")
        primeAndOddTest(int(length))
        width = input("Enter the width of the ice floe: ")
        primeAndOddTest(int(width))
        freeboard_height = input("Enter the freeboard height of the ice floe: ")
        primeAndOddTest(int(freeboard_height))
        return length, width, freeboard_height
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return getInput()   # Recursion to get input again if invalid input

def processData(length, width, freeboard_height):
    fullHeight = 9 * freeboard_height    # Freeboard height is 1/9th of the full ice floe height
    volume = length * width * fullHeight
    print("The volume of the ice floe is: ", volume)

    # Check if the volume is odd and prime
    primeAndOddTest(volume)

def dataOutput(draft):
    print(draft)
    return ''

def main():
    print("Welcome to the Cryosat-2 Ice Floe Volume Calculator!")
    while True:
        answer = input("Do you want to run the program? (Y/N)").upper()
        if answer == "Y":
            length, width, freeboard_height = getInput()
            processData(int(length), int(width), int(freeboard_height))
        elif answer == "N":
            print("Thank you for using the Cryosat-2 Ice Floe Volume Calculator!")
            break
        else:
            print("Invalid input. Please enter Y or N.")
            continue

if __name__ == "__main__":
    main()

"""
Prime and Odd Test Table
========================================================================================
| Input |           Expected Output           |             Actual Output           |
========================================================================================
|   1   | Number is not odd.                  | Number is not odd.                  
|       | Number is not prime.                | Number is not prime.
----------------------------------------------------------------------------------------
|   2   | Number is not odd.                  | Number is not odd.
|       | Number is prime.                    | Number is prime.
----------------------------------------------------------------------------------------
|   3   | Number is odd.                      | Number is odd.
|       | Number is prime.                    | Number is prime.
----------------------------------------------------------------------------------------
|   4   | Number is not odd.                  | Number is not odd.
|       | Number is not prime.                | Number is not prime.
----------------------------------------------------------------------------------------

"""
