import datetime,time,shutil,os,glob,sys

# 获取目录文件列表
def Get_file_list(source_path):
    files_list=[]
    for i in glob.glob(source_path + '/**/*', recursive=True):
        if os.path.isfile(i):
            files_list.append(i)
    return files_list

def Delete_file(path):
    # 删除目录下的文件,每删除一个文件,都休息delete_onefile_sleep时间
    sleepms = 0
    files_list = Get_file_list(path)
    for i in files_list:
        if os.path.exists(i):
            try:
                os.remove (i)
                #time.sleep(sleepms)
                #Write_log('deleting file ' + i + ' ...')
                #print('deleting file ' + i + ' sleep:' + sleepms + ' ...')
            except Exception as e:
                print(e)
                continue

t1=time.time()


each_dir ='d:\pic1'
# shutil.rmtree(each_dir)
Delete_file(each_dir)

t2=time.time()
print("相差",round((t2-t1),3),"s")