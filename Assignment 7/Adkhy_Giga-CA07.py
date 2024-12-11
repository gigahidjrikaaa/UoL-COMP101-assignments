# Adkhy_Giga Dec2024 CA-07.py
# Breaking-Even Point for Theatre Seating Dashboard

def getBreakEvenPoint(production_cost, revenue):
    '''
    Takes in the production cost and selling price for band A and calculates the break-even point.
    '''
    break_even_point = production_cost / revenue
    rounded_break_even_point = int(-(-break_even_point // 1))
    return rounded_break_even_point

def getInputs():
    '''
    Takes in the production cost and selling price for band A.
    '''
    production_cost = int(input("Enter the production cost: "))
    price_seat_A = int(input("Enter the selling price for seat at band A: "))
    price_seat_B = 2 * price_seat_A
    return production_cost, price_seat_A, price_seat_B

def main():
    '''
    Main function to call the other functions.
    '''
    production_cost, price_seat_A, price_seat_B = getInputs()


if __name__ == "__main__":
    main()