# Assignment - Packages
# Classes are not necessary for smaller assignments/applications - there is a lot of overhead and intellectual demand
# this is between 100 and 200 lines of code // Classes are going out of favour, in favour of Functional Programming
# Dictionary rather Class here

# possible inputs
def get_input():
    shipment_quote = {}
    shipment_quote["customer_name"] = input("Customer name: ")    # we are creating a key in shipment_quote // dictionary has many key value pairs - even inside one package
    shipment_quote["weight"] = input("Package weight in kilograms: ")
    shipment_quote["cubic_meters"] = input("Cubic meters of package: ")
    print(shipment_quote)
    print()

    # no specific delivery date yes or no
    # required delivery date (year-mm-dd hh:mm tz)
    # dangerous goods yes or no
    # urgent yes or no
    # ? heavy - this not about exceeding the weight limitation but being close // not sure about htis
    # internation yes or no
    # contact info
    # recipient address
    # recipient name
    return shipment_quote

def main():                                      
    shipment_quote = get_input()

if __name__ == "__main__":                        # name is special type of variable -->  called a dunder (double-underscore) // allows me to import from here to other programs 
    main()                                        # writing this way means then entire .py file is now a module rather than just a script


#main()                 # naive, not good Python style