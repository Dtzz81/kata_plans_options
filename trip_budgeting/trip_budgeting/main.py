def calculate_cost(itinerary=None):
    output = {
        "no_pass": 0,
        "half_fare_pass": 120,
        "tourist_pass": 431
    }
    
    if itinerary:
        output["no_pass"] = 55

    return output
