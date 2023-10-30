
from sqlalchemy import create_engine
class Connection:
    """ 远程数据库 """
    con_read = None
    con_write = None
    ip = '47.100.191.150'
    user = 'remoteU2'
    password = 'feiyu2021'
    port = 3306
    data_base_name = 'ledger'


    """ 本机 """
    # con_read = None
    # con_write = None
    # ip = 'localhost'
    # user = 'root'
    # password = '1234'
    # port = 3306
    # data_base_name = 'qianduan_sql'



    """连接数据库
    """
    def connect_remote_database_read(self):


        if self.con_read == None or self.con_read.closed:
            engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.port}/{self.data_base_name}?charset=utf8",pool_recycle=3600, pool_size=3, max_overflow=0)
            self.con_read = engine.connect()
        return self.con_read

    def connect_remote_database_write(self):
        """ 写"""

    
        if self.con_write == None or self.con_write.closed:
            engine = create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.ip}:{self.port}/{self.data_base_name}?charset=utf8",pool_recycle=3600, pool_size=3, max_overflow=0)
            self.con_write = engine.connect()
        return self.con_write


    def disconnect(self,area_type:str,option_type:str):
        """"断开连接

        Args:
            area_type (str): 数据库所属位置。local与remote
            option_type (str): 操作类型。write和read
        """

        self.con_read.close()


# 其他文件导入此对象即可 
datebase_single_obj = Connection()

