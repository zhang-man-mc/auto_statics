# import sys
# import os
# # 获取当前文件所在目录的绝对路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# # 获取项目根目录的路径（假设项目根目录在当前文件的上一级目录）
# project_dir = os.path.dirname(current_dir)
# # 将项目根目录的路径添加到系统环境变量中
# sys.path.insert(0, project_dir)

from service.init_condition import *
from database.repository import Repository
from excel.excel_operation import ExcelOperation
from condition_parameter.function_parameter import FuncParm
from utils.date_utils import DateUtils
from utils.path_file import is_new_excel_file_exist
from utils.log_utils import LogUtils
class GenerateService:
    def __init__(self):
        # 初始化sql语句
        self.__objs = init_obj()
        # 初始化数据库的查询
        self.rep = Repository()
        
    def init_condition_parameter(self,scene:int,district:str,year:int,month:int,begin_time:str,end_time:str):
        """对5个统计对象初始化查询条件"""
        init(self.__objs,scene,district,year,month,begin_time,end_time)

    def get_all_sql(self):
        """获得五个统计类型的Sql查询语句"""
        if self.__objs == None:
            return
        query_sql = []
        # 将每个统计类型的sql语句存储到query_sql中
        for item in self.__objs:
            sql= item.back_query_sql()
            query_sql.append(sql)
        return query_sql

    def query_five_data_from_database(self,query_sql:list):
        """获得五个统计类型的Sql查询语句"""
        data = []
        for sql in query_sql:
            d = self.rep.read_from_database_ledger(sql)
            data.append(d)
        return data
    

    
    def generate_statistical_excel(self,sql_params:FuncParm):
        """生成一张统计表格"""
        # 初始化各个sql语句的参数变量
        self.init_condition_parameter(sql_params.scene,sql_params.district,sql_params.year,sql_params.month,sql_params.begin_time,sql_params.end_time)
        # 获得待查询的sql语句
        sql = self.get_all_sql()
        # 拿到查询的结果
        data = self.query_five_data_from_database(sql)
        # 形成excel的文件名
        new_excel_name = ExcelOperation.Generate_excel_name_by_dynamic_parameters(sql_params)
        # 判断当前路径是否存在new_excel文件夹，没有则创建
        is_new_excel_file_exist()
        # 写入到原excel文件的sheet中，并保存
        ExcelOperation.save_to_origin_excel(sql_params.origin_excel_name,new_excel_name,data)




    def output_jin_shang_catering_statics_excel(self,func_parm:FuncParm):
        # 生成统计表
        self.generate_statistical_excel(func_parm)

    def output_jin_shang_construction_site_statics_excel(self,func_parm:FuncParm):
       
        # 生成统计表
        self.generate_statistical_excel(func_parm)

    def output_jin_shang_industrial_enterprise_statics_excel(self,func_parm:FuncParm):
        # 生成统计表
        self.generate_statistical_excel(func_parm)
    
    def output_jin_an_catering_statics_excel(self,func_parm:FuncParm):
        # 生成统计表
        self.generate_statistical_excel(func_parm)

    def output_xu_hui_catering_statics_excel(self,func_parm:FuncParm):
        # 生成统计表
        self.generate_statistical_excel(func_parm)

    # 生成所有的excel
    # def output_all(self,func_parm):
        
   
    def generate_excel_by_selected_num(self,selected_num:int,year:int,month:int,begin_time:str,end_time:str):
        LogUtils.info(f'配置参数为：{selected_num} {year} {month} {begin_time} {end_time}')
        if int(selected_num) == 1:
            jin_shan_catering = FuncParm('金山餐饮-小程序',1,'金山区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_catering)+'正在生成...')
            self.output_jin_shang_catering_statics_excel(jin_shan_catering)
            return 
        if int(selected_num) == 2:
            jin_shan_construction_site = FuncParm('金山工地-小程序',2,'金山区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_construction_site)+'正在生成...')
            self.output_jin_shang_construction_site_statics_excel(jin_shan_construction_site)
            return
        if int(selected_num) == 3:
            jin_shan_industrial_enterprise = FuncParm('金山碳谷绿湾工业企业-小程序',6,'金山区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_industrial_enterprise)+'正在生成...')
            self.output_jin_shang_industrial_enterprise_statics_excel(jin_shan_industrial_enterprise)
            return
        if int(selected_num) == 4:
            jin_an_catering = FuncParm('静安餐饮-小程序',1,'静安区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_an_catering)+'正在生成...')
            self.output_jin_an_catering_statics_excel(jin_an_catering)
            return
        if int(selected_num) == 5:
            xu_hui_catering = FuncParm('徐汇餐饮-小程序',1,'徐汇区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(xu_hui_catering)+'正在生成...')
            self.output_xu_hui_catering_statics_excel(xu_hui_catering)
            return
        if int(selected_num) == 6:
            jin_shan_catering = FuncParm('金山餐饮-小程序',1,'金山区',year,month,begin_time,end_time)
            jin_shan_construction_site = FuncParm('金山工地-小程序',2,'金山区',year,month,begin_time,end_time)
            jin_shan_industrial_enterprise = FuncParm('金山碳谷绿湾工业企业-小程序',6,'金山区',year,month,begin_time,end_time)
            jin_an_catering = FuncParm('静安餐饮-小程序',1,'静安区',year,month,begin_time,end_time)
            xu_hui_catering = FuncParm('徐汇餐饮-小程序',1,'徐汇区',year,month,begin_time,end_time)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_catering)+'正在生成...')
            self.output_jin_shang_catering_statics_excel(jin_shan_catering)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_construction_site)+'正在生成...')
            self.output_jin_shang_construction_site_statics_excel(jin_shan_construction_site)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_shan_industrial_enterprise)+'正在生成...')
            self.output_jin_shang_industrial_enterprise_statics_excel(jin_shan_industrial_enterprise)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(jin_an_catering)+'正在生成...')
            self.output_jin_an_catering_statics_excel(jin_an_catering)
            LogUtils.info(ExcelOperation.Generate_excel_name_by_dynamic_parameters(xu_hui_catering)+'正在生成...')
            self.output_xu_hui_catering_statics_excel(xu_hui_catering)
            return

    # def generate_excel_by_selected_num(self,selected_num:int,year:int,month:int,begin_time:str,end_time:str):
    #     if int(selected_num) == 1:
    #         jin_an_catering = FuncParm('静安餐饮-小程序',1,'静安区',year,month,begin_time,end_time)
    #         self.output_jin_an_catering_statics_excel(jin_an_catering)
    #         return
    #     if int(selected_num) == 2:
    #         xu_hui_catering = FuncParm('徐汇餐饮-小程序',1,'徐汇区',year,month,begin_time,end_time)
    #         self.output_xu_hui_catering_statics_excel(xu_hui_catering)
    #         return
    #     if int(selected_num) == 3:
    #         jin_shan_catering = FuncParm('金山餐饮-小程序',1,'金山区',year,month,begin_time,end_time)
    #         jin_shan_construction_site = FuncParm('金山工地-小程序',2,'金山区',year,month,begin_time,end_time)
    #         jin_shan_industrial_enterprise = FuncParm('金山工业企业-小程序',6,'金山区',year,month,begin_time,end_time)
    #         jin_an_catering = FuncParm('静安餐饮-小程序',1,'静安区',year,month,begin_time,end_time)
    #         xu_hui_catering = FuncParm('徐汇餐饮-小程序',1,'徐汇区',year,month,begin_time,end_time)

    #         self.output_jin_shang_catering_statics_excel(jin_shan_catering)
    #         self.output_jin_shang_construction_site_statics_excel(jin_shan_construction_site)
    #         self.output_jin_shang_industrial_enterprise_statics_excel(jin_shan_industrial_enterprise)
    #         self.output_jin_an_catering_statics_excel(jin_an_catering)
    #         self.output_xu_hui_catering_statics_excel(xu_hui_catering)
    #         return
        
        
if __name__ == '__main__':
    # 初始化sql查询参数
    func_parm = FuncParm(1,'金山区',2023,10,'2023-10-01 00:00:00','2023-10-31 23:59:59','jins_1','jins_1_10')
    g = GenerateService()
    # 生成统计表
    g.generate_statistical_excel(func_parm)
