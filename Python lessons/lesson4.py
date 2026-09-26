# Day 4 - Weight converter (lbs to kg)
weight_lbs = input('Weight (lbs): ')
weight_kg = float(weight_lbs) * 0.45  # float (not int) so decimals like 150.5 work
print(weight_kg)
