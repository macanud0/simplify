# find-move.py
import os, sys
import shutil
import argparse as ap
 

def findFileInDir(dir, file_name, target_dir):
    dir_name = str(target_dir) + '_books'
    for root, dirs, files in os.walk(dir):
            
        for file in files:           
            if file_name in file:
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
    parser = ap.ArgumentParser(description="Find files and move script")
    parser.add_argument("--source")
    parser.add_argument("--file")
    parser.add_argument("--td", help="optional target directory name")
    
    args, leftovers = parser.parse_known_args()

    if args.source is not None and args.file is not None:
        print "Source and file have been set (values are %s, %s)" % args.source, args.file
        target_dir = args.td if args.td is not None else args.file
        findFileInDir(args.source, args.file, target_dir)
    else:
        print('Usage: python find-move.py --source [source_dir] --file file [target_file_name] --td [Optional: target_dir]')