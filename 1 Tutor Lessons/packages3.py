# Assignment - Packages
# Classes are not necessary for smaller assignments/applications - there is a lot of overhead and intellectual demand
# this is between 100 and 200 lines of code // Classes are going out of favour, in favour of Functional Programming
# Dictionary rather Class here
# have to figure out what the separate dictionary for reference information would hold
import pprint  

print() 

"""def get_input():                                                                 #originally all the input and declared variables were together
    shipment_quote = {}
    print()
    shipment_quote["customer_name"] = input("Customer name: ")    
    shipment_quote["weight_kg"] = int(input("Package weight in kilograms: "))
    shipment_quote["cubic_meters"] = int(input("Cubic meters of package: ")) #I have them doing the math outside of program
    shipment_quote["dangerous"] = input("Dangerous goods? (y/n): ")
    return shipment_quote        """                                                # broke it up so I'm not asking for more info than I need to establish can_ship

def get_input():
    shipment_quote = {                                                              # nested dictionary version
        "customer_name": {"name": "Customer name", "value": None},
        "weight_kg": {"name": "Package weight (kg)", "value": None},                # how do I add the Int here // changed from None to 0 to get integer but the input from user still text
        "cubic_meters": {"name": "Package volume (cubic meters)", "value": None},   # how do I add the Int here // changed from None to 0 to get integer but the input from user still text
        "dangerous": {"name": "Dangerous goods? (y/n)", "value": None}              # will need to translate to True False
    }
    for field_name, value in shipment_quote.items():    
        shipment_quote[field_name]["value"] = input(shipment_quote[field_name]["name"] + ": ") # cannot bounce out before dangerous if too heavy or too large
    return shipment_quote

def evaluate_package(shipment_quote):
    shipment_quote["weight_kg"]["value"] = int(shipment_quote["weight_kg"]["value"])                        
    shipment_quote["cubic_meters"]["value"] = int(shipment_quote["cubic_meters"]["value"])
    if ((shipment_quote["weight_kg"]["value"] >= 10) or (shipment_quote["cubic_meters"]["value"] >= 125)):          # too heavy, too voluminous
        shipment_quote["can_ship"]["value"] = "False" 
        print("We cannot ship your package because it is either more than 10kg or more than 125 cubic meters.")                
        print()
                                 # exit() quit() both bounce me entirely out of the program and I cannot use break or continue here
    else: 
        shipment_quote["can_ship"]["value"] = "True"                    
    return(shipment_quote)

def declare_variables(shipment_quote):
   
    shipment_quote["can_ship"]["value"] = None                                       # confirm that this retains the items input above
    shipment_quote["air_possible"]["value"] = None                                   # use None for defaults for safety and debugging
    shipment_quote["ship_ground_nonurgent_cost"]["value"] = None                     # None is a value that means I don't have a value yet = built into Python, like True or False
    shipment_quote["ship_ground_urgent_cost"]["value"] = None
    shipment_quote["ship_ocean_cost"]["value"] = None
    shipment_quote["ship_air_cost_kg"]["value"] = None
    shipment_quote["ship_air_cost_cm"]["value"] = None                          
    return shipment_quote



"""def validate_data(shipment_quote):                                          # not working but hasn't broken anything else
    print("testing if validate_data is ever opened")
    if ((shipment_quote["dangerous"] == "Y") or (shipment_quote["dangerous"]=="y") or (shipment_quote["dangerous"]=="Yes") or (shipment_quote["dangerous"]=="yes") or (shipment_quote["dangerous"]=="YES")):
        shipment_quote["dangerous"] = True
    if ((shipment_quote["dangerous"] == "N") or (shipment_quote["dangerous"]=="n") or (shipment_quote["dangerous"]=="No") or (shipment_quote["dangerous"]=="no") or (shipment_quote["dangerous"]=="NO")):
        shipment_quote["dangerous"] = False
    if ((shipment_quote["dangerous"] != True) or (shipment_quote["dangerous"] != False)):
        print("Invalid value for Dangerous.")
    return(shipment_quote)"""

def calculate_ocean(shipment_quote):                                                  # ocean
    if shipment_quote["can_ship"]["value"] == "True":
        shipment_quote["ship_ocean_cost"]["value"] = 30                                         # cost for ocean flat rate
                                                                                                          
    return(shipment_quote)    


def calculate_air(shipment_quote):                                                            # air
    if ((shipment_quote["dangerous"]["value"] == "y") or (shipment_quote["can_ship"]["value"] == "False")):    # removed if ((shipment_quote["heavy"] == "y") or
        shipment_quote["air_possible"]["value"] = "False"
    else:
        shipment_quote["air_possible"]["value"] = "True"
    if shipment_quote["air_possible"]["value"] == "True":                                               # but this part is working
        shipment_quote["ship_air_cost_kg"]["value"] = (shipment_quote["weight_kg"]["value"] * 10)          # cost for air weight
        shipment_quote["ship_air_cost_cm"]["value"] = (shipment_quote["cubic_meters"]["value"] * 20)       # cost for air volume
    return(shipment_quote)

def calculate_ground(shipment_quote):                                                          # ground
    if shipment_quote["can_ship"]["value"] == "True":
        shipment_quote["ship_ground_nonurgent_cost"]["value"] = 25                                # cost for ground if not urgent flat rate
        shipment_quote["ship_ground_urgent_cost"]["value"] = 45                                   # cost for ground if urgent flat rate
    return(shipment_quote)    
                  
def fmi(shipment_quote):                                                             # prints it the way I prefer
    print("Shipment Quote Details")                                                  # complete dictionary
    print("-----------------------")
    for key, value in shipment_quote.items():
        #print("key=%s, value=%s" % (key, value))
        print(key, value)    
    for key, value in shipment_quote.items():
        print(key, )
    return(shipment_quote)

                                                         
def main():                                      
    while True:
        print()
        print("Shipment System")                               # not sure if this actually goes at the top or is a function that is called near the bottom
        print("Enter 1 to get a shipment quote.")              # I don't have this doing anything yet other than taking input
        #print("Enter 2 to update customer information.")
        print("Enter 3 to quit.")
        action = input("What would you like to do? ")

        if action == "1":
            shipment_quote = get_input()
            shipment_quote = evaluate_package(shipment_quote)    # this is not working bc of input being text and not taking my change to integer
            if shipment_quote["can_ship"] == "False":
                continue                                        # this way it still asks if dangerous even though we might already know it cannot be shipped        shipment_quote = declare_variables(shipment_quote)
            shipment_quote = calculate_ocean(shipment_quote)
            shipment_quote = calculate_air(shipment_quote)
            shipment_quote = calculate_ground(shipment_quote)
            print()
            shipment_quote = fmi(shipment_quote)
        if action == "3":
            break

if __name__ == "__main__":                        # name is special type of variable -->  called a dunder (double-underscore) // allows me to import from here to other programs 
    main()                                        # getting error here now 
                                                # writing this way means then entire .py file is now a module rather than just a script

import pprint                                   # pretty print, pprint
pprint.pprint(booking)
print()
print("fin")
print



# can we include the statements like "We cannot ship this package because too heavy and too voluminous" as key value pairs.  Key could be "message"
# to dos:
    # play w dictionary in dictionary - sample in tutor folder
    # change my y/n to True/False?? not sure if this is just part of what he has us doing next wk
    # We will rework my program next week
    # 
    # maybe:
    # > error msgs
    # > air cost will be x -- if air weight cost is larger than air volume cost, then print x.  Do I create a variable to hold the result of comparison?  Do I add a message in the key value pairs?

