
class Ledger:

    # 场景
    __scene = None
    # 区
    __district = None
    # 月
    __month = None
    # 年
    __year = None
    # 季度开始
    __quarter_begin = None
    # 季度结束
    __quarter_end = None

    # 设置场景值
    def set_scene(self,value:int):
        if value < 1 or value > 7:
            print('场景值不在范围内')
            return
        Ledger.__scene = value

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return
        Ledger.__district = value

    # 设置月份
    def set_month(self,value:int):
        if value < 1 or value > 12:
            print('场景值不在范围内')
            return
        Ledger.__month = value

    # 设置月份
    def set_year(self,value:int):
        Ledger.__year = value

    def set_quarter_begin(self,value:int):
        Ledger.__quarter_begin = value

    def set_quarter_end(self,value:int):
        Ledger.__quarter_end = value

    # 获取场景值
    def get_scene(self):
        return Ledger.__scene
    # 获取区值
    def get_district(self):
        return Ledger.__district
    # 获取月值
    def get_month(self):
        return Ledger.__month
    
    # 获取年值
    def get_year(self):
        return Ledger.__year

    def def_quarter_begin(self):
        return Ledger.__quarter_begin

    def def_quarter_end(self):
        return Ledger.__quarter_end

    # 返回查询结果
    def back_query_sql(self):
        # 如果场景，区至少一个未被赋值时，则直接返回
        if self.__scene == None or self.__district == None or self.__year == None or self.__month == None:
            return 
        
        self.query_sql = f"""
                SELECT
                        b.UI_Extension1 AS '区县',
                        CONCAT(
                        '"',
                        GROUP_CONCAT(
                        e.UI_Nick_Name SEPARATOR '\n'
                        ),
                        '"'
                        ) AS '微信用户',
                        b.UI_Extension2 AS '场景类型',
                        b.UI_AcountName AS '账号',
                        b.UI_RealName AS '名称',

                        IF (f.L_TypeId = - 1, 1, 0) AS 自巡查,

                        IF (f.L_NeedUpdate = TRUE, 1, 0) AS 必填项,
                        a.LS_SubTypeId AS '台帐编号',
                        a.LS_SubTypeName AS '台帐名称',
                        a.LR_Year AS '年',
                        a.LR_Month AS '月',
                        a.LR_Day AS '日' 
                        FROM
                        ea_t_ledgerrecord AS a
                        LEFT JOIN ea_t_ledgersubtype AS f ON a.LS_SubTypeId = f.LS_SubTypeId
                        LEFT JOIN sm_t_userinfo AS b ON a.LR_SubmitID = b.UI_GUID
                        LEFT JOIN ea_t_restaurant_base_info AS c ON b.UI_GUID = c.RB_GUID
                        LEFT JOIN ea_t_baseinfo AS d ON b.UI_GUID = d.BI_GUID
                        LEFT JOIN sm_t_userinfo_wx AS e ON b.UI_GUID = e.UI_GUID
                        WHERE
                        a.LR_Year = {self.__year}
                        AND (
                        -- 年度
                        (a.LR_Month BETWEEN 1 AND 12
                        AND f.L_Period = 12 and (a.LR_Extension2 != 'notInvolved' or a.LR_Extension2 is null ))
                        -- 半年度
                        OR
                        (a.LR_Month BETWEEN 1 AND 6
                        AND f.L_Period = 6 and (a.LR_Extension2 != 'notInvolved' or a.LR_Extension2 is null ))
                        -- 季度
                        OR
                        (a.LR_Month BETWEEN {self.__quarter_begin} AND {self.__quarter_end}
                        AND f.L_Period = 3 and (a.LR_Extension2 != 'notInvolved' or a.LR_Extension2 is null ))
                        -- 月度
                        OR
                        (a.LR_Month = {self.__month})
                        ) 
                        AND (
                        (
                        b.UI_Extension2 = '{self.__scene}'
                        AND b.UI_Extension1 = '{self.__district}'
                        )
                        )
                        GROUP BY
                        b.UI_AcountName,
                        a.LR_Year,
                        a.LS_SubTypeId
                        ORDER BY
                        b.UI_Extension2,
                        b.UI_AcountName,
                        a.LR_Year DESC,
                        a.LR_Month DESC,
                        a.LS_SubTypeId
            """
        return self.query_sql


if __name__ == '__main__':
    a = Ledger()
    a.set_district('静安区')
    a.set_scene(1)
    a.set_month(11)
    a.set_year(2023)
    print(a.get_scene())
    print(a.get_district())

    b =  Ledger()
    sql = a.back_Ledger_sql()
    print(sql)



