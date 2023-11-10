# floors - floors quantity
# apartments_floor - apartments quantity on the floor
# apartment_number - apartment number
# entrance - entrance quantity (default: 5)
def get_apartment(floors, apartments_floor, apartment_number, entrance=5):
    if ((floors and apartments_floor and apartments_floor) > 0) and (
            apartment_number <= floors * apartments_floor * entrance):

        all_apartment_number = []
        all_apartment_number2 = []
        temp_apartment_counter = []

        # Get numbers apartments
        for x in range(floors * apartments_floor * entrance):
            all_apartment_number.append(x + 1)

        # Create double-array for division apartments into floors
        for number in all_apartment_number:
            if not number % apartments_floor:
                temp_apartment_counter.append(number)
                all_apartment_number2.append(temp_apartment_counter)
                temp_apartment_counter = []
            else:
                temp_apartment_counter.append(number)

        # Main logic
        for floor, apartments in enumerate(all_apartment_number2):
            if apartment_number in apartments:
                current_entrance = (floor // floors) + 1
                current_floor = (floor + 1) - floors * (current_entrance - 1)
                return (f"Your apartment with number: {apartment_number} is located as:"
                        f"\nEntrance: {current_entrance}\nFloor: {current_floor}")
    else:
        return f"You are entered incorrect values!"


print(get_apartment(5, 4, 83))
