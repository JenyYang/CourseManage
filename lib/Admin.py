#! /user/bin/python/
# -*-coding:utf-8 -*-
import os
from config import setting
import pickle
import time

class Admin_Class:
    def __init__(self):
        self.user=None
        self.pwd=None

    def register(self,user,pwd):
        if os.path.exists(os.path.join(setting.BASE_ADMIN_DB, user)):
            print("管理员已存在")
        else:
            self.user=user
            self.pwd=pwd
            pickle.dump(self, open(os.path.join(setting.BASE_ADMIN_DB, self.user), "xb"))
    def login(self,user,pwd):
        if os.path.exists(os.path.join(setting.BASE_ADMIN_DB,user)):
            obj=pickle.load(open(os.path.join(setting.BASE_ADMIN_DB,user),"rb"))
            if obj.user==user and obj.pwd==pwd:
                #登录成功
                return 1
            else:
                #用户名或密码错误
                return 0
        else:#管理员不存在
            return -1


class Teacher:
    def __init__(self,name,age,admin_obj):
        self.name=name
        self.age=age
        self.admin=admin_obj
        self.creat_time=time.strftime("%Y-%m-%d %H:%M:%S")
        self.__cost=0

class Course:
    def __init__(self,name,cost,teacher_obj,admin_obj):
        self.name=name
        self.cost=cost
        self.teacher=teacher_obj
        self.admin=admin_obj