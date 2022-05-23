import os,glob
# 获取目录文件列表
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list

path = r'D:\pic1\2021\05\02\B00UU00A100BCM1SAY8G'
# path = r'D:\\pic1\\2021\\05\\02\\B00UU00A100BCM1SAY8G\\B00UU00A100BCM1SAY8G-205956-0-13.jpg'

files_list = Get_file_list(path)
print(files_list)