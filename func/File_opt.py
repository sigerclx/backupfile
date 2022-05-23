import datetime,os,time,sys,shutil
from func.tools import *
from func.Write_log import Write_log
from func.param import *

def Copy_file(file):
    sleepms = Get_value("copy_onefile_sleep")  # 每拷贝一个文件休息copy_onefile_sleep时间
    source_path = Get_value('source_path')  # 定义源文件夹
    dest_path1 = Get_value('dest_path')  # 定义目的文件夹

    dest_file = file.replace(source_path, dest_path1)
    dest_path = dest_file[0:dest_file.rfind("\\")]

    # 目标文件夹不存在,则建立
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
        Write_log(dest_path + " Created ")

    try:
        shutil.copy2(file, dest_path)
        time.sleep(sleepms)
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        Write_log("copying " + file + ' to ' + dest_path)
    except Exception:
        print("Copying " + file + ' to ' + dest_path + " sleep : " + str(sleepms) + '...')
        Write_log("copying " + file + ' to ' + dest_path + ' error: 源文件找不到 或其他错误')


def Delete_file(file):
    # 删除目录下的文件,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = Get_value("delete_onefile_sleep")
    source_path = Get_value("source_path")
    dest_path = Get_value("dest_path")
    delete_file = Get_value("deletefile")
    # 获取源目录里需要保留（不能删除）的目录清单
    date_list = Get_value("date_list")
    if os.path.exists(file.replace(source_path,dest_path)):
        # 如果路径不含被保护的日期，则可以删除
        if not any(s in file for s in date_list):
            try:
                if delete_file:
                    os.remove (file)
                    time.sleep(sleepms)
                    Write_log('deleting file ' + file + ' ...')
                    print('deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
                else:
                    print('DEMO: deleting file ' + file + ' sleep:' + str(sleepms) + ' ...')
            except Exception as e:
                print(e)
    else:
        Copy_file(file)  # 如果目标文件不存在，先备份，本次不删除

# 获取当前目录下的文件和目录
def folderfilelist(folder):
    folderlists =[]
    filelists = []

    for file in os.listdir(folder):
        file = os.path.join(folder,file)
        if os.path.isdir(file):
            folderlists.append(file)
        else:
            filelists.append(file)

    return filelists,folderlists


def Delete_folder(path):
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting folder ' + path + ' ...')
            Write_log('deleting folder ' + path)
        except Exception as e:
            #print(e)
            Write_log(e)

def Delete_folderAndfile(path):
    filelists,folderlists = folderfilelist(path)
    for file in filelists:
        print('deleting file in NG folder ' + path + ' ...')
        Write_log('deleting file in NG folder ' + path)
        os.remove(file)
    for folder in folderlists:
        Delete_folderAndfile(folder)
    # 如果上面文件都删除了，那就把目录也删除掉
    if os.path.isdir(path):
        try:
            os.rmdir(path)  # 删空目录,如果目录里文件不空,则不能删除
            print('deleting NG folder' + path + ' ...')
            Write_log('deleting folder ' + path)
        except Exception as e:
            #print(e)
            Write_log(e)


def Scan_path(rootDir):
    rootDir = r'' + rootDir
    curr_date = (datetime.datetime.now()).strftime("%Y\%m\%d")

    # 只遍历当前文件夹下的文件夹和文件
    for lists in os.listdir(rootDir):
        curr_path = os.path.join(rootDir, lists)
        nopathfolder = curr_path.split('\\')[-1]
        #print('curr_path',curr_path,curr_path.split('\\')[-1])
        if os.path.isdir(curr_path):

            if curr_date in curr_path:
                # 保护目录，不操作
                continue
            # NG文件夹直接删除
            if nopathfolder.upper() == "NG":
                #print('ng=',curr_path)
                Delete_folderAndfile(curr_path)
                continue
            Scan_path(curr_path)  # 递归调用自己
        else:
            # 复制当前目录下的文件
            Delete_file(curr_path)
        # 删除当前文件夹
        Delete_folder(curr_path)





