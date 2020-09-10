import yaml
import colors

from random import randint
from settings import pickname, pickclass

classes = ["Attacker", "Defender", "Sniper", "Hunter", "Igniter", "Absorber"]

names = ["YikesLoL2002", "TankistDunka210", "Wulf33", "Kluchevaya", "HuKoLaU228", "ProGamer211", "Honka", "Honka1", "Milenium-Cr", "uYwahN"]

with open("yaml/infoclasses.yaml") as class_:
    info = yaml.safe_load(class_.read())

class Player:
    def __init__(self, name, class_):
        self.class_ = class_
        self.name = name
        
        # здоровье
        self.hp = info["Classes"][self.class_]["Health"]
        self.maxhp = self.hp
        
        # минимальный и максимальный урон
        self.minattack = info["Classes"][self.class_]["Attack"][0]
        self.maxattack = info["Classes"][self.class_]["Attack"][1]
        
        # хил
        self.minheal = info["Heal"][0]
        self.maxheal = info["Heal"][1]
        
        # защита
        self.defence = info["Classes"][self.class_]["Defence"]
        
        self.abilitypoints = 0
        
        # победы/поражения
        self.wins = 0
        self.loses = 0
        
        self.money = info["StartMoney"]
        
        # +деньги при победе
        self.MINmoneywin = info["MoneyWin"][0]
        self.MAXmoneywin = info["MoneyWin"][1]
        
        # -деньги при поражении
        self.MINmoneylose = info["MoneyLose"][0]
        self.MAXmoneylose = info["MoneyLose"][1]
        
    def check(self):
        print(f"Класс: {self.class_}")
        print(f"Здоровье: {self.hp}/{self.maxhp}")
        print(f"Деньги: {self.money}")
        print(f"Победы/поражения: {self.wins}/{self.loses}")
        
    def createbot(self):
        global bot
        randomname = randint(0, len(names)-1)
        randomclass = randint(0, len(classes)-1)
        botname = names[randomname]
        botclass = classes[randomclass]
        bot = Bot(botname, botclass)
        return bot

    def fight(self, enemy):
        # застав0чка
        print(f"{colors.gray('Игрок')} {self.name} ({self.class_}) {colors.red('vs')} {colors.gray('Бот')} {bot.name} ({bot.class_})")
        
        while True:
            
            if user.checkhealth():
                user.loses += 1
                lose = True
                break
            
            self.abilitypoints += 1
            bot.abilitypoints += 1
            
            print("Выберите действие:")
            print("1. Атака")
            print("2. Хил (3)")
            print("3. Защита (5)")
            try:
                act = int(input(">>> "))
            except ValueError:
                print(colors.red("Неразборчиво!"))
                act = 1
                
            if act == 1:
                self.attack()
            
            elif act == 2:
                self.heal()
            
            elif act == 3:
                print("ок")
            
            else:
                self.attack()
            
            if bot.checkhealth():
                user.wins += 1
                win = True
                break
            
            print(f"Ход {colors.gray('бота!')}")
            
            bot.actions()
        
        if win:
            
            print("Вы победили!")
            earnedmoney = randint(self.MINmoneywin, self.MAXmoneywin)
            
            self.money += earnedmoney
            print(f"Ваш баланс: {self.money} ({colors.green(f'+{earnedmoney}')})")
        
        elif lose:
            
            print("Вы проиграли!")
            decreasedmoney = randint(self.MINmoneylose, self.MAXmoneylose)
            
            self.money += decreasedmoney
            print(f"Ваш баланс: {self.money} ({colors.red(f'-{decreasedmoney}')})")
    
    def attack(self):
        print("Вы атакуете!")
        damage = randint(self.minattack, self.maxattack)
        bot.hp -= damage - bot.defence
        print(f"Вы нанесли {damage-bot.defence} ед. урона! Здоровье врага - {bot.hp}/{bot.maxhp}.")
    
    def heal(self):
        if self.abilitypoints >= 3:
            healed = randint(self.minheal, self.maxheal)
            print("Вы лечитесь.")
            self.hp += healed
            if self.hp > self.maxhp:
                self.hp = self.maxhp
                print(f"Ваше здоровье: {colors.green(f'{self.hp}')}/{self.maxhp} (+{healed})")
            else:
                print(f"Ваше здоровье: {self.hp}/{self.maxhp}")
        
        else:
            print("У вас мало очков способности!")
            self.attack()
            
    def checkhealth(self):
        if self.hp <= 0:
            return True
            
        
class Bot(Player):
    def actions(self):
        if self.abilitypoints < 3:
            self.attack()
            
        elif self.abilitypoints >= 3:
            if self.hp < self.maxhp * 0.7:
                self.abilitypoints -= 3
                self.heal()
                
            elif self.abilitypoints >= 5:
                if user.hp < self.hp * 0.8:
                    self.abilitypoints -= 5
                    print("БОТ ВЫБРАЛ КАКАШКА")
            
            else:
                self.attack()
        
        else:
            self.attack()
    
    def attack(self):
        damage = randint(self.minattack, self.maxattack)
        print("Противник атакует!")
        user.hp -= damage - user.defence
        print(f"Ваше здоровье: {user.hp}/{user.maxhp} (-{damage-user.defence})")
    
    def heal(self):
        healed = randint(self.minheal, self.maxheal)
        print("Противник лечится!")
        bot.hp += healed
        if bot.hp > bot.maxhp:
            bot.hp = bot.maxhp
            print(f"Здоровье врага: {colors.red(f'{bot.hp}')}/{bot.maxhp} (+{healed})")
        else:
            print(f"Здоровье врага: {bot.hp}/{bot.maxhp} (+{healed})")
            
user = Player(pickname(),pickclass())
while True:
    print("1. Битва")
    print("2. Профиль")
    try:
        act = int(input(">>> "))
    except ValueError:
        pass
    
    if act == 1:
        user.fight(user.createbot())
    elif act == 2:
        user.check()