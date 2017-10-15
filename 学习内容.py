#coding=utf-8

import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time
import MySQLdb
import urllib
import multiprocessing
import threading
"""
1Python基础（第1周）
课程目标
1.掌握Python基础相关的知识；
2.为后续的学习打下坚实的基础。
作业/案例
2048小游戏。包含知识点：Python语法基础、Python控制流、函数、面向对象。
主要内容
1.Python初识
2.Python语法基础
3.Python控制流与小实例
4.Python函数详解
5.Python模块实战

2Python网络爬虫基础及进阶实训（第2周-第5周）
课程目标
1.掌握Python网络爬虫基础及进阶；
2.掌握基本的网络爬虫项目；
3.编写复杂的爬虫项目；
4.解决复杂的反爬攻克技术；
5.编写大型爬虫项目。
作业/案例1
京东商城商品爬虫项目。包含知识点：网络爬虫基础、抓包分析技术、用户代理/代理IP池技术。
作业/案例2
知乎爬虫项目。包含知识点：Scrapy基础、Scrapy进阶、验证码处理技术、数据去重技术、分布式爬虫技术。
主要内容
1.网络爬虫
2.爬虫原理与数据抓取实战
3.Scrapy框架及其实战
4.淘宝商品大型爬虫项目与自动写入数据库实战
5.BeautifulSoup基础实战
6.PhantomJS基础实战
7.腾讯动漫爬虫项目实战
8.分布式爬虫原理
9.分布式爬虫Docker基础及Redis基础
10.高阶分布式爬虫技术实战


3Python数据挖掘与机器学习基础、进阶及案例实训（第6周-第11周）
课程目标
1.掌握Python数据挖掘与机器学习基础；
2.学会数据预处理；
3.掌握数据挖掘与机器学习的核心知识点；
4.深入理解常见算法的底层原理，并通过Python实现；
5.对常见算法进行实际应用；
6.掌握文本挖掘技术、深入掌握机器学习技术；
7.深入掌握数据挖掘与机器学习实践案例的应用。
作业/案例1
和讯博客数据预处理项目。包含知识点：数据挖掘与机器学习基础、数据预处理技术、词云技术。
作业/案例2
公司客户群体划分与产品个性化推荐项目。包含知识点：模型评价、分类算法、聚类算法、关联分析算法。
作业/案例3
计算机视觉之图像自动识别案例。包含知识点：图像处理技术、图像分类技术、计算机视觉技术。
主要内容
1.Python数据挖掘与机器学习技术概述及应用场景
2.基础模块的安装及使用
3.数据导入、可视化实战
4.数据预处理技术及其实战
5.K-近邻（KNN）算法原理及其项目实战
6.朴素贝叶斯算法原理及其实战
7.Adaboost元算法原理及其实战
8.支持向量机（SVM）原理及其实战
9.逻辑回归原理及其实战
10.Apriori算法原理及其实战
11.线性回归算法原理及其实战
12.FP-Growth算法原理及其实战
13.Sklearn基础、常见算法实现及其实战
14.MILK基础、常见算法实现及其实战
15.文本挖掘综合项目案例实战
16.网页分类综合项目案例实战
17.人脸数据分解综合项目案例实战


4Python WEB开发技术实训（第12周-第13周）
课程目标
1.掌握Python基础相关的知识；
2.为后续的学习打下坚实的基础。
作业/案例
2048小游戏。包含知识点：Python语法基础、Python控制流、函数、面向对象。
主要内容
1.WEB服务器的搭建
2.Python CGI编程基础
3.Django安装与配置、基本指令实战及MVC编程实战
4.MySQL数据库使用基础实战
5.模板及模型的使用实战
6.网站权限控制系统及权限设计常见技巧
7.注册与登陆系统实现
8.数据导入与迁移
9.网站的伪静态化及国际化支持实现
10.多数据库联用与缓存优化实战
11.session与generic实战应用
12.接口开发实战
13.中间件的应用
14.Blog项目与CMS项目实战

5Python自动化运维技术实训（第14周-第15周）
课程目标
1.了解自动化运维技术；
2.通过Python实现对集群服务器进行批量自动化运维。
作业/案例
服务器批量监控案例。包含知识点：Python自动化运维基础、批量运维技术实战。
主要内容
1.Python自动化运维基础与自动监控实战
2.Python自动化运维之系统安全管理与报表管理
3.Python自动化运维之批量运维管理实战
4.Python自动化运维与Ansible实战
5.Python自动化运维与Saltstack实战
6.Python自动化运维之大规模流量监控与管理实战"""