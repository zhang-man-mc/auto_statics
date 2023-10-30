
class Scene:
    # 餐饮
    __scene_1 = 1  
    # 工地
    __scene_2 = 2 
    # 码头
    __scene_3 = 3 
    # 堆场
    __scene_4 = 4 
    # 搅拌站
    __scene_5 = 5 
    # 工业企业
    __scene_6 = 6 
    # 汽修
    __scene_7 = 7 


    @staticmethod
    def get_scene1():
        return Scene.__scene_1
    @staticmethod
    def get_scene2():
        return Scene.__scene_2
    @staticmethod
    def get_scene3():
        return Scene.__scene_3
    @staticmethod
    def get_scene4():
        return Scene.__scene_4
    @staticmethod
    def get_scene5():
        return Scene.__scene_5
    @staticmethod
    def get_scene6():
        return Scene.__scene_6
    @staticmethod
    def get_scene7():
        return Scene.__scene_7
    
    def get_scene_description(scene_id:int):
        """根据场景id返回场景描述

        Args:
            scene_id (_type_): 场景id
        """
        if scene_id == 1:
            return '餐饮'
        if scene_id == 2 :
            return '工地'
        if scene_id == 3 :
            return '码头'
        if scene_id == 4 :
            return '堆场'
        if scene_id == 5 :
            return '搅拌站'
        if scene_id == 6 :
            return '碳谷绿湾工业企业'
        if scene_id == 7 :
            return '汽修'

        

if __name__ == '__main__':
    print(Scene.get_scene1())
    print(Scene.get_scene4())