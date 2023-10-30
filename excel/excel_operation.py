
from excel.excel import Excel
from condition_parameter.function_parameter import FuncParm
from condition_parameter.scene import Scene
from utils.date_utils import DateUtils
from excel.sheet_cols import ColumnDelete
from utils.log_utils import  LogUtils
from utils.format_utils import FormatUtils
class ExcelOperation:

    def write_to_sheet(sheet,data_list:list):
        """写入sheet"""
        for i in range(1, len(data_list)+1):
            for j in range(1,len(data_list[i-1])+1):
                # 表示将data_list列表的第0个元素的第0个数据，写入到excel表格的第2行第一列				
                sheet.cell(i+1 , j, data_list[i - 1][j-1])					
        # print('写入成功')


    def save_to_origin_excel(origin_excel_name:str,new_excel_name:str,data:list):
        """将数据写入到原始excel表中

        Args:
            origin_excel_name (str): 原始excel文件名
            new_excel_name (str): 新的excel文件名
            data (list): 待写入的数据
        """
        e = Excel()
        # 获得excel表对象
        excel_obj = e.get_excel_file_obj(origin_excel_name)
        # 得到所有sheet名字
        sheet_names = e.get_all_sheet_names(excel_obj)
        # 最多只有6个sheet
        # if len(sheet_names) > 6:
        #     del sheet_names[-1]
        # 去掉“统计”的sheet
        # to_be_written_sheet_nums = len(sheet_names) - 1
        to_be_written_sheet_nums = 5
        # 待写入的数据元素个数应该与sheet数量相同
        if len(data) != to_be_written_sheet_nums:
            LogUtils.error('传入的数据个数不等于待写入的sheet数量')
            return
        # 各个sheet需要清空的列
        delete_max_cols = ColumnDelete.get_sheets_delete_cols()
        # 将数据分别写入5个sheet
        for i in range(to_be_written_sheet_nums):
            # 获得该sheet对象
            sheet_obj = e.get_sheet(excel_obj,sheet_names[i])
            # 清空sheet的指定列
            e.del_cols_range_from_second_row(sheet_obj,delete_max_cols[i])
            # 将值写入sheet
            ExcelOperation.write_to_sheet(sheet_obj,data[i])
        # 保存成新的表
        e.save_to_new_excel(excel_obj,new_excel_name)
        LogUtils.info('excel表生成完毕')
        FormatUtils.line_break()

    def Generate_excel_name_by_dynamic_parameters(function_parameters:FuncParm)->str:
        """根据场景,区,时间参数生成excel文件名字

        Args:
            function_parameters (FuncParm): 传入的查询条件对象

        Returns:
            str: 新的文件名
        """
        if isinstance(function_parameters,FuncParm) != True:
            LogUtils.error('生成excel文件名 传参类型错误')
            return
        district = function_parameters.district[:2]
        scene = Scene.get_scene_description(function_parameters.scene)
        today_date = DateUtils.today_date()
        # excel_name = district + scene + f'-环境守法自助小程序使用情况-（{scene}单位）-' + function_parameters.district + '-统计截至' + today_date
        excel_name = district + scene + f'小程序'+ str(DateUtils.get_month_by_time(function_parameters.begin_time)) +'月使用情况-' + today_date
        return excel_name


if __name__ == '__main__':
    # data = [
    #         [1,2,3,4,5,6],
    #         [1,2,3,4,5,6],
    #         [1,2,3,4,5,6],
    #         [1,2,3,4,5,6],
    #         [1,2,3,4,5,6]
    #         ]
    data = [[
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]
            ],
            [
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]
            ],
            [
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]
            ],
            [
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]
            ],
            [
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]
            ]]
    ExcelOperation.save_to_origin_excel('nine','nine_1019',data)