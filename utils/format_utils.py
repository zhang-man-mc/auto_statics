
class FormatUtils: 

    
    @staticmethod 
    def line_break(num_lines:int=1): 
        """ 添加换行符
        param num_lines: 需要换行的行数,默认为1 
        """ 
        print('\n' * num_lines) 
    
    
    @staticmethod 
    def indent(num_spaces:int=4): 
        """ 添加缩进 
        param num_spaces: 缩进的空格数,默认为4 
        """ 
        print(' ' * num_spaces, end='')

    @staticmethod 
    def back_indent(num_spaces:int=4): 
        return ' '*num_spaces
    

    
    
