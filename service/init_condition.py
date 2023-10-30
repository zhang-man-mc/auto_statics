

from sql_statement.authentication import Authentication
from sql_statement.commitment import Commitment
from sql_statement.ledger import Ledger
from sql_statement.score import Score
from sql_statement.user_login import UserLogin
from utils.date_utils import DateUtils

def init_scene_and_district(obj,scene_value,district_value):
    """初始化场景 区"""
    obj.set_scene(scene_value)
    obj.set_district(district_value)


def init_begin_time(obj,bt:str):
    """初始化开始时间"""
    obj.set_begin_time(bt)



def init_end_time(obj,et:str):
    """初始化结束时间"""
    obj.set_end_time(et)

def init_month_and_year(obj,month:int,year:int):
    """初始化月份 季度 年"""
    obj.set_month(month)

    # 根据月份生成对应的季度范围
    quarter_begin,quarter_end = DateUtils.get_quarter(month)
    obj.set_quarter_begin(quarter_begin)
    obj.set_quarter_end(quarter_end)

    obj.set_year(year)


def init_obj():
    """对5个统计对象的sql初始化"""
    user_login = UserLogin()
    score = Score()
    ledger = Ledger()
    commitment = Commitment()
    authentication = Authentication()
    return user_login,score,ledger,commitment,authentication

def init(objs,scene:int,district:str,year:int,month:int,begin_time:str,end_time:str):
    """初始化查询语句的条件变量"""
    # 为所有对象初始化场景，区
    for item in objs:
        init_scene_and_district(item,scene,district)
        # 台账初始化月份，年
        if isinstance(item,Ledger):
            init_month_and_year(item,month,year)
        # 自评 开始和结束时间
        if isinstance(item,Score):
            init_begin_time(item,begin_time)
            init_end_time(item,end_time)
        # 用户登录 开始和结束时间
        if isinstance(item,UserLogin):
            init_begin_time(item,begin_time)
            init_end_time(item, end_time)
        #  用户承诺 结束时间
        if isinstance(item,Commitment):
            init_end_time(item,end_time)

if __name__ == '__main__':
    objs = init_obj()
    print(objs)
    print(objs[0])
    print(isinstance(objs[0],UserLogin))
    # init(objs,1,'静安区',2023,10,'2023-10-01 00:00:00','2023-10-31 23:59:59')


