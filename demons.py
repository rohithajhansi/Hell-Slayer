from Setup import character,chest,demons
from random import randint
import time

class DemonBattle:
    def __init__(self, character, chest, demons):
        self.character = character
        self.chest = chest
        self.demons = demons

    def fight_options(self):
        options = ["1. Attack Head-On (uses Attack)", "2. Use Magic (uses MP)", "3. Defend (uses Defense)"]
        print("\nChoose your strategy:")
        print("\n".join(map(lambda x: x, options)))
        time.sleep(1)
        while True:
            try:
                choice = int(input("Enter option number: "))
                if choice in [1, 2, 3]:
                    return choice
            except:
                print("Invalid input. Please enter 1, 2, or 3.")

    def battle_demon(self, demon):
            
        print(f"\nFighting {demon['name']} (Health Points: {demon['hp']}, Attack Power: {demon['attack']}, Defense power: {demon['defense']})")
        time.sleep(1)

        if self.character['hp'] < demon['hp']:
            print("You're too weak to continue. You fainted...")
            return False

        strategy = self.fight_options()

        if strategy == 1: 
            power = self.character['attack'] + randint(1, 3)
            print("You charge at the demon with pure strength!")
        elif strategy == 2: 
            if self.character['mp'] < 2:
                print("Not enough MP! Defaulting to head-on attack.")
                power = self.character['attack']
            else:
                power = self.character['mp'] + randint(2, 5)
                self.character['mp'] -= 2
                print("You cast a powerful magic spell!")
        else:  
            power = self.character['defense'] + randint(1, 2)
            print("You brace yourself and defend carefully.")

        demon_power = demon['attack'] + demon['defense'] + demon['hp']
        print("Your Power: {} vs Demon Power: {}".format(power, demon_power))

        if power >= demon_power:
            print("You defeated {}!".format(demon['name']))
            return True
        else:
            self.character['hp'] -= 2
            print("You were hurt and lost 2 HP. Remaining HP: {}".format(self.character['hp']))
            return self.character['hp'] > 0

    def start_battles(self,demon):
        print("\n Let the Demon Battles Begin!")
        result = self.battle_demon(demon)
        if not result:
            print("\nYou could not defeat the demon...")
            print("You fainted and died instead...")
            print("Better luck next time!")
            exit()
        time.sleep(1)
        print("\nYou defeated the demon! You are victorious!")
