# Assignment - Packages
# Classes are not necessary for smaller assignments/applications - there is a lot of overhead and intellectual demand
# this is between 100 and 200 lines of code // Classes are going out of favour, in favour of Functional Programming
# Dictionary rather Class here

#menu
print() 

print("Shipment System")                               # not sure if this actually goes at the top or is a function that is called near the bottom
print("Enter 1 to get a shipment quote.")              # I don't have this doing anything yet other than taking input
print("Enter 2 to update customer information.")
print("Enter 3 to complete shipment details.")
action = input("What would you like to do? ")

def get_input():                   # working
    shipment_quote = {}
    shipment_quote["customer_name"] = input("Customer name: ")    # we are creating a key in shipment_quote // dictionary has many key value pairs - even inside one package
    shipment_quote["weight_kg"] = input("Package weight in kilograms: ")
    shipment_quote["cubic_meters"] = input("Cubic meters of package: ") #I have them doing the math outside of program
    shipment_quote["deliver_by_date"] = input("Deliver by date: ")
    shipment_quote["dangerous"] = input("Dangerous goods (y/n): ")
    shipment_quote["urgent"] = input("Urgent (y/n): ")
    shipment_quote["international"] = input("International (y/n): ")  # i am not assuming that ocean assumes international
    print("The items in shipment_quote are: ")         # I could set can_ship, heavy, air_possible here
    print(shipment_quote)
    print()
    return shipment_quote

def eval_package():                            #not working
    if shipment_quote["weight_kg"] >= 10:                     # this would likely not get entered.  the clerk would just ask and then say we cannot ship
        print("Package is too heavy.")
        shipment_quote["can_ship"] = "n"
    else:
        shipment_quote["can_ship"] = "y"
    if shipment_quote["cubic_meters"] >= 125:                # does the length of each side also have to be less than 5 meters?  I only did cubic meters
        print("Package is too large.")
        shipment_quote["can_ship"] = "n"
    else:
        shipment_quote["can_ship"] = "y"
    if shipment_quote["weight_kg"] >= 7:                     # heavy was in the reqs --> I chose 7kg as the delimiter but could be a different value
        print ("Package is heavy therefore must be routed by ground or ocean.")
        shipment_quote["heavy"] = "y"
    else:
        shipment_quote["heavy"] = "n"
    if shipment_quote["can_ship"] == "n":
        print("We cannot ship this package.")
    return(shipment_quote)    

def routing():                               #not working
    if ((shipment_quote["can_ship"] == y) and (shipment_quote["dangerous"] == "y")):
        print("This package must be routed by ground or ocean.")
        shipment_quote["air_possible"] = "n"
    if ((shipment_quote["can_ship"] == y) and (shipment_quote["dangerous"] == "n")):
        print("This package can be routed by ground or ocean or air.")
        shipment_quote["air_possible"] = "y"
   
def cost():                                           # I've decided to put all the estimates in the quote
    shipment_quote["ship_air_cost_kg"] = (shipment_quote[weight_kg] * 10)
    shipment_quote["ship_air_cost_cf"] = (shipment_quote[cubic_meters] * 20)
    ship_ocean_cost = 30                              # do I try to make these numbers come back as dollars (is that a thing?) or just put a "$" in front of the answer
    shipment_quote["ship_ground_nonurgent_cost"] = 25
    shipment_quote["ship_ground_urgent_cost"] = 45

def estimate():    
    print("Estimated cost to ship by various routes: ")
    print("Ground Non-Urgent: $", ship_ground_nonurgent_cost)
    print("Ground Urgent: $", ship_ground_urgent_cost)
    print("Ocean: $", ship_ocean_cost)
    if shipment_quote["air_possible"] == "y":
        print("Air will be the larger of : $", ship_air_cost_kg, "or $", ship_air_cost_cf)

#for my information
def fmi(shipment_quote):
    print("Complete dictionary")
    for key, value in shipment_quote.items():
        print("key=%s, value=%s" % (key, value))
    return(shipment_quote)


                                                       # I have not yet tried to get the either or working here    
def main():                                      
    shipment_quote = get_input()
    shipment_quote = eval_package()     # line 88 error but I don't know why
    shipment_quote = routing()
    shipment_quote = cost()             # line 94 error but I don't understand it
    shipment_quote = estimate()
    shipment_quote = fmi()

if __name__ == "__main__":                        # name is special type of variable -->  called a dunder (double-underscore) // allows me to import from here to other programs 
    main()                                        # getting error here now # writing this way means then entire .py file is now a module rather than just a script

print()
print("still menu and larger value things to clean up")
print()
print


#if __name__ == "__eval_package__":
#    eval_package()                      # line 102 error but I don't understand it

#main()                 # naive, not good Python style