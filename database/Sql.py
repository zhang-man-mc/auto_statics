
""" 查询语句 """

class Sql:
    

    @staticmethod
    def query_letter_of_commitment(scene_type:int,district:str):
        """"""
        query_sql = f"""SELECT
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
                            -- b.UI_GUID, 
                            b.UI_RealName as '名称',
                            CONCAT('https://fyami.com.cn/images/', a.CM_Url) as '承诺书链接jpg',
                            CONCAT('https://fyami.com.cn/images/', a.CM_Pdf_Url) as '承诺书链接pdf',
                            max(a.CM_Create_Time) as '最新承诺时间',
                            DATEDIFF(NOW(), max(a.CM_Create_Time)) as '承诺生效天数',
                            IF(DATEDIFF(NOW(), max(a.CM_Create_Time)) > 365, '是', '否') as '是否逾期'
                            FROM
                                ea_t_commitment AS a
                            LEFT JOIN sm_t_userinfo AS b ON a.UI_GUID = b.UI_GUID
                            LEFT JOIN sm_t_userinfo_wx as c ON a.UI_GUID = c.UI_GUID
                            WHERE
                            (b.UI_Extension2 = '{scene_type}' AND b.UI_Extension1 = '{district}')
                            GROUP BY a.UI_GUID
                            ORDER BY b.UI_Extension1, 类型, a.CM_Create_Time desc
        """
        return query_sql

if __name__ == '__main__':
    print(Sql.query_letter_of_commitment(1,'金山区'))