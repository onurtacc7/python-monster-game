import sys
import random


class Main:
    max_width = 5
    max_height = 5
    character_alive = True
    character_won = False
    monster_awake = False
    monster_awakened = False
    monster_move_per_turn = 2

    def __init__(self):
        self.display_menu()

    def reset_current_game(self):
        self.character_position = [0, 0]
        self.monster_position = [1, 0]
        self.trap_position = [0, 1]
        self.flask_position = [1, 1]

    def place_character(self):
        self.character_position = [0, 0]

    def place_monster(self):
        self.monster_position = [random.randint(0, self.max_width - 1), random.randint(0, self.max_height - 1)]
        if self.coordinate_collisions('monster', 'player'):
            self.place_monster()
        elif self.coordinate_collisions('monster', 'flask'):
            self.place_monster()
        elif self.coordinate_collisions('monster', 'trap'):
            self.place_monster()

    def place_trap(self):
        self.trap_position = [random.randint(0, self.max_width - 1), random.randint(0, self.max_height - 1)]
        if self.coordinate_collisions('trap', 'player'):
            self.place_trap()
        elif self.coordinate_collisions('trap', 'flask'):
            self.place_trap()
        elif self.coordinate_collisions('trap', 'monster'):
            self.place_trap()

    def place_flask(self):
        self.flask_position = [random.randint(0, self.max_width - 1), random.randint(0, self.max_height - 1)]
        if self.coordinate_collisions('flask', 'player'):
            self.place_flask()
        elif self.coordinate_collisions('flask', 'trap'):
            self.place_flask()
        elif self.coordinate_collisions('flask', 'monster'):
            self.place_flask()

    def display_menu(self):
        menu_list = ['Start New Game', '[Saved Game]', '[Load Game]', 'Customize Setup', 'Exit']
        print('Type the number of your choice')
        print()
        for i in range(1, len(menu_list) + 1):
            print(str(i) + ' ' + menu_list[i - 1])
        choice = input('Your Choice: ')
        self.menu_choice(choice)

    def collision_check(self):
        if self.coordinate_collisions('player', 'monster'):
            self.character_alive = False
            return True
        elif self.coordinate_collisions('player', 'flash'):
            self.character_won = True
            return True
        elif self.coordinate_collisions('player', 'trap'):
            self.monster_awakened = True
            self.trap_position = [-1, -1]
            return True
        return False

    def coordinate_collisions(self, coord1, coord2):
        if coord1 == coord2:
            return None
        if coord1 == 'monster':
            first = self.monster_position
        elif coord1 == 'flask':
            first = self.flask_position
        elif coord1 == 'trap':
            first = self.trap_position
        elif coord1 == 'player':
            first = self.character_position
        else:
            return None

        if coord2 == 'monster':
            second = self.monster_position
        elif coord2 == 'flask':
            second = self.flask_position
        elif coord2 == 'trap':
            second = self.trap_position
        elif coord2 == 'player':
            second = self.character_position
        else:
            return None

        if first[0] == second[0] and first[1] == second[1]:
            return True
        else:
            return False

    def start_new_game(self):
        self.reset_all_settings()
        self.reset_current_game()
        self.setup_game()

    def reset_all_settings(self):
        self.character_alive = True
        self.monster_awake = False
        self.character_won = False
        self.monster_awakened = False

    def setup_game(self):
        self.place_character()
        self.place_monster()
        self.place_trap()
        self.place_flask()
        self.draw_grid()

    def menu_choice(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
        if choice == 1:
            self.start_new_game()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            sys.exit(0)
        else:
            print('That wasn\'nt a valid option. Try again.')
            self.display_menu()

    def draw_grid(self):
        height = self.max_height
        width = self.max_width

        for y in range(0, height):
            for x in range(0, width):
                y = str(y)
                x = str(x)
                char_x = str(self.character_position[0])
                char_y = str(self.character_position[1])
                if str(self.monster_position[0]) == x and str(
                        self.monster_position[1]) == y and self.monster_awake == True:
                    sys.stdout.write('M')
                elif char_x == x and char_y == y:
                    sys.stdout.write('X')
                elif str(self.trap_position[0]) == x and str(self.trap_position[1]) == y:
                    sys.stdout.write('T')
                elif str(self.flask_position[0]) == x and str(self.flask_position[1]) == y:
                    sys.stdout.write('F')
                else:
                    sys.stdout.write('?')

            sys.stdout.write('\r\n')


monster = Main()
