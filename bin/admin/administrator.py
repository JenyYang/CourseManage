#! /user/bin/python/
# -*-coding:utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib import Admin
from config import setting
import pickle


def register(user, pwd):
    obj = Admin.Admin_Class()
    obj.register(user, pwd)


def login(user, pwd):
    obj = Admin.Admin_Class()
    ret = obj.login(user, pwd)
    if ret == 0:
        print("用户名或密码错误")
    elif ret==-1:
        print("管理员不存在")
    return ret

def creat_teacher(admin_obj):
    teacher_list=[]
    for i in range(5):
        t_obj=Admin.Teacher("黎明" + str(i), 20 + i, admin_obj)
        teacher_list.append(t_obj)
    if os.path.exists(setting.Base_TEACHER_DB):
        exist_list = pickle.load(open(setting.Base_TEACHER_DB, "rb"))
        teacher_list.extend(exist_list)
    pickle.dump(teacher_list,open(setting.Base_TEACHER_DB,"wb"))

def create_course(course_name,course_cost,teacher_obj,admin_obj):
    obj=Admin.Course(course_name,course_cost,teacher_obj,admin_obj)
    c_list=[]
    c_list.append(obj)
    if os.path.exists(setting.BASE_COURSE_DB):
        exist_list=pickle.load(open(setting.BASE_COURSE_DB,"rb"))
        c_list.extend(exist_list)
    pickle.dump(c_list,open(setting.BASE_COURSE_DB, "wb"))
def main():
    inp = input("1、管理员注册   2、管理员登录")
    user = input("用户名：")
    pwd = input("密码")
    if inp == "1":
        # 注册
        register(user, pwd)
    elif inp == "2":
        # 登录
        ret = login(user, pwd)
        if ret == 1:
            admin_obj = pickle.load(open(os.path.join(setting.BASE_ADMIN_DB, user), "rb"))
            # print(admin_obj.user,admin_obj.pwd)

            while True:
                inp = input("1,创建老师；2、创建课程 q:退出")
                if inp=="1":
                    creat_teacher(admin_obj)
                elif inp=="2":
                    if os.path.exists(setting.Base_TEACHER_DB):
                        teacher_list = pickle.load(open(setting.Base_TEACHER_DB, "rb"))
                        for num, item in enumerate(teacher_list, 1):
                            print(num, item.name, item.age, item.admin.user, item.creat_time)
                    else:
                        print("还没有老师，先创建老师")
                    while True:
                        course_name=input("课程名(q退出)：")
                        if course_name == "q":
                            break
                        course_cost=input("课时费：")
                        t_num=input("授课老师(序号)")
                        teacher=teacher_list[int(t_num)-1]
                        create_course(course_name,course_cost,teacher,admin_obj)

                else:
                    break

if __name__ == "__main__":
    main()
