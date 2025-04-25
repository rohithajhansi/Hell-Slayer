import time

def right():
    """Creates a function that will be called when the player encounters a path"""
    print("You have encountered a New Path.")
    time.sleep(1)
    print("You have 2 options:")
    options = ["1. Take Right","2. Continue"]
    print("\n".join(map(lambda x: x, options)))
    time.sleep(1)
    while True:
        try:
            user_option = int(input("What do you want to do (number)? "))
            filtered_options = list(filter(lambda x: 1 in x, user_option))

            if user_option == 1:
                print("You have successfully turned Right.")
                wrong_path = True
                exit()
                break
            elif user_option == 2:
                print("You have successfully continued.")
                Goal = "pass"
                break
        except (TypeError, ValueError,Exception):
            print("Please only enter a number (|_|).")
            
    
def left():
    """Creates a function that will be called when the player encounters a path"""
    print("You have encountered a New Path.")
    time.sleep(1)
    print("You have 2 options:")
    options = ["1. Take Left","2. Continue"]
    print("\n".join(map(lambda x: x, options)))
    time.sleep(1)
    while True:
        try:
            user_option = int(input("What do you want to do (number)? "))
            if user_option == 1:
                print("You have successfully turned Left.")
                print("Unfortunately, you have eneded up at bottom of the mountain.")
                print("You have failed to climb the mountain.")
                print("You have failed to save your sister.")
                print("Better luck next time!")
                exit()
                break
            elif user_option == 2:
                print("You have successfully continued.")
                Goal = "pass"
                break
        except (TypeError, ValueError,Exception):
            print("Please only enter a number (|_|).")
