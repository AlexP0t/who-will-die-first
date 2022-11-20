import random
print("*****************************")
print("*  Добро пожаловать в игру  *")
print("*     КТО ПЕРВЫЙ СДОХНЕТ    *")
print("*                           *")
print("*    Сражайся с монстрами   *")
print("*         или беги!         *")
print("*                           *")
print("* автор: Alex Poterianski   *")
print("*****************************")
print()
situations = ["empty", "monster", "empty", "empty", "food", "weapon", "armor"]
surnames = ["грозный", "мудрый", "мистический", "тупоголовый", "любопытный", "устрашающий", "магический","космический",
            "кибернетический"]

armors = [{"name": "Viking Helmet", "block": 20},
          {"name": "Space suit", "block": 90},
          {"name": "Bone armor", "block": 13},
          {"name": "Suit of bags", "block": 10},
          {"name": "Diamond armor", "block": 100},
          {"name": "Diamond armor", "block": 100},
          {"name": "Suit of bags", "block": 10},
          {"name": "Suit of bags", "block": 10},
          {"name": "Suit of bags", "block": 10},
          {"name": "Bone armor", "block": 50},
          {"name": "Viking Helmet", "block": 20},
          {"name": "Viking Helmet", "block": 20},
          {"name": "Viking Helmet", "block": 20},
          {"name": "Steel armor", "block": 150},
         ]
weapons = [
    {"name": "Katana", "atack": 16},
    {"name": "Sword", "atack": 18},
    {"name": "Knife", "atack": 10},
    {"name": "Axe", "atack": 20},
    {"name": "Spear", "atack": 10},
    {"name": "kerambit", "atack": 15},
    {"name": "Frying pan", "atack": 25},
    {"name": "Aquaman Trident", "atack": 30},
    {"name": "Lord sword", "atack": 40},
    {"name": "Tor Hammer", "atack": 60},
]

monster_names = [
    {"name": "Gagrgantus", "lifes": 1300},
    {"name": "Lampapus", "lifes": 1600},
    {"name": "King crimson", "lifes": 1100},
    {"name": "Dio Brande", "lifes": 2200},
    {"name": "Astrashi", "lifes": 1000},
    {"name": "Vushas", "lifes": 1500},
    {"name": "Crantatus", "lifes": 1000},
    {"name": "Patak", "lifes": 1540},
    {"name": "Cratos", "lifes": 5000},
]

foods = [
    {"name": "fastfood", "lifes": 5},
    {"name": "Home potato", "lifes": 10},
    {"name": "apple", "lifes": 3},
    {"name": "meat", "lifes": 32},
    {"name": "pizza", "lifes": 12},
    {"name": "soup", "lifes": 6},
    {"name": "mushrooms", "lifes": 11}
]


# создадим монстров
def create_monsters():
    monsters = []
    for mn in monster_names:
        monster = {}
        monster["name"] = mn["name"]
        monster["lifes"] = mn["lifes"]
        monster["atack"] = random.randint(50, 200)
        monster["speed"] = random.randint(5, 19)
        monster["defence"] = random.randint(5, 15)
        monsters.append(monster)
    return monsters


# создадим игрока
name = input("Введите имя персонажа:")
name = name + " " + random.choice(surnames)
player = {
    "name": name,
    "lifes": 100
}
player["atack"] = random.randint(10, 15)
player["defence"] = random.randint(5, 20)
player["speed"] = random.randint(5, 20)
player["weapon"] = random.choice(weapons)
player["armor"] = random.choice(armors)
print(player)

monsters = create_monsters()

commandText = ""
while player["lifes"] > 0 and commandText != "exit":
    commandText = input("Введите команду:")
    situation = ""
    if commandText == "i":
        print(player)
    elif commandText == "w":
        print("Идём вперёд")
        situation = random.choice(situations)
    elif commandText == "a":
        print("Идём влево")
        situation = random.choice(situations)
    elif commandText == "d":
        print("Идём вправо")
        situation = random.choice(situations)
    elif commandText == "s":
        print("Идём назад")
        situation = random.choice(situations)

    if situation == "empty":
        print(player["name"], "никого не встретил")
    elif situation == "food":
        food = random.choice(foods)
        player["lifes"] += food["lifes"]
        print(player["name"], "нашел еду: ", food["name"], "и восполнил жизни на ", food["lifes"])
    elif situation == "weapon":
        weapon = random.choice(weapons)
        print("У вас оружие", player["weapon"])
        print("Вы нашли оружие", weapon)
        answer = input("Заменить yes(y) или no(n)? ")
        if answer == "yes" or answer == "y":
            player["weapon"] = weapon
            print("Оружие успешно смененно")
    elif situation == "armor":
        armor = random.choice(armors)
        print("У вас броня", player["armor"])
        print("Вы нашли", armor)
        answer = input("Заменить yes(y) или no(n)? ")
        if answer == "yes" or answer == "y":
            player["armor"] = armor
            print("Вы успешно сменили броню")
    elif situation == "monster":
        monster = random.choice(monsters)
        player_lifes = player["lifes"]
        player_atack = player["atack"]
        player_defence = player["defence"]
        player_weapon = player["weapon"]["atack"]
        player_speed = player["speed"]
        player_armor = player["armor"]["block"]

        monster_name = monster["name"]
        monster_lifes = monster["lifes"]
        monster_atack = monster["atack"]
        monster_defence = monster["defence"]
        monster_speed = monster["speed"]
        print("Игрок", player)
        print("Встретил монстра: ", monster)
        answer = input("Сражаться или убежать - f или r?")
        if answer == 'r':
            if player_speed > monster_speed:
                print("Вы успешно убежали")
                continue
            else:
                print("Монстр оказался быстрее вас")

        print("Бой начинается!")

        while player_lifes > 0 and monster_lifes > 0:
            player_damage = random.randint(1, player_atack) * player_weapon - monster_defence
            if player_damage < 0:
                player_damage = 0
            monster_lifes = monster_lifes - player_damage
            print("Игрок наносит урон:", player_damage, "Защита монстра:", monster_defence, "Жизнь", monster_lifes)

            if monster_lifes < 0:
                break

            monster_damage = random.randint(1, monster_atack) - player_defence - player_armor

            if monster_damage < 0:
                monster_damage = 0
            player_lifes -= monster_damage
            print("Монстр наносит урон:", monster_damage, "Защита игрока:", player_defence,
                  "Броня игрока:", player_armor, "Жизнь", player_lifes)
            player_armor -= 1
            monster_defence -= 1
            player_defence -= 1
            if monster_defence < 0:
                monster_defence = 0
            if player_defence < 0:
                player_defence = 0
            if player_armor < 0:
                player_armor = 0

        player["lifes"] = player_lifes
        if player_lifes > 0:
            print("Победа!!!")
        else:
            print("Игрок проиграл")
            break


print("*****************************")
print("*       Игра завершена      *")
print("*                           *")
print("*        ВЫ СДОХЛИ          *")
print("*                           *")
print("*****************************")

