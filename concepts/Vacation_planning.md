TAKING A VACATION

1. Planning Your Trip
- When planning a vacation, it’s very important to know exactly how much you’re going to spend.

    def hotel_cost(nights):
    return 140 * nights

2. Getting There
 - You’re going to need to take a plane ride to get to your location.

  def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

  3. Transportation
  - You’re also going to need a rental car in order for you to get around.
  def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
  	cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

  4. Pull it Together
  - Great! Now that you’ve got your 3 main costs figured out, let’s put them together in order to find the total cost of your trip.
  Notice that we changed the argument of hotel_costs() from nights to days - 1. Since we want trip-cost to only depend on two parameters, we have to convert the variable nights into days.

  def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

"""You cant expect to only spend money on the plane ride, hotel, and rental car when going on a vacation. There also needs to be room for additional costs like fancy food or souvenirs."""
# Modifying your trip_cost function definition. Add a third argument, spending_money.

  5. Plan Your Trip!
  - Nice work! Now that you have it all together, let’s take a trip.

  What if we went to Los Angeles for 5 days and brought an extra 600 dollars of spending money?
  we write:
  print trip_cost("Los Angeles", 5, 600)
