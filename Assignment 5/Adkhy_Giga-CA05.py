# Adkhy_Giga Nov2024 CA-5.py
# Asks the user for input from the Cryosat-2 readings - Calculate ice floe volume and check primes and odds - Output the volume and prime/odd status
 
def primeAndOddTest():
    '''Function to check if a number is odd and prime using the trial division method (no return value)'''
    odd_status = "odd"
    prime = "prime"

    print("===== Prime Calculator =====")
    checked_num = input("Enter any number that you want to check: ")
    
    # Check if number is divisible by 2 (remainder is 0). If so, it is even.
    if checked_num % 2 == 0:
        odd_status = "even"
    
    # Prime Test - Trial Division Method
    # Check if number is greater than 1. If not, it is not prime.
    if checked_num > 1:
        # Check if number is divisible by any number from 2 to sqrt(checked_num) inclusive [rounded down to nearest integer]. If not divisible then it is prime.
        for i in range(2, int(checked_num ** 0.5) + 1): 
            if checked_num % i == 0:
                prime = "not prime"
                break
    else:
        prime = "not prime"
        
    # Output the test results
    print(checked_num, "is", odd_status, "and is" , prime + ".\n")
    print("=====================================")


def getInput():
    '''Function to get input from user and return the values'''
    print("Welcome to the Cryosat-2 Ice Floe Volume Calculator!")
    try:        # Exception handling for invalid input
        length = input("\nEnter the length of the ice floe: ")
        width = input("Enter the width of the ice floe: ")
        freeboard_height = input("Enter the freeboard height of the ice floe: ")
        return length, width, freeboard_height
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return getInput()   # Recursion to get input again if invalid input

def processData(length, width, freeboard_height):
    '''Function to process the dimensions and calculate the volume of the ice floe'''
    full_height = 9 * freeboard_height    # Freeboard height is 1/9th of the full ice floe height
    volume = length * width * full_height
    draft = full_height - freeboard_height

    return volume, draft, full_height

def dataOutput(length, width, freeboard_height, volume, draft, full_height):
    '''Function to output the volume and summary of the reading from input'''
    print("The volume of the ice floe is", volume, "m^3.")

    # Output the summary
    print("=====================================")
    print("===== CRYOSAT-2 READING SUMMARY =====")
    print("=====================================")
    print("Length\t\t\t: ", length, "m")
    print("Width\t\t\t: ", width, "m")
    print("Freeboard height\t: ", freeboard_height, "m")
    print("Draft\t\t\t: ", draft, "m")
    print("Total height\t\t: ", full_height, "m")
    print("Volume\t\t\t: ", volume, "m^3")
    print("=====================================")
    
    return ''

def main():
    while True:
        print("=====================================")
        answer = input("Do you want to run the program? (Y/N): ").upper()
        if answer == "Y":       # Perform the modules
            primeAndOddTest()
            length, width, freeboard_height = getInput()
            volume, draft, full_height = processData(int(length), int(width), int(freeboard_height))
            dataOutput(length, width, freeboard_height, volume, draft, full_height)
        elif answer == "N":     # Exit the program with user-facing message
            print("\n=====================================")
            print("Exiting the program... Have a good day!")
            print("=====================================")
            break
        else:
            print("Invalid input. Please enter Y or N.")
            continue

if __name__ == "__main__":
    main()

"""
Prime and Odd Test Table
============================================================================================================================
| Input |               Expected Output                 |                   Actual Output                  |    COMMENT    |
============================================================================================================================
|   2   | 2 is even and is prime.                       | 2 is even and is prime.                          |    OK         |
|   3   | 3 is odd and is prime.                        | 3 is odd and is prime.                           |    OK         |
|   4   | 4 is even and is not prime.                   | 4 is even and is not prime.                      |    OK         |
|   10  | 10 is even and is not prime.                  | 10 is even and is not prime.                     |    OK         |
|   11  | 11 is odd and is prime.                       | 11 is odd and is prime.                          |    OK         |
|  2301 | 2301 is odd and is not prime.                 | 2301 is odd and is not prime.                    |    OK         |
| 11027 | 11027 is odd and is prime.                    | 11027 is odd and is prime.                       |    OK         |
|   0   | 0 is even and is not prime.                   | 0 is even and is not prime.                      |    OK         |
============================================================================================================================
"""
