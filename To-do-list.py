print(".................................TO-DO LIST.................................")

while True:
    choice = int(input("\n \n Select the operation of your choice \n 1. VIEW \n 2. ADD \n 3. DELETE \n 4. QUIT \n"))

    list = ["Workout","Take your dog for a walk","Practice Coding","Meditate"]

    if (choice==1):
        for elements in list:
            print (elements)
            
    elif (choice==2):
        new_item = input("Enter a new item to the list: ")
        new_item_pos = int(input("Enter the position to be inserted: "))
        list.insert((new_item_pos-1),new_item)
        
        print("\nUpdated List:\n")

        for elements in list:
            print (elements)
    
       
                        
    elif (choice==3):
        item_rem = int(input("Mention the item number to be deleted: "))
        item_rem = item_rem-1
        list.pop(item_rem)

        print("\nUpdated List:\n")
        for elements in list:
            print (elements)
            
    
    elif (choice==4):
        quit()

    else:
        print("Invalid operation. Please select a valid operation")
        
    
    
    

    



