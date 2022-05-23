import os
import datetime,os,glob,shutil

days =['2021-05-11', '2021-05-10', '2021-05-09', '2021-05-08', '2021-05-07', '2021-05-06', '2021-05-05', '2021-05-04', '2021-05-03', '2021-05-02', '2021-05-01', '2021-04-30', '2021-04-29', '2021-04-28', '2021-04-27']

source_path = r'd:\pic1'
dest_path =r'y:\pic1'
backup_days = 10



# 根据源文件夹，在目标文件夹建立相同目录结构
def Create_folder(dest_path):
    if not os.path.exists(dest_path):
            os.makedirs(dest_path)

path=r'D:\pic1\2021\13'
shutil.rmtree(path)

# for i in days:
#     Create_folder(os.path.join(source_path,i))

