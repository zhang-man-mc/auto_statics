
class Authentication:

    # 场景
    __scene = None
    # 区
    __district = None


    # 设置场景值
    def set_scene(self,value:int):
        if value < 1 or value > 7:
            print('场景值不在范围内')
            return
        Authentication.__scene = value

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return
        Authentication.__district = value

    # 获取场景值
    def get_scene(self):
        return Authentication.__scene
    # 获取区值
    def get_district(self):
        return Authentication.__district

    # 返回查询结果
    def back_query_sql(self):
        # 如果场景，区至少一个未被赋值时，则直接返回
        if self.__scene == None or self.__district == None:
            return 
        
        self.query_sql = f"""
                    SELECT
                        (CASE 
                            WHEN e.UI_Extension2 = 1 THEN '餐饮'
                            WHEN e.UI_Extension2 = 2 THEN '工地'
                            WHEN e.UI_Extension2 = 3 THEN '码头'
                            WHEN e.UI_Extension2 = 4 THEN '堆场'
                            WHEN e.UI_Extension2 = 5 THEN '搅拌站'
                            WHEN e.UI_Extension2 = 6 THEN '工业企业'
                            WHEN e.UI_Extension2 = 7 THEN '汽修'
                        END) as '类型',
                        e.UI_AcountName AS '账户',
                        e.UI_RealName AS '用户名',
                        b.BI_Name AS '场景名称',
                        IF(b.BI_Extension3 is null, '未认证', '已认证') AS '场景认证',
                        c.CI_Name AS '企业名称',
                        IF(c.CI_Extension3 is null, '未认证', '已认证') AS '企业认证',
                        CONCAT('"',GROUP_CONCAT(IF(a.UI_Nick_Name is null, '/', a.UI_Nick_Name) SEPARATOR '\n'),'"') as '微信昵称',
                        CONCAT('"',GROUP_CONCAT(IF(d.PI_Name is null, '/', d.PI_Name) SEPARATOR '\n'),'"') as '微信用户实名',
                        CONCAT('"',GROUP_CONCAT(IF(d.PI_ID_Type is null, '/', d.PI_ID_Type) SEPARATOR '\n'),'"') as '证件类型',
                        CONCAT('"',GROUP_CONCAT(IF(d.PI_ID is null, '/', d.PI_ID) SEPARATOR '\n'),'"') as '证件号',
                        CONCAT('"',GROUP_CONCAT(IF(d.PI_Position is null, '/', d.PI_Position) SEPARATOR '\n'),'"') as '职位',
                        CONCAT('"',GROUP_CONCAT(IF(d.PI_Extension3 is null, '未认证', '已认证') SEPARATOR '\n'),'"') as '个人认证'
                        FROM
                        sm_t_userinfo as e
                        LEFT JOIN sm_t_userinfo_wx AS a ON a.UI_GUID = e.UI_GUID
                        LEFT JOIN ea_t_baseinfo AS b on b.BI_GUID = e.UI_GUID
                        LEFT JOIN ea_companyinfo AS c ON b.CI_GUID = c.CI_GUID
                        LEFT JOIN ea_t_personal_info as d on a.PI_GUID = d.PI_GUID
                        WHERE 
                        (e.UI_Extension2 = '{self.__scene}' AND e.UI_Extension1 = '{self.__district}')
                        and e.UI_IsEnable = true
                        AND e.UI_UserTypeID = 3
                        AND (e.UI_WorkNo != 'test' or e.UI_WorkNo is null)
                        GROUP BY e.UI_GUID
                        ORDER BY 类型
            """
        return self.query_sql


if __name__ == '__main__':
    a = Authentication()
    a.set_district('静安区')
    a.set_scene(1)
    print(a.get_scene())
    print(a.get_district())

    b =  Authentication()
    sql = a.back_user_authentication_sql()
    print(sql)



