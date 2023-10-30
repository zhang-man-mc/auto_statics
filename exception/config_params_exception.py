import sys
import os
# 获取当前文件所在目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录的路径（假设项目根目录在当前文件的上一级目录）
project_dir = os.path.dirname(current_dir)
# 将项目根目录的路径添加到系统环境变量中
sys.path.insert(0, project_dir)

from utils.log_utils import LogUtils

class ParamsException(Exception):
    def __init__(self,error_id:int):
        self.error_id = error_id


    def output_error_by_num(self):
        if self.error_id == 0:
            LogUtils.error('开始时间 格式不符合规范')
        if self.error_id == 1:
            LogUtils.error('结束时间 格式不符合规范')
        if self.error_id == 2:
            LogUtils.error('开始时间不能大于结束时间')
        if self.error_id == 3:
            LogUtils.error('开始和结束时间不能跨度到其他月份')
        if self.error_id == 4:
            LogUtils.error('年份 格式不符合规范')
        if self.error_id == 5:
            LogUtils.error('月份 格式不符合规范') 
        if self.error_id == 6:
            LogUtils.error('起始时间与月份应该在同一个月')   
        LogUtils.error('配置文件中时间格式无效，请检查时间参数')


if __name__ == '__main__':
    c = ParamsException(1)
    print(c)