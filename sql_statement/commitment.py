
class Commitment:

    # 场景
    __scene = None
    # 区
    __district = None
    # 结束时间
    __end_time = None

    # 设置场景值
    def set_scene(self,value:int):
        if value < 1 or value > 7:
            print('场景值不在范围内')
            return
        Commitment.__scene = value

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return 
        Commitment.__district = value

    # 设置结束时间
    def set_end_time(self,value:str):
        Commitment.__end_time = value

    # 获取场景值
    def get_scene(self):
        return Commitment.__scene

    # 获取区值
    def get_district(self):
        return Commitment.__district

    # 获取结束时间
    def get_end_time(self):
        return Commitment.__end_time

    # 返回查询结果
    def back_query_sql(self):
        # 如果场景，区至少一个未被赋值时，则直接返回
        if self.__scene == None or self.__district == None:
            return 
        
        self.query_sql = f"""
                SELECT
                        b.UI_Extension1 as '区县',
                        CONCAT('"',GROUP_CONCAT(c.UI_Nick_Name SEPARATOR '\n'),'"') as '微信用户',
                        (CASE 
                            WHEN b.UI_Extension2 = 1 THEN '餐饮'
                            WHEN b.UI_Extension2 = 2 THEN '工地'
                            WHEN b.UI_Extension2 = 3 THEN '码头'
                            WHEN b.UI_Extension2 = 4 THEN '堆场'
                            WHEN b.UI_Extension2 = 5 THEN '搅拌站'
                            WHEN b.UI_Extension2 = 6 THEN '工业企业'
                            WHEN b.UI_Extension2 = 7 THEN '汽修'
                        END) as '类型',
                            b.UI_AcountName as '账号',
                        b.UI_RealName as '名称',
                        CONCAT('https://fyami.com.cn/images/', a.CM_Url) as '承诺书链接jpg',
                        CONCAT('https://fyami.com.cn/images/', a.CM_Pdf_Url) as '承诺书链接pdf',
                        max(a.CM_Create_Time) as '最新承诺时间',
                        DATEDIFF('{self.__end_time}', max(a.CM_Create_Time)) as '承诺生效天数',
                        IF(DATEDIFF('{self.__end_time}', max(a.CM_Create_Time)) > 365, '是', '否') as '是否逾期'
                        FROM
                            ea_t_commitment AS a
                        LEFT JOIN sm_t_userinfo AS b ON a.UI_GUID = b.UI_GUID
                        LEFT JOIN sm_t_userinfo_wx as c ON a.UI_GUID = c.UI_GUID
                        WHERE
                        a.CM_Create_Time <'{self.__end_time}' and
                           (b.UI_Extension2 = '{self.__scene}' AND b.UI_Extension1 = '{self.__district}')
                        GROUP BY a.UI_GUID
                        ORDER BY b.UI_Extension1, 类型, a.CM_Create_Time desc
            """
        return self.query_sql


if __name__ == '__main__':
    a = Commitment()
    a.set_district('tt')
    a.set_scene(1)
    print(a.get_scene())
    print(a.get_district())

    b =  Commitment()
    sql = a.back_user_Commitment_sql()
    print(sql)



