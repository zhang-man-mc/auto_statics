import sys
import os
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录的路径（假设项目根目录在当前文件的上一级目录）
project_dir = os.path.dirname(current_dir)
# 将项目根目录的路径添加到系统环境变量中
sys.path.insert(0, project_dir)

import configparser
from utils.date_utils import DateUtils
from exception.config_params_exception import ParamsException

class Config:
    # 要生成的excel编号
    _select_num = None
    # 单区域还是所有区域
    _is_single_analysis_field = None
    # 是否需要过程表
    _is_need_process_sheet = None
    # 年
    _year = None
    # 月
    _month = None
    # 开始时间
    _begin_time = None
    # 结束时间
    _end_time = None
    # 读取的配置是否有效(默认是无效)
    _is_config_value_valid = False


    def __init__(self):
        # 读取配置文件 
        self._read_config_value()
        # 判断时间参数格式是否有效
        try:
            self._judge_time_is_valid()
            # 置配置值为有效标志
            self._is_config_value_valid = True
        except ParamsException as pe:
            # 输出错误原因
            pe.output_error_by_num()
            # 置配置值为无效标志
            self._is_config_value_valid = False
            input("按回车键结束")

    def _judge_time_is_valid(self):
        """判断起始时间是否有效"""
        # 判断开始和结束时间格式是否正确
        if not DateUtils.is_time_format_valid(self._begin_time):
            raise ParamsException(0)
        if not DateUtils.is_time_format_valid(self._end_time):
            raise ParamsException(1)
        # 开始时间大于结束时间时 
        if self._begin_time >= self._end_time:
            raise  ParamsException(2)
        # 判断开始和结束时间是否跨月
        if not DateUtils.is_time_same_month(self._begin_time,self._end_time) :
            raise ParamsException(3)
        # 判断年份是否有效
        if not DateUtils.is_year_format_valid(self._year) :
            raise ParamsException(4)
        # 判断月份是否有效 
        if not DateUtils.is_month_format_valid(self._month):
            raise ParamsException(5)
        # 判断开始时间是否在月份内
        if not DateUtils.is_time_in_month(self._begin_time,self._month):
            raise ParamsException(6)
        return True
    
    def _read_config_value(self):
        """读取配置文件参数"""
        config = configparser.ConfigParser()  
        # 读取配置文件
        config.read('config.ini',encoding='utf-8')
        # 获取配置文件字段值
        self._select_num = int(config.get('condition', 'select_num'))
        self._is_need_process_sheet = int(config.get('condition', 'is_need_process_sheet'))
        self._is_single_analysis_field = int(config.get('condition', 'is_single_analysis_field'))
        self._year = int(config.get('condition', 'year'))
        self._month = int(config.get('condition', 'month'))
        self._begin_time = config.get('condition', 'begin_time')
        self._end_time = config.get('condition', 'end_time')

    def get_select_num(self):
        return self._select_num

    def get_is_single_analysis_field(self):
        return self._is_single_analysis_field

    def get_is_need_process_sheet(self):
        return self._is_need_process_sheet

    def get_year(self):
        return self._year

    def get_month(self):
        return self._month

    def get_begin_time(self):
        return self._begin_time

    def get_end_time(self):
        return self._end_time

    def get_is_config_value_valid(self):
        return self._is_config_value_valid


if __name__ == '__main__':
    c = Config()
    
    print(c.get_select_num())
    print(c.get_is_need_process_sheet())
    print(c.get_year())
    print(c.get_is_config_value_valid())