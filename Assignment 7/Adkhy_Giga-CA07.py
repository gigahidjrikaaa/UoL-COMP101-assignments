# Adkhy_Giga Dec2024 CA-07.py
# Breaking-Even Point for Theatre Seating Dashboard

import random

def getBreakEvenPoint(production_cost, revenue):
    '''
    Takes in the production cost and selling price for band A and calculates the break-even point.
    '''
    break_even_point = production_cost / revenue
    rounded_break_even_point = int(-(-break_even_point // 1))   # Rounding UP to the nearest integer
    return rounded_break_even_point

def getInputs():
    '''
    Takes in the production cost and selling price for band A.
    '''
    production_cost = int(input("Enter the production cost: "))
    price_seat_A = int(input("Enter the selling price for seat at band A: "))
    price_seat_B = 2 * price_seat_A
    return production_cost, price_seat_A, price_seat_B

def displaySeatingMap(seating_map):
    '''
    Displays the seating map in a 2D matrix.
    '''
    for row in seating_map:     # Prints each row of the 2D list on a new line
        print(row)
    return

def getSeatsFullBooked(rows=4, columns=5, status='full'):
    '''
    Returns the number of booked seats in the theatre and the seating map, represented by 1s and 0s.
    Partially booked seating map uses a random number generator to book seats.
    '''
    if status == 'full':
        seating_map = [[1 for i in range(columns)] for j in range(rows)]                        # 2D list of 1s
        booked_seats = rows * columns
    elif status == 'partial':
        seating_map = [[random.choice([0, 1]) for i in range(columns)] for j in range(rows)]    # 2D list of 0s and 1s using random number generator
        booked_seats = sum([sum(row) for row in seating_map])                                   # Sum of all 1s in the 2D list
    print("Booked Seats: ", booked_seats)
    print("Seating Map: ", displaySeatingMap(seating_map))
    return booked_seats, seating_map

def main():
    '''
    Main function to call the other functions.
    '''
    production_cost, price_seat_A, price_seat_B = getInputs()
    getSeatsFullBooked()
    getSeatsFullBooked(status='partial')

if __name__ == "__main__":
    main()