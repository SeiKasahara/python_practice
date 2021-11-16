import random
from types import NoneType

allchoice = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
prompt = """
(0) 石头
(1) 剪刀
(2) 布
请选择(0/1/2):"""
cwin = 0
pwin = 0

while cwin < 2 and pwin < 2:
    computer = random.choice(allchoice)
    ind = int(input(prompt))
    player = allchoice[ind]

    print('你的选择: %s , 电脑的选择: %s' % (player, computer))
    if player == computer:
        print('平局')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1m你赢了\033[31;0m')
    else:
        cwin += 1
        print('你输了')
