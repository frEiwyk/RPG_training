from classes.game import Person, bcolors
from classes.magic import Spells
from classes.inventory import Item
import random
import time


# create black magic
fire = Spells("Fire", 10, 150, "black")
thunder = Spells("Thunder", 13, 200, "black")
blizzard = Spells("Blizzard", 17, 300, "black")
meteor = Spells("Meteor", 24, 500, "black")
quake = Spells("Quake", 14, 140, "black")

# create white magic
cure = Spells("Cure", 12, 600, "white")
cura = Spells("Cura", 18, 1000, "white")


# inventory
potion = Item('Potion', 'potion', 'heals 500 HP', 500)
high_potion = Item('High Potion', 'potion', 'heals 1000 HP', 1000)
super_potion = Item('Super Potion', 'potion', 'heals 3000 HP', 3000)
elixer = Item('Elixer', 'elixer', 'fully restores HP/MP of one party member', 9999)
mega_elixer = Item('Mega Elixer', 'elixer', "fully restores party's HP/MP", 9999)

grenade = Item('Grenade', 'attack', 'deals 500 damage to all enemies', 500)


player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [blizzard, meteor, quake, cura]

player_items = [{"item": potion, "quantity": 5}, {"item": high_potion, "quantity": 3},
                {"item": super_potion, "quantity": 2}, {"item": elixer, "quantity": 2},
                {"item": mega_elixer, "quantity": 2}, {"item": grenade, "quantity": 2}]


player1 = Person('Valos  ', 3460, 95, 160, 50, player_spells, player_items)
player2 = Person('Morgan ', 4460, 130, 190, 50, player_spells, player_items)
player3 = Person('Freeman', 3980, 95, 170, 50, player_spells, player_items)

enemy1 = Person('Imp  ', 1250, 130, 400, 200, enemy_spells, [])
enemy2 = Person('Magus', 12000, 405, 505, 25, enemy_spells, [])
enemy3 = Person('Imp  ', 1250, 130, 400, 200, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

battle = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while battle:
    time.sleep(0.5)
    print("===================")
    print("Name:                 HP                                  MP")
    for player in players:
        player.get_stats()

    print("\n")
    time.sleep(0.5)
    for enemy in enemies:
        enemy.get_enemy_stats()

    time.sleep(0.5)
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1                 # because indexing in Python starts from 0

        if index == 0:
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(damage)
            time.sleep(0.5)
            print('\n' + 'You attack ' + enemies[enemy].name.replace(" ", "") + ' for', damage, 'points of damage.')
        elif index == 1:
            player.choose_magic()
            time.sleep(0.5)
            magic_choice = int(input('Choose magic: ')) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou don't have enough magic point.\n" + bcolors.ENDC)
                time.sleep(0.5)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_damage)
                time.sleep(0.5)
                print(bcolors.OKBLUE + '\n' + spell.name + ' heals for ' + str(magic_damage) + ' HP' + bcolors.ENDC)
            elif spell.type == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_damage)
                time.sleep(0.5)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_damage) + " points of damage to "
                      + enemies[enemy].name.replace(" ", "") + "." + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            time.sleep(0.5)
            item_choice = int(input('Choose item: ')) - 1

            if item_choice == -1:
                continue

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "None left." + bcolors.ENDC)
                time.sleep(0.5)
                continue

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if item.type == 'potion':
                player.heal(item.prop)
                time.sleep(0.5)
                print(bcolors.OKGREEN + '\n' + item.name, 'heals' + player.name.replace(" ", "") + 'for', str(item.prop),
                      'HP' + bcolors.ENDC)
            elif item.type == 'elixer':

                if item.name == 'mega_elixer':
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                    time.sleep(0.5)
                print(bcolors.OKGREEN + '\n' + item.name, 'fully restores HP/MP of the party' + bcolors.ENDC)
            elif item.type == 'attack':
                for enemy in enemies:
                    enemy.take_damage(item.prop)
                time.sleep(0.5)
                print(bcolors.FAIL + '\n' + item.name, 'deals', str(item.prop), 'points of damage to all enemies.'
                      + bcolors.ENDC)

        defeated = 0
        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated += 1
        if defeated == len(enemies):
            time.sleep(1)
            print(bcolors.OKBLUE + 'ALL ENEMIES ARE DEAD. YOU WIN!' + bcolors.ENDC)
            battle = False
            break

    defeated2 = 0
    for player in players:
        if player.get_hp() == 0:
            defeated2 += 1
    if defeated2 == len(players):
        time.sleep(1)
        print(bcolors.FAIL + 'The enemy has defeated you!' + bcolors.ENDC)
        battle = False

    # enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            attacked = random.randrange(0, 3)
            enemy_damage = enemy.generate_damage()

            players[attacked].take_damage(enemy_damage)
            print(enemy.name.replace(" ", "") + " attacks " + players[attacked].name.replace(" ", "")
                  + " for " + str(enemy_damage) + ".")

        if enemy_choice == 1:
            random_choice = random.randrange(0, 4)

            spell_choice = enemy.magic[random_choice]
            enemy_damage = spell_choice.generate_damage()

            if spell_choice.type == 'white':
                enemy.heal(enemy_damage)
                time.sleep(0.5)
                print(spell_choice.name + ' heals ' + bcolors.FAIL + enemy.name.replace(" ", "") + bcolors.ENDC +
                      ' for', enemy_damage, ' HP.')
            elif spell_choice.type == 'black':
                attacked = random.randrange(0, 3)
                players[attacked].take_damage(enemy_damage)
                time.sleep(0.5)
                print("\n", bcolors.FAIL, enemy.name.replace(" ", ""), " deals", enemy_damage,
                      "points of damage to", players[attacked].name.replace(" ", ""),
                      " with", spell_choice.name, ".", bcolors.ENDC)

