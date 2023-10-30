
class UserLogin:

    # 场景
    __scene = None
    # 区
    __district = None
    # 开始时间
    __begin_time = None
    # 结束时间
    __end_time = None

    # 设置场景值
    def set_scene(self,value:int):
        if value < 1 or value > 7:
            print('场景值不在范围内')
            return
        UserLogin.__scene = value

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return
        UserLogin.__district = value

    # 设置开始时间
    def set_begin_time(self,value:str):
        UserLogin.__begin_time = value

    # 设置结束时间
    def set_end_time(self,value:str):
        UserLogin.__end_time = value

    # 获取场景值
    def get_scene(self):
        return UserLogin.__scene
    # 获取区值
    def get_district(self):
        return UserLogin.__district
    # 获取开始时间
    def get_begin_time(self):
        return UserLogin.__begin_time

    # 获取结束时间
    def get_end_time(self):
        return UserLogin.__end_time

    # 返回查询结果
    def back_query_sql(self):
        # 如果场景，区至少一个未被赋值时，则直接返回
        if self.__scene == None or self.__district == None or self.__begin_time == None :
            return 
        
        self.query_sql = f"""
                SELECT
                        d.UI_AcountName as "账号",
                        d.UI_RealName as "场景名称",
                        CONCAT('"',GROUP_CONCAT(a.UI_Nick_Name SEPARATOR '\n'),'"') as '微信用户',
                         b.RB_Concentration_Area as "集中区",
                        b.RB_Cooking_Fumes_Type as '油烟类型',
                        d.UI_Extension2 as '场景类型',
                        d.UI_Extension1 as '区县',
                        CASE 
                                WHEN f.UL_User_GUID IS NOT NULL THEN '已登录'
                                ELSE '未登录'
                            END as '登录情况'
                        FROM
                         sm_t_userinfo as d
                        LEFT JOIN ea_t_restaurant_base_info AS b ON d.UI_GUID = b.RB_GUID
                        LEFT JOIN ea_t_baseinfo AS c ON d.UI_GUID = c.BI_GUID
                        LEFT JOIN sm_t_userinfo_wx AS a ON a.UI_GUID = d.UI_GUID
                        LEFT JOIN 
                            (
                                SELECT DISTINCT UL_User_GUID
                                FROM sm_t_user_login_log
                                WHERE UL_Login_Time BETWEEN '{self.__begin_time}' AND '{self.__end_time}'
                            ) AS f ON d.UI_GUID = f.UL_User_GUID
                        WHERE
                         d.UI_Extension1 = '{self.__district}'  
                        and d.UI_Extension2 = '{self.__scene}' 
                        and d.UI_IsEnable = true
                        AND d.UI_UserTypeID = 3
                        AND (d.UI_WorkNo != 'test' or d.UI_WorkNo is null)
                        GROUP BY d.UI_GUID
                        ORDER BY d.UI_AcountName, d.UI_Extension2
            """
        return self.query_sql


if __name__ == '__main__':
    a = UserLogin()
    a.set_district('静安区')
    a.set_scene(1)
    a.set_begin_time('2023-05-1 00:00:00')
    print(a.get_scene())
    print(a.get_district())

    b =  UserLogin()
    sql = a.back_UserLogin_sql()
    print(sql)



