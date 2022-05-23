import datetime,os,glob,shutil,time,sys
from func.Write_log import Write_log

# 按今天日期,和距今天数backup_days,返回日期列表
def Get_copy_dates(backup_days,today=1):
    date_list = []
    for i in range(1-today, backup_days):
        curr_date = (datetime.datetime.now() - datetime.timedelta(days=i)).strftime("%Y\%m\%d")
        date_list.append(curr_date)
    return date_list


def Create_folder(dest_path):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)


# 获取目录列表
def Get_dir_list(source_path):
    dir_list=[]
    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isdir(i):
            dir_list.append(i)
    return dir_list


# 获取目录文件列表,如果传递进来是一个文件也可以
def Get_file_list(source_path):
    files_list=[]
    if os.path.isfile(source_path):
        files_list.append(source_path)
        return files_list

    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list





import configparser
#读取ini方法
def Read_ini(inivaluse,inikey='param'):
        config = configparser.ConfigParser()
        config.read("config.ini",encoding="utf-8-sig")
        convaluse=config.get(inikey,inivaluse)
        return convaluse