# Title: Programming with User-defined Functions - Practical Task 1
# Summary: This script calculates the total cost of a holiday including flight, hotel, and car rental costs.
# It uses user-defined functions to compute costs based on user inputs.
# Date: [Date of completion]

# Function to calculate hotel cost based on number of nights
def hotel_cost(num_nights):
    """
    Calculates the total cost of hotel stay based on the number of nights.

    Parameters:
    - num_nights (int): Number of nights staying at the hotel.

    Returns:
    - int: Total cost of the hotel stay.
    """
    hotel_fee_per_night = 260  # Cost per night at the hotel
    total_cost = num_nights * hotel_fee_per_night
    return total_cost

# Function to calculate flight cost based on selected city
def plane_cost(city_flight):
    """
    Calculates the flight cost based on the selected destination city.

    Parameters:
    - city_flight (int): Selected city for the flight (1 for Madagascar, 2 for Italy, 3 for China).

    Returns:
    - int: Cost of the flight to the selected city.
    """
    if city_flight == 1:
        flight_choice = 2500
    elif city_flight == 2:
        flight_choice = 800
    elif city_flight == 3:
        flight_choice = 1250
    else:
        print("You did not select a valid flight option.")
        flight_choice = 0  # Default value for invalid input
    return flight_choice

# Function to calculate car rental cost based on number of days
def car_rental(rental_days):
    """
    Calculates the total cost of car rental based on the number of days.

    Parameters:
    - rental_days (int): Number of days for which the car is rented.

    Returns:
    - int: Total cost of car rental for the specified days.
    """
    car_rental_daily_fee = 100  # Daily rental fee for the car
    total_cost = rental_days * car_rental_daily_fee
    return total_cost

# Function to calculate total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    """
    Calculates the total cost of the holiday including flight, hotel, and car rental costs.

    Parameters:
    - num_nights (int): Number of nights staying at the hotel.
    - city_flight (int): Selected city for the flight (1 for Madagascar, 2 for Italy, 3 for China).
    - rental_days (int): Number of days for which the car is rented.

    Returns:
    - int: Total cost of the holiday.
    """
    # Calculate individual costs
    total_hotel_cost = hotel_cost(num_nights)
    total_flight_cost = plane_cost(city_flight)
    total_car_cost = car_rental(rental_days)

    # Calculate total holiday cost
    total_cost = total_hotel_cost + total_flight_cost + total_car_cost
    return total_cost

# Main program
if __name__ == "__main__":
    # Prompt user for inputs
    city_flight = int(input("To fly to Madagascar type '1', to fly to Italy, type '2', or to fly to China type '3': "))
    num_nights = int(input("Enter the number of nights you plan to stay: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    # Calculate and print total holiday cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)
    print(f"Therefore, your total holiday cost is: £{total_cost}")