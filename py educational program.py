#1.Number
# a = 1.0
# b = 3
# print(a + b)
 # int(integer)
 # float
 # complex

#2.String
# string1 = "我是第一个字符串"
# string2 = "我是第二个字符串"
# print(string1 + string2)
# print(string1[0:4])

#3.Function
# #define
# def get_sum(sum1,sum2):
# 	result = sum1 + sum2
# 	return result
# a = 1
# b = 3
# c = get_sum(a,b)
# print(c)

# 4.Class
# class Person:
# 	def __init__(self,name,height,weight,gender):
# 		self.name = name
# 		self.height = height
# 		self.weight = weight
# 		self.gender = gender

# 	def say_name(self):
# 		print("我的名字叫"+self.name)

# 	def say_hello(self,target_name):
# 		print("我叫"+self.name+"很高兴见到你"+target_name)

# person1 = Person("老王",170,100,"男")
# person2 = Person("老张",160,60,"女")

# person1.say_name()
# person2.say_name()

# person1.say_hello("老邓")

# print(person1.weight)

# 5.字符串使用方法
# string1 = "hello World!"
#len length
# print(len(string1))

#capitalize
# print(string1.capitalize())

#upper
# print(string1.upper())

#lower
# print(string1.lower())

#replace
# print(string1.replace("World","world"))

#find
# print(string1.find("llo"))

#*Boolean
# a = True
# b = False

#isupper
# print(string1.isupper())

#函数默认值
# def get_sum(sum1,sum2 = 4):
#     return sum1 + sum2

# print(get_sum(1))

#split
# print(string1.split('o',1))

#endswith
# print(string1.endswith("world"))

#6.List
# list1 = [1,3,2,4,5]
# list1[1] = 9
# list1.append(6)
# list1.pop()
# print(len(list1))
# list1.insert(0,0)
# list1.sort()
# list1.reverse()
# list1.remove(1)
# print(list1.index(2))
# print(list1)

#7.Tuple
# tuple1 = (1,2,3)

# print(len(tuple1))
# print(tuple1[0])

# print(list(tuple1))

#8.Dict
# dict1 = {"name":"老姚","height":180,"weight":140}
# dict1["name"] = "老李"
# print(dict1["name"])
# print(dict1.keys())
# dict1["gender"] = "男"
# print(dict1.values())
# dict1.pop("name")
# print(dict1)

#9.Set
# set1 = {1,2,3,5,2}
# set1 = set((2,3,1,5,7))
# set1 = {1,2,3,4,5,6,7,8,9}
# set1.add(5)
# set1.discard(3)
# set2 ={3,4,5}
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.issubset(set1))

#10.值类型变量与引用型变量
# a = 1
# b = a
# b = 3

# print("a:" + str(a))
# print("b:" + str(b))

# list1 = [1,2,3]
# list2 = list1 *传的是地址
# list2[1] = 4

# print("list1" + str(list1))
# print("list2" + str(list2))

#值类型：数字 布尔

#引用类型：列表 元组 字典 集合 字符串

# homework_finished = True
# if(homework_finished):
#     print("你可以去打游戏")
# else:
#     print("滚去写作业")
      
# > < >= <= == !=   

# prize = 1000
# expensive = (prize > 800)
# print(expensive)

# prize = 100

# if(prize > 800):
#     print("你这也太贵啦")
# elif(prize > 600):
#     print("还是有点贵")
# elif(prize>  400):
#     print("能不能再少点")
# elif(prize > 200):
#     print("可以接受")
# else:
#     print("买了")

# a = 10

# while (a >= 5):
#     print(a)
#     a = a-1

# print("循环结束")

# string1 = "sjdkjalksdjljasdl"

# for char in string1:
#     print(char)

# list1 = ["老邓","老张","老王"]

# for person in list1:
#     print(person)

#*print(list(range(0,10,2)))

# for i in range(0,len(list1),1):
    # print(list1[i])

# for i in range(10):
#     print(i)
#     if(i == 5):
#         break

# print("循环结束")

# patients = [False,True,False,True]

# for patient in patients:
#     if(patient):
#         continue
#     print("治疗")