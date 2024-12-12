# Adkhy_Giga Dec2024 CA-07.py
# Breaking-Even Point for Theatre Seating Dashboard

import random

PROGRAMME_COST = 10
ROWS = 4
COLUMNS = 5

def lineSeparator(length=50):
    '''
    Prints a line separator.
    '''
    print("=" * length)

def printCenteredText(text, length=50):
    '''
    Prints centered text.
    '''
    print(text.center(length, " "))

def printTitle(title, length=50):
    '''
    Prints a title with line separator.
    '''
    lineSeparator()
    printCenteredText(title, length)

def getBreakEvenPoint(production_cost: int, revenue: int):
    '''
    Returns the break-even point in days (rounded up).
    '''
    break_even_point = production_cost / revenue   
    return int(-(-break_even_point // 1))   # Rounding UP to the nearest integer

def getInputs():
    '''
    Returns the production cost and selling prices for seats at band A and B.
    '''
    production_cost = int(input("Enter the production cost: "))
    price_seat_A = int(input("Enter the selling price for seat at [BAND A]: "))
    price_seat_B = price_seat_A / 2
    print("*" * 50 + "\n")
    return production_cost, price_seat_A, price_seat_B

def displayMap(seating_map: list):
    '''
    Displays the seating map in a 2D matrix of 1s and 0s.
    '''
    for row in seating_map:
        printCenteredText(str(row) + " = " + str(sum(row)) + " orders")
    printCenteredText("Total: " + str(sum([sum(row) for row in seating_map])) + str(" orders"))   # Sum of all 1s in the 2D list (shorthand)

def getProgrammeStatus(seating_map: list, rows=ROWS, columns=COLUMNS, booking_status='full'):
    '''
    Returns the number of extra programmes purchased and the programmes map, represented by 1s and 0s.
    Full booking status uses a random number generator for programmes purchase, while partial booking status uses the seating map.
    '''
    programmes_map = []
    if booking_status == 'full':
        for j in range(rows):
            row = []
            for i in range(columns):
                if seating_map[j][i] == 1:
                    row.append(random.choice([0, 1]))   # Randomly assign 0 or 1 to each seat, add to the row list
            programmes_map.append(row)                  # Add the row list to the programmes map list
    elif booking_status == 'partial':
        programmes_map = seating_map
    programmes_purchased = sum([sum(row) for row in programmes_map])  # Sum of all 1s in the seating map
    return programmes_map, programmes_purchased
        

def getSeatsStatus(rows=ROWS, columns=COLUMNS, booking_status='full'):
    '''
    Returns the number of booked seats in the theatre and the seating map, represented by 1s and 0s.
    Partially booked seating map uses a random number generator to book seats.
    Also returns the number of extra programmes purchased [partial -> everyone buys, full -> use RNG].
    '''
    if booking_status == 'full':
        seating_map = [[1 for i in range(columns)] for j in range(rows)]                        # 2D list of 1s
        programmes_map, programmes_purchased = getProgrammeStatus(seating_map, booking_status='full')
    elif booking_status == 'partial':
        seating_map = [[random.choice([0, 1]) for i in range(columns)] for j in range(rows)]    # 2D list of 0s and 1s using random number generator                                  # Sum of all 1s in the 2D list
        programmes_map, programmes_purchased = getProgrammeStatus(seating_map, booking_status='partial')
    printTitle("SEATING MAP")
    displayMap(seating_map)
    printTitle("PROGRAMMES MAP")
    displayMap(programmes_map)
    
    return seating_map, programmes_map, programmes_purchased

def printLegend():
    '''
    Prints the legend for the revenue report.
    '''
    print("WITHOUT PROGRAMMES\t||\tWITH PROGRAMMES")
    lineSeparator()

def showRevenueReport(seating_map: list, programmes_map: list, price_seat_A, price_seat_B, programmes_purchased, production_cost=0):
    '''
    Returns the revenue generated from the booked seats.
    '''
    revenue_seat_a_no_prog = revenue_seat_a_prog = 0
    revenue_seat_b_no_prog = revenue_seat_b_prog = 0
    seats_a_sold = seats_b_sold = 0
    row_revenue_no_prog = row_revenue_prog = [0] * ROWS
    programme_revenue = 0

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
    break_even_no_prog = getBreakEvenPoint(production_cost, total_revenue_no_prog)
    break_even_prog = getBreakEvenPoint(production_cost, total_revenue_prog)

    # Print Revenue Report
    printTitle("REVENUE REPORT")
    printTitle("SEATS SOLD")
    printCenteredText("TOTAL SEATS SOLD: " + str(seats_a_sold + seats_b_sold))
    print("BAND A:", seats_a_sold, "\t\t||\tBAND B:", seats_b_sold)
    printTitle("SEATING REVENUE")
    printLegend()
    print("Seat A: ", revenue_seat_a_no_prog, "\t\t||\t", revenue_seat_a_prog)
    print("Seat B: ", revenue_seat_b_no_prog, "\t\t||\t", revenue_seat_b_prog)
    printTitle("ROW REVENUE")
    printLegend()
    for i in range(len(row_revenue_no_prog)):
        print("Row", i+1, ":", row_revenue_no_prog[i], "\t\t||\t", row_revenue_prog[i])
    printTitle("PROGRAMME REVENUE")
    printCenteredText("Programmes Purchased: " + str(programmes_purchased))
    printCenteredText("Programme Revenue: " + str(programme_revenue))
    printTitle("TOTAL REVENUE & BREAK-EVEN POINT")
    printLegend()
    print("Total Revenue: ", total_revenue_no_prog, "\t||\t", total_revenue_prog)
    print("Break-even: ", break_even_no_prog, " days\t||\t", break_even_prog, " days")

def main():
    production_cost, price_seat_A, price_seat_B = getInputs()

    # Full Booking Status
    printTitle("FULL BOOKING STATUS")
    full_seating_map, full_programmes_map, full_programmes_purchased = getSeatsStatus()
    showRevenueReport(full_seating_map, full_programmes_map, price_seat_A, price_seat_B, full_programmes_purchased, production_cost)

    # Partial Booking Status
    print()
    printTitle("PARTIAL BOOKING STATUS")
    partial_seating_map, partial_programmes_map, partial_programmes_purchased = getSeatsStatus(booking_status='partial')
    showRevenueReport(partial_seating_map, partial_programmes_map, price_seat_A, price_seat_B, partial_programmes_purchased, production_cost)

if __name__ == "__main__":
    main()