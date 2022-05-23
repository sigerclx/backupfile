import os,glob,shutil

class BackupFile():
    def __init__(self,source_path,dest_path):
        self.source_path = source_path
        self.dest_path = dest_path

    # 根据源文件夹，在目标文件夹建立相同目录结构
    def Create_folder(self):
        if not os.path.exists(self.dest_path):
            os.makedirs(self.dest_path)

    def Copy_file(self):
        fileList = open('log.txt', mode='a', encoding='utf-8')
        if os.path.exists(self.source_path):
            self.Create_folder(self.dest_path)
        else:
            fileList.writelines(self.source_path + " is not exist! \n")
            fileList.flush()
            fileList.close()
            return
        # 复制文件
        for i in glob.glob(self.source_path + '/**/*', recursive=True):
            if os.path.isfile(i):
                if not os.path.exists(i.replace(self.source_path, self.dest_path)):
                    shutil.copy2(i, dest_path)
                    fileList.writelines(i + " " + dest_path + "\n")
                    fileList.flush()

        fileList.close()