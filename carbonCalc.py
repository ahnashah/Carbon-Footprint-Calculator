# Carbon Footprint Calculator for Vehicles

# Define emission factors (in grams of CO2 per kilometer) for different vehicle types
emission_factors = {
    "gasoline_car": 2.31,   # Example value, you can replace it with actual data
    "diesel_car": 2.68,    # Example value, you can replace it with actual data
    "electric_car": 0,     # Electric cars have no tailpipe emissions
}

# Function to calculate the carbon footprint
def calculate_carbon_footprint(vehicle_type, distance):
    if vehicle_type in emission_factors:
        emission_factor = emission_factors[vehicle_type]
        carbon_footprint = emission_factor * distance
        return carbon_footprint
    else:
        return "Invalid vehicle type."

# Input from the user
vehicle_type = input("Enter the vehicle type (gasoline_car, diesel_car, electric_car): ")
distance = float(input("Enter the distance traveled (in kilometers): "))

# Calculate and display the carbon footprint
carbon_footprint = calculate_carbon_footprint(vehicle_type, distance)
if isinstance(carbon_footprint, (float, int)):
    print(f"Carbon Footprint for the {vehicle_type}: {carbon_footprint} grams of CO2")
else:
    print(carbon_footprint)
