booking = {
    "customer_name": {"name": "Customer name", "value": None},
    "weight_kg": {"name": "Weight in Kg", "value": None},
    "volume_m3": {"name": "Volume in cubic meters", "value": None},
}
print("BOOKING DICTIONARY")
for field_name, value in booking.items():
    booking[field_name]["value"] = input(booking[field_name]["name"] + ": ")

print(booking["weight_kg"])
print(booking["weight_kg"]["value"])
booking["weight_kg"]["value"] = float(booking["weight_kg"]["value"])
print(type(booking["weight_kg"]["value"]))
print()
#####################################################
print()
print("CATEGORIES DICTIONARY")
categories = {
    "category": "fruit"{"product": "apple", "cost": "1"},
    "category": "fruit"{"product": "pear", "cost": "2"},
    "category": "vegetable"{"product": "carrots - 1 lb", "cost": "2"},
    "category": "vegetable"{"product" : "potatoes - 5 lbs", "cost" :"5"},
    "category": "meat"{"product": "hamburger - 2 lbs", "cost" : "6"},
}
print(categories)
print()

#################################################



