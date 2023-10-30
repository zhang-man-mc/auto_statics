
from utils.date_utils import DateUtils

class FuncParm:
    scene = None
    district= None
    year = None
    month = None,
    begin_time = None,
    end_time = None
    origin_excel_name = None

    def __init__(self,origin_excel_name:str,scene:int,district:str,year:int=DateUtils.get_current_year(),month:int=DateUtils.get_current_month(),begin_time:str=DateUtils.get_current_month_first_day(),end_time:str=DateUtils.get_current_month_last_day()):
        """_summary_

        Args:
            origin_excel_name (str): 原excel文件名
            new_excel_name (str): 新的excel文件名
            scene (int): 场景
            district (str): 区
            year (int): 年
            month (int): 月
            begin_time (str): 开始时间
            end_time (str): 结束时间
        """
        self.scene = scene
        self.district = district
        self.year = year
        self.month = month
        self.begin_time = begin_time
        self.end_time = end_time
        self.origin_excel_name = origin_excel_name



if __name__ == '__main__':
   
    fp1 = FuncParm(1,2,3,4)
    print(fp1.end_time)