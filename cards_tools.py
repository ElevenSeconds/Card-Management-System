card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1.添加名片")
    print("2.显示所有人的名片信息")
    print("3.查找某人的名片信息")
    print()
    print("输入0退出系统")
    print("*" * 50)


def add_card():
    """添加个人名片信息"""
    print("-" * 50)
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入QQ号：")
    email_str = input("请输入邮箱：")

    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    card_list.append(card_dict)

    print("添加%s的名片信息成功" % name_str)
    print("-" * 50)


def show_all():
    """显示所有人的名片信息"""
    # (me)增加判断列表为空，提示

    print("-" * 50)

    if len(card_list) == 0:
        print("当前列表中没有名片信息")
        return

    # 1. 打印表头
    for table_info in ["姓名", "电话", "QQ", "email"]:
        print(table_info, end="\t\t")
    print()

    # 2. 打印分割线
    print("-" * 50)

    # 3. 打印表内所有字典的信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("-" * 50)


def search_card():
    """按照name这个key寻找个人名片信息"""
    print("-" * 50)

    find_name = input("请输入想寻找的名片姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("找到了%s的名片信息，他的名片信息如下：" % find_name)
            for table_info in ["姓名", "电话", "QQ", "email"]:
                print(table_info, end="\t\t")
            print()
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # （me）完善其他操作如删除和修改
            print("请选择其他操作：【1】修改 【2】删除："
                  "【0】返回上一级菜单")
            deal_card(card_dict)

        break

    else:
        print("查无此人")
    print("-" * 50)


def deal_card(find_dict):
    """
    对指定字典的修改和删除操作
    :param find_dict: 遍历字典列表时，满足要求的字典
    """
    action_str = input("请选择操作：")

    if action_str == "1":

        find_dict["name"] = input_info(find_dict["name"], "请输入姓名：")
        find_dict["phone"] = input_info(find_dict["phone"], "请输入电话号码：")
        find_dict["qq"] = input_info(find_dict["qq"], "请输入QQ：")
        find_dict["email"] = input_info(find_dict["email"], "请输入邮箱：")

        print("%s的名片修改成功" % find_dict["name"])

    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除%s的名片信息成功：" % find_dict["name"])


def input_info(source_value, tip_message):
    """
    当输入为空时，则保留原有的键值对，当输入有变化的时候则更改输入值
    :param source_value: 原来字典保存的值
    :param tip_message: 提醒输入什么的字符串语句
    :return: 如果输入，返回输入内容，否则返回字典原有值
    """
    result = input(tip_message)

    if len(result) > 0:
        return result
    else:
        return source_value
