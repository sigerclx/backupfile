import os,glob,shutil,datetime,time



spath = r"d:\pic1\2021\01"
spath = r"C:\Windows"
dpath = r"Y:\pic1"
allpic_files = []
allpic_dirs = []

# t1=time.time()
#
#
# for i in glob.glob(spath + '/**/*', recursive=True):
#     if os.path.isfile(i):
#         allpic_dirs.append(i)
#         #print(i)
# print(len(allpic_dirs))
# t2=time.time()
# print("相差",round((t2-t1),3),"s")
def is_valid_date(str):
  '''判断是否是一个有效的日期字符串'''
  try:
    time.strptime(str, "%Y\%m\%d")
    return True
  except:
    return False

print(is_valid_date(r'2021\02\04'))

def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            #pass
            allpic_dirs.append(os.path.join(root,f))
    print(len(allpic_dirs))

t1=time.time()
allpic_dirs = []
Test1(spath)
t2=time.time()
print("相差",round((t2-t1),3),"s")


#读当前目录下的文件夹和文件，只读当前层
# def Test2(rootDir):
#     for lists in os.listdir(rootDir):
#         path = os.path.join(rootDir, lists)
#         print(path)
#         if os.path.isdir(path):
#             allpic_dirs.append(path)
#     print(len(allpic_dirs))
#
#
# t1=time.time()
# allpic_dirs = []
# Test2(spath)
# t2=time.time()
# print("相差",round((t2-t1),3),"s")




#
# for i in glob.glob(spath + '/**/*', recursive=True):
#     if os.path.isfile(i):
#         allpic_files.append(i)
#
# allpic =  len(allpic_files)
# print(allpic,allpic_files)
# print('======')
# curr_date = (datetime.datetime.now()).strftime("%Y\%m\%d")
# print(curr_date)
# for file in allpic_files:
#     dest = file.replace(spath,dpath)
#     path = dest[0:dest.rfind("\\")]
#     if curr_date in file:
#         break
#     if not os.path.exists(path):
#         os.makedirs(path)
#     if not os.path.exists(dest):
#         shutil.copy2(file,dest)
#         print(file,dest)
#
#





#shutil.move(r"C:\Users\Jacky\Pictures\ocr1.jpg", r"C:\Users\Jacky\Pictures\1")




