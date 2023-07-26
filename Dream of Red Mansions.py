import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def __str__(self):
        return self.name

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)
        self.level = 1
        self.exp = 0
        self.inventory = {}

    def add_item(self, item, quantity=1):
        if item.name in self.inventory:
            self.inventory[item.name] += quantity
        else:
            self.inventory[item.name] = quantity

    def remove_item(self, item, quantity=1):
        if item.name in self.inventory:
            if self.inventory[item.name] >= quantity:
                self.inventory[item.name] -= quantity
                return True
            else:
                return False
        else:
            return False

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Event:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

def show_inventory(player):
    print("\n你的背包：")
    for item_name, quantity in player.inventory.items():
        print(f"{item_name}: {quantity}个")

def choose_action():
    print("\n你可以做以下操作：")
    print("1. 查看角色状态")
    print("2. 查看背包")
    print("3. 探索故事情节")
    print("4. 退出游戏")
    while True:
        try:
            choice = int(input("请输入你的选择（1/2/3/4）："))
            if 1 <= choice <= 4:
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def show_character_status(player):
    print(f"\n{name}等级：{player.level}")
    print(f"生命值：{player.health}")
    print(f"攻击力：{player.attack}")
    print(f"经验值：{player.exp}/{player.level * 100}")

def explore_event(player, event):
    delay_print(f"\n{event.description}")
    for idx, choice in enumerate(event.choices, start=1):
        print(f"{idx}. {choice}")
    while True:
        try:
            choice = int(input("请输入你的选择（输入序号）："))
            if 1 <= choice <= len(event.choices):
                return choice
            else:
                print("无效的选择，请重新输入。")
        except ValueError:
            print("无效的输入，请重新输入。")

def level_up(player):
    player.exp -= player.level * 100
    player.level += 1
    player.health = 100
    player.attack += 5
    delay_print(f"恭喜你升级了！你的等级提升到了{player.level}级。生命值和攻击力得到了增加。")

def play_game():
    player_name = input("请输入你的角色名字：")
    player = Player(player_name)
    
    events = [
        Event("你来到了贾府，是否要进去拜访贾宝玉？", ["是，进去拜访", "不，先去其他地方"]),
        Event("你在草坪上看到了一本失落已久的书，是否要拾起查看？", ["是，拾起查看", "不，继续前进"]),
        Event("你在街上遇到了一个受伤的流浪汉，是否要帮助他？", ["是，帮助他", "不，继续前进"]),
        Event("你闯进了一家神秘的酒楼，是否要尝试一下他们的美食？", ["是，尝试美食", "不，继续前进"]),
        Event("你来到了一片茶园，是否要品尝一下当地的名茶？", ["是，品尝名茶", "不，继续前进"])
    ]

    delay_print(f"欢迎来到《红楼梦》游戏，{player_name}！")
    delay_print("你将在这个世界中体验不同的故事情节。")

    while True:
        show_character_status(player)
        action = choose_action()

        if action == 1:
            show_character_status(player)
        elif action == 2:
            show_inventory(player)
        elif action == 3:
            event = random.choice(events)
            choice = explore_event(player, event)
            if choice == 1:
                delay_print("你做出了明智的选择，故事继续发展。")
            elif choice == 2:
                delay_print("你选择了继续前进。")
        elif action == 4:
            delay_print("谢谢你玩《红楼梦》游戏，再见！")
            exit()

if __name__ == "__main__":
    play_game()
