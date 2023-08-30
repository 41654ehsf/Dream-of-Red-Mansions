import time

class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100

class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def explore_garden(player):
    delay_print(f"欢迎来到《红楼梦》大观园，{player.name}！")
    delay_print("你将在这个游戏中探索大观园，与人物互动，感受这个经典文学世界。")

    characters = [
        Character("贾宝玉", "一个情感细腻，善良聪慧的少年。"),
        Character("林黛玉", "一个美丽而忧郁的女子，贾宝玉的表妹。"),
        Character("王熙凤", "一个精明干练，善于安排事务的女性。"),
    ]

    while player.energy > 0:
        print("\n你可以前往以下地点：")
        print("1. 贾宝玉的房间")
        print("2. 林黛玉的房间")
        print("3. 王熙凤的房间")

        choice = input("请选择要前往的地点（输入地点编号）：")
        if choice in ["1", "2", "3"]:
            character = characters[int(choice) - 1]
            delay_print(f"{player.name}前往了{character.name}的房间。")
            delay_print(character.description)
        else:
            delay_print("无效的选择。")

        player.energy -= 20
        continue_choice = input("是否继续探索？(是/否): ").strip().lower()
        if continue_choice != "是":
            delay_print(f"谢谢参与《红楼梦》大观园游戏！再见。")
            exit()

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    explore_garden(player)

if __name__ == "__main__":
    main()
