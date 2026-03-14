# 3. Design automation script which accept two directory names. Copy all files from first directory 
# into second directory. Second directory should be created at run time. 
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files from Demo to Temp. 

# Usage : DirectoryCopy.py “Demo” “Temp” 

import sys
import os
import shutil

def directory_scanner(src_dir, dest_dir):

    Ret = False

    Ret = os.path.exists(src_dir)

    if (Ret == False):
        print("Source directory does not exist")
        return
    
    Ret = os.path.isdir(src_dir)

    if(Ret == False):
        print("Source path is not a directory")
        return
    
    Ret = os.path.exists(dest_dir)

    if(Ret == False):
        os.mkdir(dest_dir)
        print("Directory created:", dest_dir)

    for folder, subfolder, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(folder, file)
            dest_file = os.path.join(dest_dir, file)

            shutil.copy(src_file, dest_file)
            print("Copied:", file)

    print("-" * 40)
    print("Copying completed successfully")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py Demo Temp")
        return

    directory_scanner(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
