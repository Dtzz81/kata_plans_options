import pytest
from trip_budgeting.main import calculate_cost

def test_no_trip_taken():
    # Arrange

    # Act
    output = calculate_cost()

    # Assert
    expected_output = {
        "no_pass": 0,
        "half_fare_pass": 120,
        "tourist_pass": 431
    }

    assert output == expected_output

def test_one_way_to_zermatt():
    # Arrange
    itinerary_one_trip = [{"journey": "Geneva to Zermat", "price": 55}]

    # Act
    output = calculate_cost(itinerary_one_trip)

    # Assert
    expected_no_pass_value = 55

    assert output["no_pass"] == expected_no_pass_value
#Geneva - Zermatt: £55 (Day 1 - This trip will be bought for sure)

