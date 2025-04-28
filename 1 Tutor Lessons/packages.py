# Assignment - Packages
# Classes are not necessary for smaller assignments/applications - there is a lot of overhead and intellectual demand
# this is between 100 and 200 lines of code // Classes are going out of favour, in favour of Functional Programming
# Dictionary rather Class here

#menu
print() 

def get_input():                              # working
    shipment_quote = {}
    shipment_quote["customer_name"] = input("Customer name: ")    # we are creating a key in shipment_quote // dictionary has many key value pairs - even inside one package
    shipment_quote["weight_kg"] = int(input("Package weight in kilograms: "))
    shipment_quote["cubic_meters"] = int(input("Cubic meters of package: ")) #I have them doing the math outside of program
    shipment_quote["deliver_by_date"] = input("Deliver by date: ")
    shipment_quote["dangerous"] = input("Dangerous goods (y/n): ")
    shipment_quote["urgent"] = input("Urgent (y/n): ")
    shipment_quote["international"] = input("International (y/n): ")  # i am not assuming that ocean assumes international
    shipment_quote["can_ship"] = "y"
    shipment_quote["heavy"] = "n"
    shipment_quote["air_possible"] = None                                   # use None for defaults for safety and debugging
    shipment_quote["ship_ground_nonurgent_cost"] = None                     # None is a value that means I don't have a value yet = built into Python, like True or False
    shipment_quote["ship_ground_urgent_cost"] = None
    shipment_quote["ship_ocean_cost"] = None
    shipment_quote["ship_air_cost_kg"] = None
    shipment_quote["ship_air_cost_cm"] = None
    print("The items in shipment_quote are: ")         
    print(shipment_quote)
    print()
    return shipment_quote

def eval_package(shipment_quote):                            # not working
    if shipment_quote["weight_kg"] >= 10:                     # this would likely not get entered.  the clerk would just ask and then say we cannot ship
        shipment_quote["can_ship"] = "n"                 # it was also going to print The package is too heavy.
    if shipment_quote["cubic_meters"] >= 125:                # does the length of each side also have to be less than 5 meters?  I only did cubic meters
        shipment_quote["can_ship"] = "n"                # it was also going to print The package is too large.
    if shipment_quote["weight_kg"] >= 7:                     # heavy was in the reqs --> I chose 7kg as the delimiter but could be a different value
        shipment_quote["heavy"] = "y"                   # it was also going to print The package is heavy but can be shipped by ground or ocean.
    if shipment_quote["can_ship"] == "n":
        print("We cannot ship this package.")
    return(shipment_quote)    

def routing(shipment_quote):                               # not working
    if ((shipment_quote["can_ship"] == "y") and (shipment_quote["dangerous"] == "y")):
        print("This package must be routed by ground or ocean.")
        shipment_quote["air_possible"] = "n"
    if ((shipment_quote["can_ship"] == "y") and (shipment_quote["dangerous"] == "n")):
        print("This package can be routed by ground or ocean or air.")
        shipment_quote["air_possible"] = "y"
    return(shipment_quote)
   
def cost(shipment_quote):                                  # not working   # I've decided to put all the estimates in the quote
    shipment_quote["ship_ocean_cost"] = 30                              # do I try to make these numbers come back as dollars (is that a thing?) or just put a "$" in front of the answer
    shipment_quote["ship_ground_nonurgent_cost"] = 25
    shipment_quote["ship_ground_urgent_cost"] = 45
    if shipment_quote["air_possible"] == "y":                                         # I accidentally collapsed some rows.  How did I do that?
        shipment_quote["ship_air_cost_kg"] = (shipment_quote["weight_kg"] * 10)
        shipment_quote["ship_air_cost_cm"] = (shipment_quote["cubic_meters"] * 20)
    return(shipment_quote)

def estimate(shipment_quote):                              # not working
    print("Estimated cost to ship by various routes: ")
    print("Ground Non-Urgent: $", shipment_quote["ship_ground_nonurgent_cost"])
    print("Ground Urgent: $", shipment_quote["ship_ground_urgent_cost"])
    print("Ocean: $", shipment_quote["ship_ocean_cost"])
    if shipment_quote["air_possible"] == "y":                  # I have not yet tried to get the either or working here 
        print("Air will be the larger of : $", shipment_quote["ship_air_cost_kg"], "or $", shipment_quote["ship_air_cost_cm"])
    return(shipment_quote)

#for my information                          # not working
def fmi(shipment_quote):
    print("Complete dictionary")
    for key, value in shipment_quote.items():
        print("key=%s, value=%s" % (key, value))
    return(shipment_quote)
                                                          
def main():                                      
    while True:

        print("Shipment System")                               # not sure if this actually goes at the top or is a function that is called near the bottom
        print("Enter 1 to get a shipment quote.")              # I don't have this doing anything yet other than taking input
        #print("Enter 2 to update customer information.")
        print("Enter 3 to quit.")
        action = input("What would you like to do? ")

        if action == "1":

            shipment_quote = get_input()
            print("after get_input :", shipment_quote)
            shipment_quote = eval_package(shipment_quote)     # line 88 error but I don't know why
            print("after eval_package: ", shipment_quote)
            shipment_quote = routing(shipment_quote)
            shipment_quote = cost(shipment_quote)             # line 94 error but I don't understand it
            shipment_quote = estimate(shipment_quote)
            shipment_quote = fmi(shipment_quote)
        if action == "3":
            break

if __name__ == "__main__":                        # name is special type of variable -->  called a dunder (double-underscore) // allows me to import from here to other programs 
    main()                                        # getting error here now 
                                                # writing this way means then entire .py file is now a module rather than just a script


print()                                                         
print("still menu and larger value things to clean up")
print()
print


#main()                 # naive, not good Python style

# he wants me to think about a better way to organize the program
# rules for air vs ocean vs ground are not clearly visible in this program - can I make it clearer?
# copy this program and work on it elsewhere, then compare the 2 and see if it is better.