import yaml

with open("yaml/infoclasses.yaml") as classes:
    info = yaml.safe_load(classes.read())

def pickclass():
    while True:
        print("Выбери класс героя:")
        print("1. Атакер\n2. Защитник")
        print("3. Снайпер\n4. Охотник")
        print("5. Зажигатель\n6. Поглощатель")
        try:
            act = int(input(">>> "))
        except ValueError:
            act = 1
    
        if act == 1:
            class_ = "Attacker"
        elif act == 2:
            class_ = "Defender"
        elif act == 3:
            class_ = "Sniper"
        elif act == 4:
            class_ = "Hunter"
        elif act == 5:
            class_ = "Igniter"
        elif act == 6:
            class_ = "Absorber"
            
        health = info["Classes"][class_]["Health"]
        
        minattack = info["Classes"][class_]["Attack"][0]
        maxattack = info["Classes"][class_]["Attack"][1]
        
        defence = info["Classes"][class_]["Defence"]
        print(f"Ваш класс: {class_}")
        print(f"Здоровье: {health}")
        print(f"Урон (мин/макс): {minattack}/{maxattack}")
        print(f"Защита: {defence}")
        print("\nВы выбираете такой класс? д/н")
        
        act = input(">>> ")
        
        if act == 'д':
            return class_
            break
        else:
            pass

def pickname():
    print("Введите ваше имя:")
    return input(">>> ")