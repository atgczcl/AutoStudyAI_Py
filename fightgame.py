#!/usr/bin/env python
# coding=utf-8

def start_input_command():
    """
    输入操控命令
    :return: 
    """
    commands = input("input cmd: ").split()
    verb_word = commands[0]
    # 检查这条命令是否存在存，
    if verb_word.lower() in action_dict:
        verb = action_dict[verb_word]
    else:  # 这条命令不存在输出错误， 在未来可以扩展为自主学习功能
        print(("Unknow ver {}".format(verb_word)))
        return

    # 这里是命令+执行的文字，所以要去除执行文字,
    if len(commands) >= 2:
        noun_word = commands[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


def say(noun):
    """
    say 命令执行的函数
    :param noun: 
    :return: 
    """
    return "You said {}".format(noun)


class GameObject:
    class_name = ""
    _desc = ""
    objects = {}

    # 初始化，名字和赋值
    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    # 显示实例的 说明和介绍
    def get_desc(self):
        return self.class_name + "\n" + self._desc


class Goblin(GameObject):
    """
    哥布林怪物类型
    """
    def __init__(self, name):
        self.class_name = name
        self.health = 3
        self._desc = "A foul creature!"  # 哥布林是一个狡猾的不成熟的生物
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee"
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "|" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


# 这里是伤害函数， 实际是这里是行为模块, 思想结果决定着行为结果，
def hit(cmd):
    if cmd in GameObject.objects:
        thing = GameObject.objects[cmd]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "you hit the {}".format(thing.class_name)
        else:
            msg = "There is no {} here!".format(cmd)
        return msg


# 查找事件中心，是否存在事件，检查命令是否存在
def examine(cmd):
    if cmd in GameObject.objects:
        return GameObject.objects[cmd].get_desc()
    else:
        return "There is no {} hear.".format(cmd)


# 事件处理中心，就是找匹配， 
action_dict = {
    "say": say,
    "good": say,
    "hit": hit,
    "show": examine,
}

# 这里是形成
goblin = Goblin("goblin")  # 初始化一个哥布林实例

# 开始游戏
while True:
    start_input_command()
















