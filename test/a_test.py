

def add(a,b):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return a+b



# import cProfile
# cProfile.run('add(7,9)')

a = (1,2)
# print(add(*a))

# import configparser 
# # 创建ConfigParser对象 
# config = configparser.ConfigParser() 
# # 读取配置文件 
# config.read('config.ini',encoding='utf-8') 
# # 获取配置文件中的值 
# value1 = config.get('real', 'month') 
# value2 = config.get('real', '开始时间') 
# # 打印值 
# print(value1) 
# print(value2) 


import collections
index = collections.defaultdict(list)
print(index)
a = {'one':1,'two':2}
print(a.keys())
a.setdefault('three','hello')
print(a.get('three'))
# print(a['four'])
print(index['four'])
print(index['five'])
print(index.get('six'))
print(index)
print(a)

# for i in a:
#     print(i)