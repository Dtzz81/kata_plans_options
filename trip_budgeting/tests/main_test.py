from unittest.mock import patch
import pytest
from trip_budgeting.main import calculate_cost
from trip_budgeting.main import get_option

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

def test_train_to_zermatt_and_back():
    # Arrange
    itinerary_there_and_back = [{"journey": "Geneva to Zermat", "price": 55}, {"type": "TRAIN",
        "journey": "Visp - Geneva",
        "price": 35,}]

    # Act
    output = calculate_cost(itinerary_there_and_back)

    # Assert
    expected_no_pass_value = 90

    assert output["no_pass"] == expected_no_pass_value

def test_no_trip_taken_with_half_fare():

    output = calculate_cost()

    # Assert
    expected_output = {
        "no_pass": 0,
        "half_fare_pass": 120,
        "tourist_pass": 431
    }

    assert output == expected_output

def test_get_option_a():
    with patch('builtins.input', return_value='a'):
        result = get_option()
        assert result == "no_pass"
