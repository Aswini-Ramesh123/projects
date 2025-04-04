list1=[]
while True:
    print("To-Do List:")
    print("1. Add Task")
    print("2. View Task")

    print("3. Remove Task")
    print("4. Exit")
    choice=int(input("Enter Choice:"))
    if choice==1:
         task=input("Enter Task:")
         list1.append(task)
         print("Task Added!")
    elif choice==2:
        if list1==[]:
            print("No Task Found")
        else:
            for index,value in enumerate(list1,1):
                print(f"{index}.{value}")
    elif choice==3:
        print("Your Tasks.......")
        for index,value in enumerate(list1,1):
            print(f"{index}.{value}")
        task_num=int(input("Enter the Task Number U Want To Be Remove:"))
        try:
            if task_num >= 0 or task_num <= len(list1):
                remove_item=list1.pop(task_num-1)
                print(f"Removed Item:{remove_item}")
                print("Item Successfully Removed....")
                print("Remaining Task.....")
                for index,value in enumerate(list1,1):
                    
                    print(f"{index}.{value}")
            else:
                print("Invlid Number")
        except Exception as e:
            print("Please Enter a Valid Number!!!",e)
    elif choice==4:
        print("Exiting......Bye")
        break
    else:
        print("Invalid Choice....Please Enter Valid Choice!")
            
            
         
        
   
    
      

