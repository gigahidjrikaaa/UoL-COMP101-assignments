# Adkhy_Giga Dec2024 CA-07.py
# Breaking-Even Point for Theatre Seating Dashboard

import random

PROGRAMME_COST = 10

def lineSeparator(length=50):
    '''
    Prints a line separator.
    '''
    print("=" * length)
    return

def getBreakEvenPoint(production_cost, revenue):
    '''
    Returns the break-even point for the theatre seating dashboard.
    '''
    break_even_point = production_cost / revenue
    rounded_break_even_point = int(-(-break_even_point // 1))   # Rounding UP to the nearest integer
    return rounded_break_even_point

def getInputs():
    '''
    Returns the production cost and selling prices for seats at band A and B.
    '''
    production_cost = int(input("Enter the production cost: "))
    price_seat_A = int(input("Enter the selling price for seat at [BAND A]: "))
    price_seat_B = price_seat_A / 2
    return production_cost, price_seat_A, price_seat_B

def displaySeatingMap(seating_map):
    '''
    Displays the seating map in a 2D matrix.
    '''
    print("Seating Map:")
    for row in seating_map:
        print(row)
    return

def getSeatsStatus(rows=4, columns=5, booking_status='full'):
    '''
    Returns the number of booked seats in the theatre and the seating map, represented by 1s and 0s.
    Partially booked seating map uses a random number generator to book seats.
    Also returns the number of extra programmes purchased [partial -> everyone buys, full -> use RNG].
    '''
    if booking_status == 'full':
        seating_map = [[1 for i in range(columns)] for j in range(rows)]                        # 2D list of 1s
        booked_seats = rows * columns
        programmes_purchased = random.randint(1, booked_seats)                                  # Random number of programmes purchased
    elif booking_status == 'partial':
        seating_map = [[random.choice([0, 1]) for i in range(columns)] for j in range(rows)]    # 2D list of 0s and 1s using random number generator
        booked_seats = sum([sum(row) for row in seating_map])                                   # Sum of all 1s in the 2D list
        programmes_purchased = booked_seats
    lineSeparator()
    print("Booked Seats: ", booked_seats)
    print("Programmes Purchased: ", programmes_purchased)
    displaySeatingMap(seating_map)
    return booked_seats, seating_map, programmes_purchased

def getRevenue(seating_map, price_seat_A, price_seat_B, programmes_purchased):
    '''
    Returns the revenue generated from the booked seats.
    '''
    total_revenue, revenue_seat_a, revenue_seat_b, programme_revenue = 0
    for i in range(len(seating_map)):
        if i < 2:
            revenue_seat_a += sum(seating_map[i]) * price_seat_A
        else:
            revenue_seat_b += sum(seating_map[i]) * price_seat_B
    programme_revenue += programmes_purchased * PROGRAMME_COST
    total_revenue = revenue_seat_a + revenue_seat_b + programme_revenue
    return total_revenue

def main():
    production_cost, price_seat_A, price_seat_B = getInputs()

    # Full Booking Status
    full_booked_seats, full_seating_map, full_programmes_purchased = getSeatsStatus()
    full_revenue = getRevenue(full_seating_map, price_seat_A, price_seat_B, full_programmes_purchased)
    full_break_even_point = getBreakEvenPoint(production_cost, full_revenue)
    lineSeparator()
    print("Full Booking Status")
    print("Revenue: ", full_revenue)
    print("Break-even Point: ", full_break_even_point)
    lineSeparator()

    # Partial Booking Status
    partial_booked_seats, partial_seating_map, partial_programmes_purchased = getSeatsStatus(booking_status='partial')
    partial_revenue = getRevenue(partial_seating_map, price_seat_A, price_seat_B, partial_programmes_purchased)
    partial_break_even_point = getBreakEvenPoint(production_cost, partial_revenue)
    lineSeparator()
    print("Partial Booking Status")
    print("Revenue: ", partial_revenue)
    print("Break-even Point: ", partial_break_even_point)
    lineSeparator()

if __name__ == "__main__":
    main()