#!/usr/bin/python
# -*- coding:utf-8 -*-

import RPi.GPIO as GPIO


def main():
    # 设置GPIO编号模式
    GPIO.setmode(GPIO.BOARD)

    # 设置警告模式：关闭
    GPIO.setwarnings(False)

    # 配置通道：设置BOARD编号18针脚为输出模式
    GPIO.setup(18, GPIO.OUT)

    # 设置GPIO针脚的输出状态
    GPIO.output(18, GPIO.LOW)

    # 清理GPIO恢复默认
    #GPIO.cleanup()


if __name__ == '__main__':
    main()
