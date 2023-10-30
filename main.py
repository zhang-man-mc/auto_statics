
import sys
import os
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录的路径（假设项目根目录在当前文件的上一级目录）
project_dir = os.path.dirname(current_dir)
# 将项目根目录的路径添加到系统环境变量中
sys.path.insert(0, project_dir)

from service.generate_service import GenerateService
from condition_parameter.function_parameter import FuncParm
from utils.path_file import output_current_path
from interface.user_input import Input
from utils.format_utils import FormatUtils
from global_configuration.config import Config
from utils.log_utils import LogUtils

# def main():
#     while True:
#         # 交互界面
#         excel_num,year,month,bt,et = Input.interface()
#
#         generate_service = GenerateService()
#         # 生成excel
#         generate_service.generate_excel_by_selected_num(excel_num,year,month,bt,et)
#         # 生成的excel路径
#         print(f'文件保存路径在：{output_current_path()}'+'\\new_excel')
#         FormatUtils.line_break()



def main():
    config = Config()
    # 检查读入的配置信息是否有效
    if not config.get_is_config_value_valid():
        return
    
    # 实例化
    generate_service = GenerateService()
    # 生成excel
    generate_service.generate_excel_by_selected_num(config.get_select_num(),config.get_year(),config.get_month(),config.get_begin_time(),config.get_end_time())
    # 生成的excel路径
    LogUtils.info(f'文件保存路径在：{output_current_path()}'+'\\new_excel')
    FormatUtils.line_break()
    
    input("按回车键结束")


if __name__ == '__main__':
    main()