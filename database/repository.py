
from database.database_connection import datebase_single_obj
from sql_statement.authentication import Authentication
from sqlalchemy import text
class Repository:

    def read_from_database_ledger(self,query_sql:str)->list:
        """根据sql语句返回查询结果

        Args:
            query_sql (str): sql语句

        Returns:
            _type_: 查询结果
        """
        with datebase_single_obj.connect_remote_database_read() as con:
            result = con.execute(text(query_sql))
        return result.all()
    
    def read_authentication_situation1(self):
        """认证情况
        """
        with datebase_single_obj.connect_remote_database_read() as con:
            query_sql = 'select * from ja_t_dust_site_data_info limit 10'
            result = con.execute(text(query_sql))
            # print(result.all())
            # a = result.all()
            # for i in range(1, len(a)+1):
            #     for j in range(1,len(a[i-1])+1):
            #         print(a[i-1][j-1])
            # for row in result:
            #     print(f"x: {row.mn_code}  y: {row.dust_value}")
        return result.all()
    
if __name__ == '__main__':
    query_sql =Authentication().back_query_sql()
    r = Authentication()
    r.set_district('静安区')
    r.set_scene(1)
    rep = Repository()
    a = rep.read_authentication_situation1()
    # for i in range(1,7):
    #     print(i)
    print(a)