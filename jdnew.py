# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2020/02/24
# 京东秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time


def login():
    # 打开京东登录页，并进行扫码登录
    browser.get("https://www.jd.com/")
    time.sleep(3)
    if browser.find_element_by_link_text("你好，请登录"):
        browser.find_element_by_link_text("你好，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.jd.com/cart.action#none")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(times, choose):
    # 点击购物车里全选按钮
    if choose == 2:
        print("请手动勾选需要购买的商品")
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > times:
            if choose == 1:
                while True:
                    try:
                        if browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input"):
                            browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input").click()
                            break
                    except:
                        print("找不到购买按钮")
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("去结算"):
                        browser.find_element_by_link_text("去结算").click()
                        print("结算成功")
                        break
                except:
                    pass
            while True:
                try:
                    if browser.find_element_by_id('order-submit'):
                        browser.find_element_by_id('order-submit').click()
                        now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                        print("抢购成功时间：%s" % now1)
                except:
                    print("再次尝试提交订单")
            time.sleep(0.01)


if __name__ == "__main__":
    #times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    # 时间格式："2018-09-06 11:20:00.000000"
    times = "2020-02-22 11:37:00.000000"
    browser = webdriver.Firefox()
    browser.maximize_window()
    login()
    choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    buy(times, choose)
