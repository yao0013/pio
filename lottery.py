"""
大乐透和双色球随机选号程序

Version: 0.1
Author: 姚春敏
Date: 2021-08-18
"""

from random import randrange, randint, sample
# import tkinter

def display(balls):
    """
    输出列表中的号码
    """
    if s == 2:

        for index, ball in enumerate(balls):
            if index == len(balls) - 2:
                print('|', end=' ')
            print('%02d' % ball, end=' ')
        print()
    else:
        for index, ball in enumerate(balls):
            if index == len(balls) - 1:
                print('|', end=' ')
            print('%02d' % ball, end=' ')
        print()



def random_select():
    """
    随机选择一组号码
    """
    if s == 2:
        red_balls = [x for x in range(1, 36)]
        selected_balls = []
    # for _ in range(6):
    #     index = randrange(len(red_balls))
    #     selected_balls.append(red_balls[index])
    #     del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
        selected_balls = sample(red_balls, 5)
        selected_balls.sort()
        blue_balls = [y for y in range(1, 13)]
        selected_blusballs = []
        selected_blusballs = sample(blue_balls, 2)
        selected_blusballs.sort()
        selected_balls += selected_blusballs
        # return selected_balls
    else:
        red_balls = [x for x in range(1, 33)]
        selected_balls = []

        selected_balls = sample(red_balls, 6)
        selected_balls.sort()
        blue_balls = [y for y in range(1, 16)]
        selected_blusballs = []
        selected_blusballs = sample(blue_balls, 1)
        selected_blusballs.sort()
        selected_balls += selected_blusballs

    return selected_balls






def main():
    n = int(input('机选几注: '))
    global s
    s = int(input("请选择类型：1、双色球；2、大乐透"))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
