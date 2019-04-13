#! /usr/bin/python3.5

import cards_tools

# (笪英旭)显示系统菜单
while True:
    cards_tools.show_menu()

    action_str = input("请选择功能： ")

    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.add_card()
        elif action_str == "2":
            cards_tools.show_all()
        else:
            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎使用，再见")
        break
    else:
        print("您输入有误，请重新输入!")
