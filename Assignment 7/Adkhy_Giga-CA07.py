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

def displayMap(seating_map):
    '''
    Displays the seating map in a 2D matrix.
    '''
    for row in seating_map:
        print(row)
    return

def getProgrammeStatus(seating_map, booked_seats, rows=4, columns=5, booking_status='full'):
    programmes_map = []
    if booking_status == 'full':
        for j in range(rows):
            row = []
            for i in range(columns):
                if seating_map[j][i] == 1:
                    row.append(random.choice([0, 1]))
            else:
                row.append(0)
            programmes_map.append(row)
        programmes_purchased = sum([sum(row) for row in programmes_map])  # Sum of all 1s in the programmes map
    elif booking_status == 'partial':
        programmes_map = seating_map
        programmes_purchased = booked_seats
    return programmes_map, programmes_purchased
        

def getSeatsStatus(rows=4, columns=5, booking_status='full'):
    '''
    Returns the number of booked seats in the theatre and the seating map, represented by 1s and 0s.
    Partially booked seating map uses a random number generator to book seats.
    Also returns the number of extra programmes purchased [partial -> everyone buys, full -> use RNG].
    '''
    if booking_status == 'full':
        seating_map = [[1 for i in range(columns)] for j in range(rows)]                        # 2D list of 1s
        booked_seats = rows * columns
        programmes_map, programmes_purchased = getProgrammeStatus(seating_map, booked_seats, booking_status='full')
    elif booking_status == 'partial':
        seating_map = [[random.choice([0, 1]) for i in range(columns)] for j in range(rows)]    # 2D list of 0s and 1s using random number generator
        booked_seats = sum([sum(row) for row in seating_map])                                   # Sum of all 1s in the 2D list
        programmes_map, programmes_purchased = getProgrammeStatus(seating_map, booked_seats, booking_status='partial')
    lineSeparator()
    print("Booked Seats: ", booked_seats)
    print("Programmes Purchased: ", programmes_purchased)
    print("Seating Map:")
    displayMap(seating_map)
    lineSeparator()
    print("Programmes Map:")
    displayMap(programmes_map)
    
    return booked_seats, seating_map, programmes_map, programmes_purchased

def getRevenue(seating_map, programmes_map, price_seat_A, price_seat_B, programmes_purchased):
    '''
    Returns the revenue generated from the booked seats.
    '''
    total_revenue_no_prog = 0
    total_revenue_prog = 0
    revenue_seat_a_no_prog = 0
    revenue_seat_a_prog = 0
    revenue_seat_b_no_prog = 0
    revenue_seat_b_prog = 0
    programme_revenue = 0
    seats_a_sold = 0
    seats_b_sold = 0
    row_revenue_no_prog = [0, 0, 0, 0]
    row_revenue_prog = [0, 0, 0, 0]
    for i in range(len(seating_map)):
        if i < 2:
            row_revenue_no_prog[i] = sum(seating_map[i]) * price_seat_A
            revenue_seat_a_no_prog += row_revenue_no_prog[i]
            row_revenue_prog[i] = row_revenue_no_prog[i] + sum(programmes_map[i]) * PROGRAMME_COST
            revenue_seat_a_prog += row_revenue_prog[i]
            seats_a_sold += sum(seating_map[i])
        else:
            row_revenue_no_prog[i] = sum(seating_map[i]) * price_seat_B
            revenue_seat_b_no_prog += row_revenue_no_prog[i]
            row_revenue_prog[i] = row_revenue_no_prog[i] + sum(programmes_map[i]) * PROGRAMME_COST
            revenue_seat_b_prog += row_revenue_prog[i]
            seats_b_sold += sum(seating_map[i])
    programme_revenue += programmes_purchased * PROGRAMME_COST
    total_revenue_no_prog = revenue_seat_a_no_prog + revenue_seat_b_no_prog
    total_revenue_prog = revenue_seat_a_prog + revenue_seat_b_prog

    lineSeparator()
    print("Revenue Breakdown:")
    print("SEATS A:", seats_a_sold, "SEATS B:", seats_b_sold)
    print("Revenue from Seats A without Programmes: ", revenue_seat_a_no_prog)
    print("Revenue from Seats A with Programmes: ", revenue_seat_a_prog)
    print("Revenue from Seats B without Programmes: ", revenue_seat_b_no_prog)
    print("Revenue from Seats B with Programmes: ", revenue_seat_b_prog)
    print("Revenue from each rows:")
    for i in range(len(row_revenue_no_prog)):
        print("Row", i+1, ":", row_revenue_no_prog[i], "\t||\t", row_revenue_prog[i])
    print("Programme Revenue: ", programme_revenue)
    print("Total revenue without Programmes: ", total_revenue_no_prog)
    print("Total revenue with Programmes: ", total_revenue_prog)
    

    return

def main():
    production_cost, price_seat_A, price_seat_B = getInputs()

    # Full Booking Status
    full_booked_seats, full_seating_map, full_programmes_map, full_programmes_purchased = getSeatsStatus()
    full_revenue = getRevenue(full_seating_map, full_programmes_map, price_seat_A, price_seat_B, full_programmes_purchased)

if __name__ == "__main__":
    main()