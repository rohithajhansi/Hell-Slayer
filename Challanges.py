
import sys
import time
from Setup import character
from Story import name
from Items import inventory,items

class Challanges():
    """Creates a class that will be used to create the challanges that the player will face"""
        
    def bad_person(self):
        """Docstring"""
        print("You have encountered a stalker that keeps following you around.")
        time.sleep(1)
        print("Be Careful!")
        time.sleep(1)
        print("You have 3 options:")
        options = ["1. Run away","2. Fight","3. Try to sneak past him"]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        
        while True:
            try:
                user_option = int(input("What do you want to do? "))
                if user_option == "1":
                    print("You have successfully ran away.")
                    print("But....")
                    time.sleep(1)
                    print("You Failed to climb the mountain.")
                    print('You have failed to climb the mountain.')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                    break
                elif user_option == "2":
                    print("You have successfully fought him.")
                    print("But....")
                    time.sleep(1)
                    print("You have lost 1 Health Point.")
                    Goal = "pass"
                    break
                else:
                    print("You have successfully snuck past him.")
                    print("You Did a great job! Sneaking past him.")
                    Goal = "pass"
                    break
            except (TypeError, ValueError,Exception):
                print("Please enter a number only (|_|).")
    
    def spike(self):
        """Creates a function that will be called when the player encounters a spike trap"""
        print("You have encountered a spike trap.")
        time.sleep(1)
        
        print("You have 2 options:")
        options = ["1. Continue towards the spike trap","2. Try to avoid the spike trap by backtracking"]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        
        while True:
            try:
                user_option = int(input("\nWhat do you want to do (number)? \n"))
                if user_option == 1 and "Shield" in inventory:
                    print("You have blocked the spike trap.")
                    time.sleep(1)
                    print("Luckily you have a shield to block the spike trap.")
                    time.sleep(1)
                    print("You made a great decision!")
                    time.sleep(1)
                    print("You have successfully passed the spike trap.")
                    time.sleep(1)
                    print("Don't let your guard down! Otherwise we'll get you next time!")
                    Goal = "Pass"
                elif user_option == 2:
                    print("You have been impaled to death by the spike trap because you were too slow! (T_T)")
                    time.sleep(1)
                    print("Better luck next time!")
                    print('You have failed to climb the mountain.')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                else:
                    print("You have been impaled to death by the spike trap because you were too slow! (T_T)")
                    time.sleep(1)
                    print("Better luck next time!")
                    print('You have failed to climb the mountain.')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                break
            except (TypeError, ValueError,Exception):
                print("Please only enter a number (|_|).")
    
    def lake(self):
        """Creates a function that will be called when the player encounters a lake"""
        print("You have encountered a lake.")
        time.sleep(1)
        print("You have 2 options:")
        options = ["1. Try to swim across the lake","2. Make a Boat"]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        while True:
            try:
                user_option = int(input("What do you want to do (number)? "))
                if user_option == 1:
                    print("You have successfully Crossed the lake.")
                    Goal = "pass"
                elif user_option == 2:
                    print("You only have 4 more minutes before Zenitsu comes back looking for you.")
                    time.sleep(10)
                    print(f"Zenitsu caught up with you.{name} have no choice but to go back down.")
                    print('You have failed to climb the mountain.')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                break
            except (TypeError, ValueError,Exception):
                print("Please only enter a number (|_|).")
    
    def fire(self):
        """Creates a function that will be called when the player encounters a fire"""
        print("You have encountered a fire.")
        time.sleep(1)
        print("You have 2 options:")
        options = ["1. Try to run away from the fire very quickly","2. Wait for the fire to go out"]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        while True:
            try:
                user_option = int(input("What do you want to do (number)? "))
                if user_option == 1:
                    print("You have successfully ran away from the fire.")
                    Goal = "pass"
                elif user_option == 2:
                    print("You have been burned to death by the fire.")
                    print('You have failed to climb the mountain.')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                break
            except (TypeError, ValueError,Exception):
                print("Please only enter a number (|_|).")
                
    def oxygen_mask(self):
        '''Checks if the player has an oxygen mask in their inventory'''
        print('You realize that the air is getting thinner and thinner.\n')
        time.sleep(2)
        print('So you check your backpack to see if you have an oxygen mask.')
        if 'oxygen mask' in inventory:
            print('Luckily, you have an oxygen mask in your backpack! ^_^\n')
            print('You put it on and continue on your journey.')
            Goal = 'pass'
        else:
            print('You have no oxygen mask in your backpack. (T_T)')
            time.sleep(2)
            print('You start to feel dizzy and lightheaded and eventually suffocate to death T_T.')
            print('You have failed to climb the mountain.')
            print('You have failed to save your sister.')
            print('Better luck next time!')
            exit()
            
    def demon_house(self):
        """Creates a function that will be called when the player encounters a demon house"""
        print("You have encountered a house.")
        time.sleep(1)
        print("You have 2 options:")
        options = ["1. Take a Break","2. Continue"]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        while True:
            try:
                user_option = int(input("What do you want to do (number)? "))
                if user_option == 1:
                    print("There has been an incident.")
                    print("The demon has entered the house.")
                    print("awawqawawa")
                    print('"Do you have any last words before you die?"')
                    print('You have failed to save your sister.')
                    print('Better luck next time!')
                    exit()
                elif user_option == 2:
                    Goal = "pass"
                break
            except (TypeError, ValueError,Exception):
                print("Please only enter a number (|_|).")
                
    def rock(self):
        """Creates a function that will be called when the player encounters a rock"""
        print("You have encountered a rock.\n")
        time.sleep(1)
        print("You have 2 options:")
        options = ["1. Try to climb over the rock","2. Try to dig a tunnel under the rock",]
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        user_input = int(input("\nWhat are you going to do (number)? \n"))
        try:
            
            if user_input == 1 and 'Ladder' in inventory:
                print('You placed the ladder down and slowly began using it as a bridge.')
                print('As you are balancing on the ladder, you accidentally look down and freeze.\n')
                time.sleep(2)
                print('Looking down, you find yourself peering into a never ending chasm of darkness')
                print('Slowly but surely you climbed over the rock.\n')
                print('Congratulation! You made a great decision!\n')
                Goal = 'pass'
                
            elif user_input == 1 and 'Ladder' not in inventory:
                print('You tried to climb over the rock but you have no ladder.')
                print('Leading you to fall into the chasm of darkness.\n')
                time.sleep(2)
                print('As you fall, time starts to slow down and you remember your family.')
                print('You realize you have failed to climb the mountain and have failed your sister.\n')
                print('You close your eyes and accept your fate but suddenly...\n')
                time.sleep(3)
                print('You feel a sharp pain in your back and you open your eyes to find yourself on the ground inside the chasm\n')
                items('sword')
                items('dagger')
                if 'Sword' in inventory and 'Dagger' in inventory:
                    character['hp'] += 5
                    print('You have gained 5 attack points!\n')
                    time.sleep(2)
                print('As you stand up, you realize you are in a dipiltated bunker.\n')
                print('You have no choice but to continue on your journey.')
                time.sleep(2)
                print('As you wander about, you find the edge of a starwell leading up to the surface.\n')
                print('But... the real question is...\n')
                time.sleep(3)
                print('Where will it lead you?\n')
                time.sleep(2)
                print('You climb up the starwell and find yourself back on the mountain.')
                print('But as you look around you realize that you are much higher up the mountain.\n')
                Goal = 'pass'
                self.oxygen_mask()
            elif user_input == 2:
                print('You tried to dig a tunnel under the rock but the rock is too hard to dig under.')
                print('You continue to dig and dig but you eventually...\n')
                time.sleep(2)
                print('fail to climb the mountain and die because the rock collapsed on you. T_T\n')
                print('You have failed to save your sister.')
                print('Better luck next time!')
                exit()
                
        except (TypeError, ValueError,Exception):
                print("Please only enter a number (|_|).")