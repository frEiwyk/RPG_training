import random
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'           # red color
    ENDC = '\033[0m'            # end color code (has to be used every time)
    BOLD = '\033[1m'            # makes text bold
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, attack, defense, magic, items):
        self.max_hp = hp                            # we can always call max hp
        self.hp = hp
        self.max_mp = mp                            # we can always call max mp
        self.mp = mp
        self.attack_low = attack - 10
        self.attack_high = attack + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Inventory"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)

    def take_damage(self, damage):
        self.hp -= damage                       # updating hp based on damage taken
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost
        return self.mp

    def choose_action(self):                # showing a list of available actions
        i = 1
        time.sleep(0.5)
        print("\n" + bcolors.BOLD + "Action is on " + self.name + bcolors.ENDC)
        time.sleep(0.5)
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        time.sleep(0.5)
        for thing in self.actions:
            print('    ' + str(i) + ".", thing)
            i += 1

    def choose_magic(self):                 # showing a list of available spells
        i = 1
        time.sleep(0.5)
        print('\n' + bcolors.OKBLUE + bcolors.BOLD + "Available magic" + bcolors.ENDC)
        time.sleep(0.5)
        for spell in self.magic:
            print('    ' + str(i) + ".", spell.name, "(cost:", str(spell.cost) + "mp)")
            i += 1

    def choose_item(self):
        i = 1
        time.sleep(0.5)
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + 'Available items' + bcolors.ENDC)
        time.sleep(0.5)
        for item in self.items:
            print('    ' + str(i) + ".", item["item"].name, "(description:", str(item["item"].description) + "), "
                  + str(item["quantity"]) + 'x')
            i += 1

    def choose_target(self, enemies):
        i = 1
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + 'TARGET:' + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(str(i) + "." + enemy.name)
            i += 1
        choice = int(input("Choose target: ")) - 1
        return choice

    def get_enemy_stats(self):

        hp_bar = ""
        bar_ticks = self.hp / self.max_hp * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                     __________________________________________________")
        print(bcolors.BOLD + self.name + "    " +
              current_hp + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC
              + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = self.hp / self.max_hp * 100 / 4    # because of 25 bars

        while bar_ticks > 0:        # working hp bar
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        mp_bar = ""
        mp_bar_ticks = self.mp / self.max_mp * 100 / 10   # because of 10 bars

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                      _________________________              __________")
        print(bcolors.BOLD + self.name + "     " +
              current_hp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC
              + "|     " + bcolors.BOLD + current_mp + "|" + bcolors.ENDC + bcolors.OKBLUE
              + mp_bar + bcolors.ENDC + "|")

