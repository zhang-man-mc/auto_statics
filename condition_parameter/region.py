
class Region:

    __region1 = '静安区'
    __region2 = '徐汇区'
    __region3 = '金山区'



    def get_region1():
        """
            region1 = '静安区'
            region2 = '徐汇区'
            region3 = '金山区'
        Returns:
            _type_: 
        """
        return Region.__region1
    
    def get_region2():
        """
            region1 = '静安区'
            region2 = '徐汇区'
            region3 = '金山区'
        Returns:
            _type_: 
        """
        return Region.__region2
    
    def get_region3():
        """
            region1 = '静安区'
            region2 = '徐汇区'
            region3 = '金山区'
        Returns:
            _type_: 
        """
        return Region.__region3




if __name__ == '__main__':
    print(Region.get_region1())
    print(Region.get_region3())