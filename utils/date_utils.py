from datetime import datetime, timedelta
import re
class DateUtils:
    default_date_format = '%Y-%m-%d'
    default_time_format = '%Y-%m-%d %H:%M:%S'
    re_date_time_format = '^2\d{3}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}$'
    @staticmethod
    def now_time()->str:
        """返回当前时刻的日期时间

        Returns:
            str: 当前日期时间
        """
        return datetime.now().strftime(DateUtils.default_time_format)
    @staticmethod
    def today_date()->str:
        """返回今天的日期  2023-10-20 """
        return datetime.now().strftime(DateUtils.default_date_format)

    @staticmethod
    def get_current_month():
        return datetime.now().month

    @staticmethod
    def get_current_year():
        return datetime.now().year

    @staticmethod
    def get_current_month_first_day():
        return datetime.today().replace(day=1).strftime("%Y-%m-%d 00:00:00")

    @staticmethod
    def get_current_month_last_day():
        """返回本月的最后一天的时间"""
        today = datetime.today()
        if today.month == 12:
            last_day = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            last_day = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
        return last_day.strftime("%Y-%m-%d 23:59:59")

    @staticmethod
    def is_time_same_month(time1:str,time2:str):
        """判断两个时间是否是同一月

        Args:
            time1 (str): 
            time2 (str): 

        Returns:
            _type_: 
        """
        t1 = datetime.strptime(time1,DateUtils.default_time_format)
        t2 = datetime.strptime(time2,DateUtils.default_time_format)
        if t1.year == t2.year and t1.month == t2.month:
            return True
        return False

    @staticmethod
    def is_time_format_valid(time_str:str)->bool:
        """判断时间字符串是否是 2xxx-xx-xx xx:xx:xx格式

        Args:
            time_str (str): _description_

        Returns:
            bool: _description_
        """
        result = re.match(DateUtils.re_date_time_format,time_str)
        if result is None:
            return False
        return True

    @staticmethod
    def is_year_format_valid(year:int)->bool:
        """判断给定的年份是否有效

        Args:
            year (int): 年份

        Returns:
            bool: 
        """
        result = re.match('^2\d{3}$',str(year))
        if result is None:
            return False
        return True

    @staticmethod
    def is_month_format_valid(month:int)->bool:
        """判断给定的月份是否有效

        Args:
            year (int): 月份

        Returns:
            bool: 
        """
        if month < 1 or month > 12:
            return False
        result = re.match('^\d{1,2}$',str(month))
        if result is None:
            return False
        return True

    @staticmethod
    def get_quarter(month):
        """根据输入的月份返回季度"""
        if month < 1 or month > 12:
            return None

        quarter = (month - 1) // 3 + 1
        start_month = 3 * (quarter - 1) + 1
        end_month = 3 * quarter

        return start_month, end_month

    def is_time_in_month(time:str,month:int):
        """判断时间是否在指定月内"""
        t = datetime.strptime(time,DateUtils.default_time_format)
        if t.month != month:
            return False
        return True
    
    def get_month_by_time(time:str)->int:
        t = datetime.strptime(time,DateUtils.default_time_format)
        return t.month

if __name__ == '__main__':
    # print(DateUtils.now_time())
    # print(DateUtils.today_date())
    # print(DateUtils.get_current_month_first_day())
    # print(DateUtils.get_current_month())
    # print(DateUtils.get_current_year())

    # print(DateUtils.is_time_same_month('2023-09-30 00:00:00','2023-10-01 00:00:00'))
    # print(DateUtils.is_time_format_valid('2023-09-30 00:00:00'))
    # print(DateUtils.is_year_format_valid())
    # print(DateUtils.is_month_format_valid(12))

    # print(DateUtils.get_quarter(2))
    print(type(DateUtils.get_month_by_time('2023-09-30 00:00:00')))