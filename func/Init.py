from func.Write_log import Write_log
from func.tools import *
from func.param import *
import os

def Read_folder():
    source_path = Get_value('source_path')  # 定义源文件夹
    dest_path = Get_value('dest_path')  # 定义目的文件夹

    while not os.path.exists(source_path) or not os.path.exists(dest_path) :
        if not os.path.exists(source_path):
            print('源目录 '+source_path+' 不存在!')
            Write_log('源目录 '+source_path+' 不存在!')
        if not os.path.exists(dest_path):
            print('目标目录 '+dest_path+' 不存在!')
            Write_log('目标目录 '+dest_path+' 不存在!')
        time.sleep(Get_value("scanfoldertime"))

def ini_init():
    # 首先判断config.ini 在不在,不在就创建一个,就是为了方便.
    if not os.path.exists('config.ini'):
        Write_log("[param]",timelog='off',configfile='config')
        Write_log(r"source_path = d:\pic1", timelog='off',configfile='config')
        Write_log(r"dest_path = y:\pic1", timelog='off',configfile='config')
        # 该参数是保留最近多少天delete_before_days的数据
        Write_log("delete_before_days = 20", timelog='off',configfile='config')
        # 每次copy,清理后休息sleeptime时间
        Write_log("sleeptime = 5 * 2", timelog='off',configfile='config')
        # 每次开始copy,清理前如果 源文件夹和目的文件夹不在,则报错,过scanfoldertime时间后,再测一遍
        Write_log("scanfoldertime = 5 * 2", timelog='off', configfile='config')
        # 每删除一个文件休息delete_onefile_sleep时间
        Write_log("delete_onefile_sleep = 0.03", timelog='off', configfile='config')
        # 每拷贝一个文件休息copy_onefile_sleep时间s
        Write_log("copy_onefile_sleep = 0.03", timelog='off', configfile='config')
        # 程序演示，copy是真实的，删除的是demo,1为删除，0为演示
        Write_log("deletefile = 1", timelog='off', configfile='config')

    Read_config()

def Read_config():
    Set_value('source_path', r'' + Read_ini('source_path'))  # 定义源文件夹
    Set_value('dest_path', r'' + Read_ini('dest_path'))  # 定义目的文件夹
    Set_value('delete_before_days', int(Read_ini('delete_before_days'))) # 删除delete_days之前源数据
    Set_value('sleeptime', eval(Read_ini('sleeptime')))
    Set_value('scanfoldertime', eval(Read_ini('scanfoldertime')))
    Set_value('copy_onefile_sleep', float(Read_ini('copy_onefile_sleep')))
    Set_value('delete_onefile_sleep', float(Read_ini('delete_onefile_sleep')))
    Set_value('deletefile', int(Read_ini('deletefile')))
    Set_value('date_list', Get_copy_dates(Get_value("delete_before_days"), today=1))
