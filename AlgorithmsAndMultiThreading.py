#i used a library to generate fake data to operate the sorting algorithms on
from faker import Faker
import threading

fake = Faker()

#I created the fake data using list comprehension so that can be called smoothly and it can be generated.
names = [fake.name() for i in range(351)]
"""      
#for each element within the list, if one element is bigger than the first, swap the element positions
def BubbleSort():
    #takes the length of the list
    n = len(names)
    #iterates through each element within the list, then goes through each element with the second for loop so that the
    #actual logic can be carried out., bubble sort compares the elements in a ascending order.
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j + 1]:
                 names[j], names[j + 1] = names[j + 1], names[j]
    return(names)


#print(BubbleSort())
"""
def mergesort():
    #gotten the length and the value of half the list length
    length = len(names)
    half = length//2 # prevents compiler from taking only one element also
    #implementing the merge sort logic
    L_split = []
    R_split = []
    Lfirst_split = names[:half] #this is gonna take the first half of the list
    Rfirst_split = names[half:] #takes the second half of the list in first split
    Lsecond_split = Lfirst_split[:half]
    Rsecond_split = Rfirst_split[half:]


    #testing code
    lengthy = len(Rfirst_split)
    lengthy2 = len(Lfirst_split)  
    lengthy3 = len(Rsecond_split)
    
    second_split = []
    print(Lfirst_split)
    print(lengthy2)
    print(lengthy3)
    #print(Lfirst_split)                
    #print(Rsecond_split)
    
        
mergesort()  #this is to make sure the list is an odd amount, i.e 1,2,3,4,5 and will move accordingly
"""

"""


""""
def selection_sort():
    n = len(names)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if names[j] < names[min_index]:
                    min_index = j

            names[i], names[min_index] = names[min_index], names[i]

    print(names)

    

def insertion_sort():
     n = len(names)
     for i in range(1, n):
        C_element = names[i]
        j = i - 1

        while j >= 0 and names[j] > C_element:
            names[j + 1] = names[j]
            j = j - 1
        
        names[j + 1] = C_element
        print(names)

insertion_sort()
"""                  #create the algorithm here then do else for the other section but recreate first part with !=

     
    



               
               
               
     
         


            #upgrade the min index to another postin, then compare that position value ot the rest of the list

     
            
            






