# This defines the number of cars we have
cars = 100
# Here we have how much space is in each car
space_in_a_car = 4.0
# This defines how many drivers we have
drivers = 30
# This is the number of passengers we have
passengers = 90
# Any car without a driver, is not driven!
cars_not_driven = cars - drivers
# For every driver, we have a car being driven
cars_driven = drivers
# Only cars that are driven are counted in carpool_capacity
carpool_capacity = cars_driven*space_in_a_car
# This just tells us the average
average_passengers_per_car = passengers / cars_driven


# These lines will provide for the above variables a more human explanation
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
