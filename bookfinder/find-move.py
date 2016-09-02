# find-move.py
import os, sys
import shutil
 

def findFileInDir(dir, fileName):
    dir_name = fileName + '_books'
    for root, dirs, files in os.walk(dir):
            
        for file in files:           
            if fileName in file:
               file_path = os.path.join(root, file)
               print(file_path)
               
               if not os.path.exists(dir_name):
                   os.makedirs(dir_name)
                   
               local_file = os.path.join(dir_name,file)
               print('Local file %s' % local_file)
               
               if not os.path.exists(local_file):
                   print('File does not exist. Moving.')                 
                   shutil.move(file_path, dir_name)
               else:
                   os.remove(file_path)   
                   
 
 
if __name__ == '__main__':
    if len(sys.argv) > 1: 
        findFileInDir(str(sys.argv[1]), str(sys.argv[2]))
    else:
        print('Usage: python find-move.py folder file')