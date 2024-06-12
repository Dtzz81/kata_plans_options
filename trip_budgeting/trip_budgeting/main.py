def get_option():
    while True:
        print("Choose an option:")
        print("a - No Pass")
        print("b - Half Fare Pass")
        print("c - Tourist Pass")
        option = input("Which option did you select?: ").lower()
        if option in ['a', 'b', 'c']:
            if option == 'a':
                return "no_pass"
            elif option == 'b':
                return "half_fare_pass"
            elif option == 'c':
                return "tourist_pass"
        else:
            print("Invalid option. Please choose a valid option (a, b, or c).")

which_option = get_option()

def calculate_cost(itinerary=None):
    output = {
        "no_pass": 0,
        "half_fare_pass": 120,
        "tourist_pass": 431
    }

    if itinerary:
        total_cost = 0
        for trip in itinerary:
            total_cost += trip["price"]
        output["no_pass"] = total_cost

    return output
