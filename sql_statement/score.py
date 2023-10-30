
class Score:

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
        Score.__scene = value

    # 设置区值
    def set_district(self,value:str):
        if value != '静安区' and value != '徐汇区' and value != '金山区':
            print('区不在范围内')
            return
        Score.__district = value

    # 设置开始时间
    def set_begin_time(self,value:str):
        Score.__begin_time = value

    # 设置结束时间
    def set_end_time(self,value:str):
        Score.__end_time = value

    # 获取场景值
    def get_scene(self):
        return Score.__scene
    # 获取区值
    def get_district(self):
        return Score.__district
    # 获取月值
    def get_begin_time(self):
        return Score.__begin_time
    
    # 获取年值
    def get_end_time(self):
        return Score.__end_time


    # 返回查询结果
    def back_query_sql(self):
        # 如果场景，区至少一个未被赋值时，则直接返回
        if self.__scene == None or self.__district == None or self.__begin_time == None or self.__end_time == None:
            return 
        #       set @row_item:='';
        #       set @median_group:='';

        self.query_sql = f"""
                SELECT
                    d.UI_Nick_Name as '微信用户',
                    b.UI_Extension2 as '场景类型',
                        b.UI_AcountName as '账号',
                    b.UI_RealName as '名称',
                    c.ER_RuleName as '类型',
                    a.E_ScenseName as '季度',
                    a.E_EvaluatoruserName as '评分人',
                    a.E_ResultScoreBef as '得分',
                    a.E_CreateDate as '时间'
                    FROM
                        ea_t_evaluation AS a
                    LEFT JOIN sm_t_userinfo AS b ON a.I_GUID = b.UI_GUID
                    LEFT JOIN sm_t_evaluationrule as c on a.ST_GUID = c.ER_GUID
                    LEFT JOIN sm_t_userinfo_wx as d ON b.UI_GUID = d.UI_GUID
                    LEFT JOIN ea_t_itemevaluation as e ON a.E_GUID = e.S_GUID
                    WHERE
                    c.ER_RuleType = 0
                    AND 
                    a.E_CreateDate BETWEEN '{self.__begin_time}' AND '{self.__end_time}'
                        AND (
                    (b.UI_Extension2 = '{self.__scene}' AND b.UI_Extension1 = '{self.__district}')
                        )
                    AND b.UI_IsEnable = '1'
                    GROUP BY b.UI_GUID, a.E_ScenseName
                    ORDER BY b.UI_Extension2, a.E_ScenseName desc, b.UI_AcountName, a.E_ERType
            """
        return self.query_sql


if __name__ == '__main__':
    a = Score()
    a.set_district('静安区')
    a.set_scene(1)
    a.set_begin_time('2023-05-1 00:00:00')
    a.set_end_time('2023-05-1 00:00:00')
    print(a.get_scene())
    print(a.get_district())

    b =  Score()
    sql = a.back_Score_sql()
    print(sql)



