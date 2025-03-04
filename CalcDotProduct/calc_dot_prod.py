# Assignment - Calculate Dot Product
print()
print("Calculate Dot Product Assignment - Angelique")
print()

def main() :
    list_1 = [2, 7, 4, 6, 2]
    list_2 = [1, 6, 3, 5, 1]
    print("list_1", list_1)
    print("list_2", list_2)
    dot_product = 0
    print("dot_product starts as : ", dot_product)
    n = len(list_1)
    m = len(list_2)
    print("lengths of lists : ",  n, "and",  m)
    samelength = n-m
    print("samelength : ", samelength)    
    print()                      
        
    if samelength < 1 :
        i = 0
        print("index is : ", i)
        for num in list_1 :
            print(list_1[i], " X ", list_2[i], )            
            interim = list_1[i] * list_2[i]
            i = i + 1 
            dot_product = (dot_product + interim)
            print("dot_product : ", dot_product)
            print()
            print("index : ", i)
                       
                      
        return dot_product                                      # looking for 88 here // are there Nazis in the house?
    else :
        print("The lists are of different lengths.")
       

main()


print()
print("fin")
print()