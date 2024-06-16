"""
 __      __                .__                                                  _____  _______    ____  __.
/  \    /  \_____  _______ |  |__  _____     _____    _____    ____ _______    /  |  | \   _  \  |    |/ _|
\   \/\/   /\__  \ \_  __ \|  |  \ \__  \   /     \  /     \ _/ __ \\_  __ \  /   |  |_/  /_\  \ |      <  
 \        /  / __ \_|  | \/|   Y  \ / __ \_|  Y Y  \|  Y Y  \\  ___/ |  | \/ /    ^   /\  \_/   \|    |  \ 
  \__/\  /  (____  /|__|   |___|  /(____  /|__|_|  /|__|_|  / \___  >|__|    \____   |  \_____  /|____|__ \
       \/        \/             \/      \/       \/       \/      \/              |__|        \/         \/ v 1.0
"""

# Import nessesary modules
import random

# Define global variables
current_enemy = None
hero = None
current_enemy_index = 0
lives = 3

# Define character and enemy classes
class MainCharacter:
    def __init__(self, name, strength, dexterity, intelligence):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.experience = 0
        self.level = 1

    def battle(self, enemy, hero_roll):
        enemy_roll = random.randint(1, 10) * enemy.difficulty
        
        if hero_roll >= enemy_roll:
            self.experience += enemy.experience
            return True, f"You defeated the {enemy.name}!"
        else:
            global lives
            lives -= 1
            return False, f"You were defeated by the {enemy.name}."

class Enemy:
    def __init__(self, name, experience, difficulty):
        self.name = name
        self.experience = experience
        self.difficulty = difficulty

    def start_message(self):
        return f"You encounter a {self.name}! Prepare for battle."

class ChaosCultist(Enemy):
    def __init__(self):
        super().__init__(name="Chaos Cultist", experience=20, difficulty=1.2)

class OrkBoy(Enemy):
    def __init__(self):
        super().__init__(name="Ork Boy", experience=30, difficulty=1.5)

# Create instances of enemies
chaos_cultist = ChaosCultist()
ork_boy = OrkBoy()

# List of enemies
enemies = [chaos_cultist, ork_boy]

# Function to start the game
def start_game():
    global current_enemy_index, lives
    current_enemy_index = 0
    lives = 3
    choose_class()

# Function to choose character class
def choose_class():
    global hero
    print("Choose your character class:")
    print("1. Space Marine")
    print("2. Inquisitor")
    print("3. Tech-Priest")

    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        hero = MainCharacter("Space Marine", 15, 12, 10)
    elif choice == "2":
        hero = MainCharacter("Inquisitor", 12, 10, 15)
    elif choice == "3":
        hero = MainCharacter("Tech-Priest", 10, 15, 12)
    else:
        print("Invalid choice. Please choose again.")
        choose_class()

    start_encounter()

# Function to start encounter with enemies
def start_encounter():
    global current_enemy, current_enemy_index
    current_enemy = enemies[current_enemy_index]

    print(current_enemy.start_message())

    while True:
        user_input = input("Enter your dice roll (1-10)").strip().lower()

        if user_input == "for mankind!":
            global hero
            hero = MainCharacter("Emperor", 100, 100, 100)
            result, message = hero.battle(current_enemy, 100)
            print(message)
        elif user_input == "reverse":
            result, message = current_enemy.battle(hero, 0)
            print(message)
        else:
            try:
                hero_roll = int(user_input)
                if hero_roll < 1 or hero_roll > 10:
                    raise ValueError("Roll must be between 1 and 10.")
                
                enemy_roll = random.randint(1, 10) * current_enemy.difficulty
                result, message = hero.battle(current_enemy, hero_roll)
                print(f"Hero roll: {hero_roll}\n{message}\nEnemy roll: {enemy_roll}")
                
                if result:
                    print(f"You defeated the {current_enemy.name}!")
                else:
                    print(f"You were defeated by the {current_enemy.name}.")

                if current_enemy_index < len(enemies) - 1:
                    current_enemy_index += 1
                    current_enemy = enemies[current_enemy_index]
                    print(current_enemy.start_message())
                else:
                    print("You have defeated all enemies!")
                    break
            
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid input.")
                continue

            if lives <= 0:
                print("Game Over - You ran out of lives!")
                break

# Start the game
start_game()
