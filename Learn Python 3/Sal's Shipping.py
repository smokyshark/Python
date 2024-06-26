#Sal's Shipping
weight = 4.8
cost_ground = 20.00
#Ground Shipping
print("Ground Shipping: $")
if weight > 0 and weight <= 2:
  cost_ground += weight * 1.50
  print(cost_ground)
elif weight > 2 and weight <= 6:
  cost_ground += weight * 3.00
  print(cost_ground)
elif weight > 6 and weight <= 10:
  cost_ground += weight * 4.00
  print(cost_ground)
elif weight > 10:
  cost_ground += weight * 4.75
  print(cost_ground)
else:
  print("You have provided the wrong weight.")

cost_ground_premium = 125.00
print("Ground Shipping Premium $",cost_ground_premium)

#Drone Shipping
print("Drone Shipping: $")
if weight > 0 and weight <= 2:
  cost_drone = weight * 4.50
  print(cost_drone)
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
  print(cost_drone)
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
  print(cost_drone)
elif weight > 10:
  cost_drone = weight * 14.25
  print(cost_drone)
else:
  print("You have provided the wrong weight.")
if cost_ground < cost_ground_premium and cost_ground < cost_drone:
  print("The cheapest way to deliver your package is Ground Shipping and costs: $", cost_ground)
elif cost_drone < cost_ground and cost_drone < cost_ground_premium:
  print("The cheapest way to deliver your package is Drone Shipping and costs $", cost_drone)
else:
  print("The cheapest way to deliver your package is Ground Shipping Premium and costs $", cost_ground_premium)
