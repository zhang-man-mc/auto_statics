import os

def get_all_files_in_folder(folder_path:str,exclude_file_name:str)->list:
    """输出指定文件夹下的所有文件名(不包括文件夹),不包括exclude_file_name

    Args:
        folder_path (str): 文件夹路径
        exclude_file_name(str):排除的文件名

    Returns:
        _type_: 包含所有文件名的列表
    """
    for root, dirs, files in os.walk(folder_path):
        """其中root是当前文件夹的路径,dirs是当前文件夹中的子文件夹列表,files是当前文件夹中的文件列表"""
        if folder_path in files:
            files.remove(exclude_file_name)
        return files
    

def is_new_excel_file_exist(path:str='./new_excel'):
    if not os.path.exists(path):
        os.makedirs(path)


def output_current_path():
    return os.getcwd()

if __name__ == '__main__':
    # folder_path = r"./" 
    # file_names = get_all_files_in_folder(folder_path,'main.exe')

    # print(file_names)

    # is_new_excel_file_exist()
    print(output_current_path())

