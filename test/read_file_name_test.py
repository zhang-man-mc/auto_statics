
import os

def get_all_files_in_folder(folder_path):
    """
    获取指定文件夹下的所有文件名

    :param folder_path: 文件夹路径
    :return: 包含所有文件名的列表
    """
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        return files
    # return file_names

folder_path = r"C:\Users\Administrator\Desktop\9月" 
file_names = get_all_files_in_folder(folder_path)


# # 打印所有文件名
for file_name in file_names:
    print(file_name)
    print('\n') 




# for i,j,k in os.walk(folder_path):
#     print(i,j,k)


file_names = os.listdir(folder_path)
print(file_names)