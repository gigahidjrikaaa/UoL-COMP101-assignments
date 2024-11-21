# Adkhy_Giga Nov2024 CA-5.py
#
 
def PrimeAndOddTest(checked_num):
    '''Function to check if a number is odd and prime using the trial division method (no return value)'''
    # Odd Test
    # Check if number is divisible by 2 (remainder is 0). If so, it is not odd
    if checked_num % 2 == 0:
        print("Number is not odd.")
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

def GetInput():
    '''Function to get input from user and return the values'''
    length = input("Enter the length of the ice floe: ")
    width = input("Enter the width of the ice floe: ")
    breadth = input("Enter the breadth of the ice floe: ")
    return length, width, breadth

def ProcessData(length, width, breadth):
    # Calculate the volume of the ice floe
    volume = int(length) * int(width) * int(breadth)
    print("The volume of the ice floe is: ", volume)

    # Check if the volume is odd and prime
    PrimeAndOddTest(volume)

def DataOutput(draft):
    print(draft)
    return ''

def main():
    while True:
        answer = input("Welcome to ice floe program. Do you want to run the program? (Y/N)").upper()
        if answer == "Y":
            print("Running program...")
        elif answer == "N":
            print("Program is exiting... Goodbye!")
            break
        else:
            print("Invalid input. Please enter Y or N.")
            continue

if __name__ == "__main__":
    main()
