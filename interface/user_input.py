
import sys
import os
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录的路径（假设项目根目录在当前文件的上一级目录）
project_dir = os.path.dirname(current_dir)
# 将项目根目录的路径添加到系统环境变量中
sys.path.insert(0, project_dir)


import re
from utils.format_utils import FormatUtils
from utils.date_utils import DateUtils


class Input:
    def prompt_text():
        """输入选项"""
        print('请选择需要生成的excel:')
        print(FormatUtils.back_indent(4)+'1. 金山餐饮-环境守法自助小程序使用情况-（餐饮单位）')
        print(FormatUtils.back_indent(4)+'2. 金山工地-环境守法自助小程序使用情况-（工地单位）')
        print(FormatUtils.back_indent(4)+'3. 金山碳谷绿湾工业企业-环境守法自助小程序使用情况-（工业企业）')
        print(FormatUtils.back_indent(4)+'4. 静安餐饮-环境守法自助小程序使用情况-（餐饮单位）')
        print(FormatUtils.back_indent(4)+'5. 徐汇餐饮-环境守法自助小程序使用情况-（餐饮单位）')
        print(FormatUtils.back_indent(4)+'6. 生成上述全部')

    # def prompt_text():
    #     """输入选项"""
    #     print('请选择需要生成的excel:')
    #     print(FormatUtils.back_indent(4)+'1. 静安餐饮-环境守法自助小程序使用情况-（餐饮单位）')
    #     print(FormatUtils.back_indent(4)+'2. 徐汇餐饮-环境守法自助小程序使用情况-（餐饮单位）')
    #     print(FormatUtils.back_indent(4)+'3. 生成上述全部')

    def input_excel_num():
        """输入要生成的excel对应的数字"""
        excel_num = input("请输入对应的数字：")
        # re.match('^$',excel_num)
        is_only_digits = excel_num.isdigit()
        while not is_only_digits:
            print("输入的文本不是一个有效的数字，请重新输入。")
            excel_num = input("请输入一个数字：")
            is_only_digits = excel_num.isdigit()
        return int(excel_num)
    
    def input_year():
        """输入年"""
        year = input("请输入年份(2023)(按enter键默认为今年)：")
        # 按enter键跳过，设置为今年
        if year == '' :
            return DateUtils.get_current_year()
        # 正则表达式匹配
        is_only_digits = re.match('^2\d{3}$',year)
        while not is_only_digits:
            print("输入的文本不是一个有效的年份，请重新输入。")
            year = input("请输入年份(2023)(按enter键默认为今年)：")
            is_only_digits = re.match('^2\d{3}$',year)
        return int(year)
    
    def input_month():
        """输入年"""
        month = input("请输入月份(10)(按enter键默认为当月)：")
         # 按enter键跳过，设置为今年
        if month == '' :
            return DateUtils.get_current_month()
        # 正则表达式匹配
        month_1 = re.match('^\d{1,2}$',month)
        while not month_1 or int(month) < 1 or int(month) > 12:
            print("输入的文本不是一个有效的月份，请重新输入。")
            month = input("请输入月份(10)(按enter键默认为本月)：")
            month_1 = re.match('^\d{1,2}$',month)
        return int(month)

    def input_time(text:str='开始'):
        """输入时间

        Args:
            text (str): 可选值为:"开始","结束"

        Returns:
            _type_: _description_
        """
        time = input(f"请输入{text}的时间(2023-10-01 00:00:00)(按enter键默认为本月的开始或结束时间)：")
        # 按enter键跳过，设置为默认的当月的开始和结束时间
        if time == '' and text == '开始':
            return DateUtils.get_current_month_first_day()
        if time == '' and text == '结束':
            return DateUtils.get_current_month_last_day()
        # 正则表达式匹配
        time_1= re.match('^2\d{3}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}$',time)
        while not time_1:
            print("输入的时间格式错误，请重新输入。")
            time = input(f"请输入{text}的时间(2023-10-01 00:00:00)(按enter键默认为本月的开始或结束时间)：")
            time_1 = re.match('^2\d{3}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}$',time)
        return time
    

    def interface():
        """界面"""
        Input.prompt_text()
        excel_num = Input.input_excel_num()
        year = Input.input_year()
        month = Input.input_month()
        bt = Input.input_time('开始')
        et = Input.input_time('结束')
        # 换行
        FormatUtils.line_break()                                
        print('输入的值为：',excel_num,year,month,bt,et)
        return excel_num,year,month,bt,et
    
    
    # def inp():
    #     value = input('请输入：')

    #     print(type(value))
    #     print('--'+value+'--')
    #     if value == '':
    #         print('111')

    # def input_value(func):
    #     print('run1')
    #     def in_a():
    #         print('running---')
    #         print()
    #     return func

    # @input_value   
    # def test():
    #     print('test---')
        
if __name__ == '__main__':
    # Input.prompt_text()
    # excel_num = Input.input_excel_num()
    year = Input.input_year()

    # month = Input.input_month()
    # bt = Input.input_time('结束')
    # print(bt)
    # Input.interface()
    # Input.inp()
    # 接受输入 
    # 根据数字判断

    # 生成完后 输入生成的文件路径
    # 程序退出

    